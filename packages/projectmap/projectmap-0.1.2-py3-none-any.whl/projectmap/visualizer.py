import os
import argparse
from pathlib import Path
from typing import Set


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
            'htmlcov',
            '.coverage',
            '.tox',
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
        if is_dir:
            return name in self.ignore_dirs

        for pattern in self.ignore_files:
            if pattern.startswith('*.'):
                if name.endswith(pattern[1:]):
                    return True
            elif pattern == name:
                return True
        return False

    def visualize(self, start_path: str = '.', level: int = 0, prefix: str = '') -> None:
        path = Path(start_path)

        try:
            items = list(path.iterdir())
        except PermissionError:
            print(f"{prefix}├── [Permission Denied]")
            return

        items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

        for index, item in enumerate(items):
            is_last = index == len(items) - 1

            if self._should_ignore(item.name, item.is_dir()):
                continue

            current_prefix = '└── ' if is_last else '├── '

            next_level_prefix = '    ' if is_last else '│   '

            print(f"{prefix}{current_prefix}{item.name}")

            if item.is_dir():
                self.visualize(item, level + 1, prefix + next_level_prefix)


def main():
    parser = argparse.ArgumentParser(description='Project structure visualization')
    parser.add_argument('--path', default='.', help='Path to project root')
    parser.add_argument('--ignore-dirs', nargs='*', help='Additional directories to ignore')
    parser.add_argument('--ignore-files', nargs='*', help='Additional files to ignore')

    args = parser.parse_args()

    ignore_dirs = set()
    ignore_files = set()

    if args.ignore_dirs:
        ignore_dirs.update(args.ignore_dirs)
    if args.ignore_files:
        ignore_files.update(args.ignore_files)

    visualizer = ProjectStructureVisualizer(ignore_dirs, ignore_files)
    print(f"\nProject structure ({os.path.abspath(args.path)}):")
    print("─" * 50)
    visualizer.visualize(args.path)
    print("─" * 50)


if __name__ == '__main__':
    main()