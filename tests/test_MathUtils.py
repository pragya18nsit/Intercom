
import math
import pytest
from decimal import Decimal

from utils.mathUtils import validateLatitude, validateLongitude, getDistance


"""
test validateLatitude
"""
def testNoneArgs():
	assert validateLatitude(None) == False, "check_lat_arg fails with None arg"

def testStrArgs():
	assert validateLatitude("str") == False, "check_lat_arg fails with str arg"

def testTooSmall():
	assert validateLatitude(-90.0001) == False, "check_lat_arg fails with too small arg"

def testTooLarge():
	assert validateLatitude(90.0001) == False, "check_lat_arg fails with too large arg"

def testValidLat():
	assert validateLatitude(0) == True, "check_lat_arg fails with valid arg"

def testValidLat1():
	assert validateLatitude(35.374562) == True, "check_lat_arg fails with valids arg"


"""
test validateLongitude
"""
def testNoneArgsLong():
	assert validateLongitude(None) == False, "check_long_arg fails with None arg"

def testStrArgsLong():
	assert validateLongitude("str") == False, "check_long_arg fails with str arg"

def testTooSmallLong():
	assert validateLongitude(-180.0001) == False, "check_long_arg fails with too small arg"

def testTooLargeLong():
	assert validateLongitude(180.0001) == False, "check_long_arg fails with too large arg"

def testValidLong():
	assert validateLongitude(0) == True, "check_long_arg fails with valid arg"

def testValidLong1():
	assert validateLongitude(35.374562) == True, "check_long_arg fails with valids arg"



"""
test getDistance
"""

def testArgsNoneDistance():
    with pytest.raises(Exception) as e:
    	getDistance(None, None, None, None)

def testArgsStringDistance():
    with pytest.raises(Exception) as e:
    	getDistance("string", "string", "string", "string")

def testArgsListDistance():
    with pytest.raises(Exception) as e:
    	getDistance([0,0,0], [0,0,0], [0,0,0], [0,0,0])

def testArgsBoolDistance():
    with pytest.raises(Exception) as e:
	    assert getDistance(True, False, True, False)

def testArgsTupleDistance():
    with pytest.raises(Exception) as e:
    	getDistance((0,0,0), (0,0,0), (0,0,0), (0,0,0))

def testArgsDictDistance():
    with pytest.raises(Exception) as e:
    	getDistance({'i':0,'j':1}, {'i':0,'j':1}, {'i':0,'j':1}, {'i':0,'j':1})

def testWorkingDistance():
	# checked using online calculator and random coords
	assert math.isclose(getDistance(44.4523, -14.4543, -55.453, 24.2345), Decimal('10782'), rel_tol=0.5) == True