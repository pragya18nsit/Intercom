import math
import utils.const as const
from decimal import Decimal
from numbers import Number

def validateLatitude(latitude):
    """
    Validates a latitude

    Args:
    latitude (Decimal): latitude that is input

    Output:
    result (bool): True if latitude is valid, False if latitude is invalid
    """

    if isinstance(latitude,Number):
        if latitude>=-90 and latitude<=90:
            return True
    return False

def validateLongitude(longitude):
    """
    Validates a longitude

    Args:
    latitude (Decimal): longitude that is input

    Output:
    result (bool): True if longitude is valid, False if longitude is invalid
    """

    if isinstance(longitude,Number):
        if longitude>=-180 and longitude<=180:
            return True
    return False

def longitudeDifference(longitude1,longitude2):
    """
    Calculated difference between two longitudes

    Args:
    longitude1(Decimal): first longitude coordinate in radians
    longitude2(Decimal): second longitude coordinate in radians

    Output
    result(Decimal): difference between latitude1 and latitude2 in radians
    """

    return longitude1-longitude2

def getCentralAngle(latitude1,longitude1,latitude2,longitude2):
    """
    Calculates central angle between two coordinates

    Args:
    latitude1(Decimal): first latitude coordinate
    longitude1(Decimal): first longitude coordinate
    latitude2(Decimal): second latitude coordinate
    longitude2(Decimal): second longitude coordinate

    Output
    result(Decimal): central angle in radians
    """

    longDiff=longitudeDifference(longitude1,longitude2)
    centralAngle=math.acos(math.sin(latitude1) * math.sin(latitude2) + math.cos(latitude1) * math.cos(latitude2) * math.cos(longDiff))
    return Decimal(centralAngle)

def getDistance(latitude1,longitude1,latitude2,longitude2):
    """
    Calculated the distance between two coordinates in km

    Args:
    latitude1(Decimal): first latitude coordinate
    longitude1(Decimal): first longitude coordinate
    latitude2(Decimal): second latitude coordinate
    longitude2(Decimal): second longitude coordinate

    Output
    result(Decimal): distance between coordinates
    """
    if not validateLatitude(latitude1) or not validateLatitude(latitude2):
        raise Exception("Latitude is not valid")

    if not validateLongitude(longitude1) or not validateLongitude(longitude2):
        raise Exception("Longitude is not valid")
    
    latitude1=math.radians(latitude1)
    latitude2=math.radians(latitude2)
    longitude1=math.radians(longitude1)
    longitude2=math.radians(longitude2)

    distance=const.EARTH_RADIUS * getCentralAngle(latitude1,longitude1,latitude2,longitude2)

    return distance
