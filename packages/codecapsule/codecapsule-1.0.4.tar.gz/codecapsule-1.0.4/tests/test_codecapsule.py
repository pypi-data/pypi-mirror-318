import pytest
import os
import json
from codecapsule.__main__ import create_capsule, prepare_output_path

def test_create_capsule():
    # Create a temporary directory with some test files
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpddir:
        # Create some test files
        os.makedirs(os.path.join(tmpddir, 'src'))
        
        with open(os.path.join(tmpddir, 'src', 'test.py'), 'w') as f:
            f.write("def hello():\n    return 'world'")
        
        with open(os.path.join(tmpddir, 'README.md'), 'w') as f:
            f.write("# Test Project")
        
        # Run create_capsule
        capsule = create_capsule(tmpddir)
        
        # Assertions
        assert len(capsule) == 2
        assert any(item['path'] == 'src/test.py' for item in capsule)
        assert any(item['path'] == 'README.md' for item in capsule)

def test_prepare_output_path(tmp_path):
    # Test absolute path
    abs_path = str(tmp_path / "test.json")
    result = prepare_output_path(abs_path)
    assert result == abs_path
    
    # Test path without .json extension
    abs_path_no_ext = str(tmp_path / "test")
    result = prepare_output_path(abs_path_no_ext)
    assert result == abs_path

def test_ignore_patterns():
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpddir:
        # Create various files to test ignore patterns
        os.makedirs(os.path.join(tmpddir, '.git'))
        os.makedirs(os.path.join(tmpddir, '.venv'))
        
        with open(os.path.join(tmpddir, 'test.pyc'), 'wb') as f:
            f.write(b'some binary content')
        
        with open(os.path.join(tmpddir, 'test.txt'), 'w') as f:
            f.write("Hello world")
        
        # Run create_capsule
        capsule = create_capsule(tmpddir)
        
        # Assertions
        assert len(capsule) == 1
        assert capsule[0]['path'] == 'test.txt'