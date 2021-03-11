import pytest

import models.person as person
from utils.inviteUtils import getPeopleWithinThreshold


"""
test getPeopleWithinThreshold
"""
def test_none_args():
    with pytest.raises(Exception) as e:
        getPeopleWithinThreshold(None, None, None, None)

def test_invalid_lat_longs():
    with pytest.raises(Exception) as e:
        getPeopleWithinThreshold(None, None, 90.001, -180.532)

def test_invalid_threshold_dist():
    with pytest.raises(Exception) as e:
        getPeopleWithinThreshold([Person()], -1, 45.67, 23.0)