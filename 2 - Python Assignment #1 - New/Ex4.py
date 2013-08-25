#Ex4.py
#
#Variables:
#i - counter
#sq - square root
#squa - square of a number
#cube - cube of a number
#sqt,squat,cubet - verification variables
#
#Input: None
#Output: Number, Square Root, Square, and Cube of each number from 1 to 10
#Process: calculate > round final answers > print output

import math #import math functions
print "Number\t\tSquare Root\tSquare\t\tCube" #print table headers
i = 1 #set counter
while i < 11 : #start calculation loop
    sq = math.sqrt(i) #calc square root
    squa = i*i #calc square
    cube = i*i*i #calc cube
    sq = round(sq,2) #round data
    squa = round(squa,2)
    cube = round(cube,2)
    sqt = str(sq) + "|" #verify and clean .0s
    squat = str(squa) + "|"
    cubet = str(cube) + "|"
    if ".0|" in sqt :
        sq = int(sq)
    if ".0|" in squat :
        squa = int(squa)
    if ".0|" in cubet :
        cube = int(cube)
    print str(i) + "\t\t" + str(sq) + "\t\t" + str(squa) + "\t\t" + str(cube) #print output
    i = i+1 #advance counter
raw_input("Press the enter key to exit...") #delay
