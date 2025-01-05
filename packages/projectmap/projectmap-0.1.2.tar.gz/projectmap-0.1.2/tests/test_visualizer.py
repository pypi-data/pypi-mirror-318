from projectmap import ProjectStructureVisualizer

def test_should_ignore_directory():
    visualizer = ProjectStructureVisualizer()
    assert visualizer._should_ignore('__pycache__', True) == True
    assert visualizer._should_ignore('src', True) == False

def test_should_ignore_file():
    visualizer = ProjectStructureVisualizer()
    assert visualizer._should_ignore('.env', False) == True
    assert visualizer._should_ignore('main.py', False) == False