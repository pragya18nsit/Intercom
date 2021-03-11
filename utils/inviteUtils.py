import os
import utils.mathUtils as mathUtils
import utils.const
from decimal import Decimal
import models.person as person
from numbers import Number

def getPeopleWithinThreshold(people,threshold,latitude,longitude):
    """
    Processes people and returns people within threshold distance of input latitude and longitude coordinates

    args:
    people(list[Person]): list of person
    threshold (decimal): threshold distance
    latitude(decimal): Dublin latitude
    longitude(decimal): Dublin longitude

    output:
    invitedPeople (list[Person]): list of person within threshold
    """
    if not isinstance(threshold,Number):
        raise Exception("threshold is invalid")
    invitedPeople=list()
    for being in people:
        dist=mathUtils.getDistance(latitude,longitude,being.latitude,being.longitude)
        if dist<threshold:
            invitedPeople.append(being)
    return invitedPeople

def sortInvitedPeople(people):
    """
    Sorts invited people by User id

    args:
    people(list[Person]): list of invited people

    output:
    sortedPerople(list[Person]): list of invited people sorted by id in ascending order
    """

    sortedInvitedPeople=sorted(people, key=lambda p:p.userId)
    return sortedInvitedPeople




