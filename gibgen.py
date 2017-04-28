import random
import sys
import re
import fileinput

def main():
    spChList = []
    spChIndexList = []

    # we only want to work with .txt files for now
    if(len(sys.argv) == 2):
        if (sys.argv[1].endswith('.txt')):
            opFile = open(sys.argv[1])
            fileDat = opFile.read()
            formatStr(fileDat, spChList, spChIndexList)
            return

    # if they passed in a string
    if (isinstance(sys.argv[1], basestring)):
        return formatStr(sys.argv[1], spChList, spChIndexList)

    # to take into account other ways of passing in text
    if (sys.stdin):
        inputFile = fileinput.input()
        fileDat = inputFile.readline()
        formatStr(fileDat, spChList, spChIndexList)
        return


    exit()
    # end main()

def formatStr(toFormat, spCharList, spCharIndexes):
    newData = splitNsave(toFormat, spCharList, spCharIndexes)
    newString = ""
    # for each word, gibberize it
    for word in re.split('\s', newData):
        newString += gibberize(word)

    # add punctuation back in
    result = addPunct(newString, spCharList, spCharIndexes)

    print result
    # end formatStr()


def gibberize(toGib):
    letters = list(toGib)

    # if the list is of length <= 3, there is no need to gibberize
    if (len(letters) <= 3):
        return toGib

    # if word == abbreviation, return
    if (checkAbbr(toGib)):
        return toGib

    # grab first and last letters first and remove them from randomizer
    firstLetter = letters[0]
    lastLetter = letters[len(letters) - 1]

    del letters[0]
    del letters[len(letters) - 1]

    # loop if the word isn't scrambled. Max of 3 loops
    loopCount = 0
    while (loopCount < 3):
        newWord = ""
        i = 0
        # grab a set of random numbers to determine what characters are added
        n = random.sample(range(0, len(letters)), len(letters))
        for ch in letters:
            newWord += letters[n[i]]
            i += 1
        result = firstLetter + newWord + lastLetter
        if (result != toGib):
            break
        loopCount += 1

    return result
    # end gibberize()

def splitNsave(aString, spChList, spChIndexList):
    # splits a string by the special characters (punctuations) and stores into a list
    bigList = list(aString)
    index = 0
    toReturn = ""
    for ch in bigList:
        # if not alphabetical, add to the special character list and store its' index
        if (not re.match('[a-zA-Z]', ch)):
            spChList.append(ch)
            spChIndexList.append(index)
            # if a "whitespace" character, add to return string
            if (re.match('\s', ch)):
                toReturn += ch
        else:
            toReturn += ch
        index += 1

    return toReturn
    # end splitNsave

def checkAbbr(word):
    # assuming words with all capital letters are abbreviations
    for ch in list(word):
        if (not re.match("[A-Z]", ch)):
            return False
    # if any character in the word is not capitalized, return false
    # else, return true
    return True
    # end checkAbbr()

def addPunct(aString, charList, chIndexList):
    # break the string down into a list to add the proper punctuation in
    strList = list(aString)

    i = 0
    for ch in charList:
        strList.insert(chIndexList[i], charList[i])
        i += 1
 
    result = ""
    i = 0
    for ch in strList:
        result += strList[i]
        i += 1

    return result
    # end addPunct

main()
