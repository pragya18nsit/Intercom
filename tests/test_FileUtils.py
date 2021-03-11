import pytest

from utils import fileUtils as futils
from utils import const



"""
test readFile
"""
def testNoneArgs():
    with pytest.raises(Exception) as e:
        futils.readFile(None)

def testNoFileRead():
    with pytest.raises(Exception) as e:
        futils.readFile("/test/file")

def testWorkingFile():
    file_lines = futils.readFile(const.INPUT_FILE_PATH)
    assert isinstance(file_lines, list), "not a list"
    for line in file_lines:
        assert isinstance(line, str), "lines are not strings"


"""
test writeToFile
"""
def testNoneArgsWrite():
    with pytest.raises(Exception) as e:
        futils.writeToFile(None, None)

def testNoPerson():
    with pytest.raises(Exception) as e:
        futils.writeToFile([], None)

def testNoFileWrite():
    with pytest.raises(Exception) as e:
        futils.writeToFile(["mock"], "/test/file")