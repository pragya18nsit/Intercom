from models import Person
import utils.fileUtils as fileUtils
import utils.inviteUtils as inviteUtils
import utils.const as const

fileLines=fileUtils.readFile(const.INPUT_FILE)
allPeople=fileUtils.convertFileLinesToPersonList(fileLines)
invitedPeople=inviteUtils.getPeopleWithinThreshold(allPeople,const.THRESHOLD,const.DUBLIN_LATITUDE,const.DUBLIN_LONGITUDE)
sortedInvitedPeople=inviteUtils.sortInvitedPeople(invitedPeople)
fileUtils.writeToFile(sortedInvitedPeople,const.OUTPUT_FILE)