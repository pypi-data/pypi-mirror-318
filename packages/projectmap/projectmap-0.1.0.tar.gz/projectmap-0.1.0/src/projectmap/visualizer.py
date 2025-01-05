import os
import argparse
from pathlib import Path
from typing import List, Set


class ProjectStructureVisualizer:
    def __init__(self, ignore_dirs: Set[str] = None, ignore_files: Set[str] = None):
        self.ignore_dirs = ignore_dirs or {
            '__pycache__',
            '.git',
            '.idea',
            'venv',
            '.venv',
            'env',
            'node_modules',
            '.pytest_cache',
            '.mypy_cache',
            '.ruff_cache',
            'build',
            'dist',
            'htmlcov',  # coverage reports
            '.coverage',  # coverage data
            '.tox',
            'migration',
            'data'
        }
        self.ignore_files = ignore_files or {
            '.gitignore',
            '.env',
            '.env.local',
            '.env.development',
            '.env.production',
            '.DS_Store',
            '*.pyc',
            '*.pyo',
            '*.pyd',
            '.python-version',
            '*.so',
            '*.egg',
            '*.egg-info',
            '*.log',
            '.coverage',
            'coverage.xml',
            '.coverage.*'
        }

    def _should_ignore(self, name: str, is_dir: bool = False) -> bool:
        """Проверяет, нужно ли игнорировать файл или директорию"""
        if is_dir:
            return name in self.ignore_dirs

        # Проверка на паттерны файлов
        for pattern in self.ignore_files:
            if pattern.startswith('*.'):
                if name.endswith(pattern[1:]):
                    return True
            elif pattern == name:
                return True
        return False

    def visualize(self, start_path: str = '.', level: int = 0, prefix: str = '') -> None:
        """Рекурсивно визуализирует структуру проекта"""
        path = Path(start_path)

        # Получаем списки файлов и директорий
        try:
            items = list(path.iterdir())
        except PermissionError:
            print(f"{prefix}├── [Permission Denied]")
            return

        # Сортируем: сначала директории, потом файлы
        items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

        for index, item in enumerate(items):
            is_last = index == len(items) - 1

            if self._should_ignore(item.name, item.is_dir()):
                continue

            # Определяем префикс для текущего элемента
            current_prefix = '└── ' if is_last else '├── '

            # Определяем префикс для следующего уровня
            next_level_prefix = '    ' if is_last else '│   '

            print(f"{prefix}{current_prefix}{item.name}")

            if item.is_dir():
                self.visualize(item, level + 1, prefix + next_level_prefix)


def main():
    parser = argparse.ArgumentParser(description='Визуализация структуры проекта')
    parser.add_argument('--path', default='.', help='Путь к корню проекта')
    parser.add_argument('--ignore-dirs', nargs='*', help='Дополнительные директории для игнорирования')
    parser.add_argument('--ignore-files', nargs='*', help='Дополнительные файлы для игнорирования')

    args = parser.parse_args()

    ignore_dirs = set()
    ignore_files = set()

    if args.ignore_dirs:
        ignore_dirs.update(args.ignore_dirs)
    if args.ignore_files:
        ignore_files.update(args.ignore_files)

    visualizer = ProjectStructureVisualizer(ignore_dirs, ignore_files)
    print(f"\nСтруктура проекта ({os.path.abspath(args.path)}):")
    print("─" * 50)
    visualizer.visualize(args.path)
    print("─" * 50)


if __name__ == '__main__':
    main()