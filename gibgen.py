import random
import sys
import re

def main():
    # check to see if a file is given
    if (len(sys.argv) < 2):
        print('Please run with a text file.')
        return

    # we only want to work with .txt files for now
    if (not (sys.argv[1].endswith('.txt'))):
        print('Please use a .txt file')
        return

    opFile = open(sys.argv[1])
    fileDat = opFile.read()

    if (len(fileDat) == 0):
        print('Your file is empty')
        return

    spChList = []
    spChIndexList = []

    formatedData = splitNsave(fileDat, spChList, spChIndexList)
    newString = ""

    # for each word, gibberize it
    for word in re.split('\s', formatedData):
        newString += gibberize(word)


    # add punctuation back in
    result = addPunct(newString, spChList, spChIndexList)

    print result
    exit()
    # end main()


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

    newWord = ""
    i = 0
    n = random.sample(range(0, len(letters)), len(letters))
    for ch in letters:
        newWord += letters[n[i]]
        i += 1

    return firstLetter + newWord + lastLetter
    # end gibberize()

def splitNsave(aString, spChList, spChIndexList):
    bigList = list(aString)
    index = 0
    toReturn = ""
    for ch in bigList:
        # if not alphabetical
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
    # if all characters in word are not Capitalized, return
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
