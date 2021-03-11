import os
import json

from numbers import Number
import models.person as person

def readFile(inFilePath):
    """
    Reads file and returns contents of file

    Args:
    filePath: path to input file

    Output:
    fileLines(list[string]): list of lines in input
    """
    if os.path.isfile(inFilePath):
        try:
            fptr=open(inFilePath,"r")
            fileLines=fptr.readlines()
            fptr.close()
            return fileLines
        
        except:
            raise Exception("Cannot open input file")

    else:
        raise Exception("Cannot find input file")

def convertFileLinesToPersonList(fileLines):
    """
    Reads file lines and converts them to list of person objects

    Args:
    fileLines(list[string]): list containing lines of input

    Output:
    personList(list[Person]): input in the form of list of Person object 
    """ 
    people=list()

    try:
        for line in fileLines:
            line=json.loads(line.strip())
            people.append(Person(line["name"],line["user_id"],line["latitude"],line["longitude"]))
    except:
        raise Exception("Incorrect input format")

    if(len(people)==0):
        raise Exception("Input is empty")

    return people

def writeToFile(people,outFilePath):
    """
    writed list of invited people to file

    args:
    people(list[Person]): list of invited people
    outFilePath(string): output file path
    """
     # check lines is a list
    if not isinstance(people, list):
        raise Exception("paramter is not a list")

    # no lines in the file so print error message and return
    if len(people) == 0:
        raise Exception("no users provided")

    try:
        fptr=open(outFilePath,"w")
        for being in people:
            fptr.write(being.name+" "+str(being.userId)+"\n")
        return
    except:
        raise Exception("Cannot output")
