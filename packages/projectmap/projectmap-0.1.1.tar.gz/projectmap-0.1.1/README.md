# ProjectMap

A modern Python tool for creating visual maps of project structures in the terminal.

## Installation

```bash
pip install projectmap
```

## Features
- **Interactive Project Mapping**: Visualize your project's structure with clear, hierarchical representations
- **Smart Filtering**: Built-in ignore patterns for common development artifacts
- **Flexible Configuration**: Easily customize which files and directories to include or exclude
- **Clean Unicode Output**: Beautiful terminal visualization using box-drawing characters
- **Python API & CLI**: Use as a command-line tool or integrate into your Python applications
- **Intelligent Sorting**: Organized display with directories first, followed by files

## Quick Start

### Command Line
```bash
# Map current directory
projectmap

# Map specific directory
projectmap --path /path/to/project

# Custom ignore patterns
projectmap --path . --ignore-dirs "logs" "temp" --ignore-files "*.tmp" "*.bak"
```

### Python API
```python
from projectmap import ProjectStructureVisualizer

# Basic usage
visualizer = ProjectStructureVisualizer()
visualizer.visualize('.')

# Custom configuration
visualizer = ProjectStructureVisualizer(
    ignore_dirs={'logs', 'temp'},
    ignore_files={'.env', '*.bak'}
)
visualizer.visualize('/path/to/project')
```

## Example Output

```
Project Structure (/your/project):
──────────────────────────────
├── src
│   └── projectmap
│       ├── __init__.py
│       └── visualizer.py
├── tests
│   └── test_visualizer.py
├── docs
│   ├── api.md
│   └── usage.md
├── README.md
├── pyproject.toml
└── LICENSE
──────────────────────────────
```

## Configuration

### Default Ignored Patterns

#### Directories
```python
DEFAULT_IGNORE_DIRS = {
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
    '.tox'
}
```

#### Files
```python
DEFAULT_IGNORE_FILES = {
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
```

## Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/projectmap.git
cd projectmap

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development version
pip install -e ".[dev]"

# Run tests
pytest
```

## Project Structure

```
projectmap/
├── src/
│   └── projectmap/
│       ├── __init__.py
│       └── visualizer.py
├── tests/
│   └── test_visualizer.py
├── README.md
├── pyproject.toml
└── LICENSE
```

## Package Configuration (pyproject.toml)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "projectmap"
version = "0.1.0"
description = "A modern tool for visualizing project structures in the terminal"
readme = "README.md"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["project", "structure", "visualization", "tree", "map"]
dependencies = [
    "pathlib",
]
requires-python = ">=3.7"

[project.optional-dependencies]
dev = ["pytest"]

[project.urls]
Homepage = "https://github.com/username/projectmap"

[project.scripts]
projectmap = "projectmap.visualizer:main"
```

## Roadmap

### Version 0.2.0
- Color output support
- Export to JSON/YAML
- Custom depth limits

### Version 0.3.0
- File size information
- Directory statistics
- Pattern-based filtering

### Version 0.4.0
- Git integration
- Multiple output formats
- Interactive mode

## Contributing

We welcome contributions! Here's how you can help:

1. Check our [issues page](https://github.com/yourusername/projectmap/issues)
2. Fork the repository
3. Create a feature branch
4. Write your changes
5. Submit a pull request

## License

MIT License - feel free to use this project for your needs.

## Support

- GitHub Issues: [https://github.com/yourusername/projectmap/issues](https://github.com/yourusername/projectmap/issues)
- Documentation: [https://projectmap.readthedocs.io](https://projectmap.readthedocs.io)