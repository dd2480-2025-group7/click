import pytest
import os
from click._compat import open_stream 
# Test suite for testing and improving branch coverage for open_stream in _compat.py

def test_open_stream_raises_a():
    #tests that we get error when "a" in atomic mode
    # we can't have mode "a" if atomic is True
    with pytest.raises(ValueError, match="Appending to an existing file is not supported"): # verifies that Valueerror is raised
        open_stream("testfile.txt", mode="a", atomic=True) # we don't need an actual file since it won't be opened

def test_open_stream_raises_x():
    #Tests that open_stream raises ValueError when 'x' is used in atomic mode
    with pytest.raises(ValueError, match="Use the `overwrite`-parameter instead"): #verifies that ValueError is raised
        open_stream("testfile.txt", mode="x", atomic=True)

def test_open_stream_raises_r_and_rb():
    # Tests that open_stream raises ValueError when 'w' is not in mode and we have atomic
    # mode r
    with pytest.raises(ValueError, match="Atomic writes only make sense with `w`-mode"):
        open_stream("testfile.txt", mode="r", atomic=True)

    #mode rb
    with pytest.raises(ValueError, match="Atomic writes only make sense with `w`-mode"):
        open_stream("testfile.txt", mode="rb", atomic=True)

if __name__ == "__main__":
    pytest.main()