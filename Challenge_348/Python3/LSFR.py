import sys
import re

def main(*args):
    if len(args) != 5:
        print("Invalid arguments, use: [<tap-positions>] <feedback function> <initial value> <clock steps>")
    LFSR(args[1], args[2], args[3], args[4])  
     
# Implements a Linear Feedback Shift Register with two functions: XOR and XNOR
def LFSR(tapPositions, function, initialValue, clockAmount):
    tapPositions = [2**int(item) for item in re.split('\[|,|\]',tapPositions) if item !=''] # Get proper bit positions from the tap positions
    workingValue = int(initialValue,2)
    for clockStep in range(0, int(clockAmount) + 1):
        print(format(workingValue,("0" + str(len(initialValue)) + "b")))
        for index in range(0, len(tapPositions)):
            if index == 0:
                leftBit = (workingValue & tapPositions[index]) // tapPositions[index]
            else:
                if function == "XOR":
                    leftBit = ((workingValue & tapPositions[index]) // tapPositions[index]) ^ leftBit
                if function == "XNOR":
                    leftBit = ((workingValue & tapPositions[index]) // tapPositions[index]) ^ leftBit
                    # Doing this rather than ~ as a series of 1's is negative
                    if leftBit == 0:
                        leftBit = 1
                    else:
                        leftBit = 0
        leftBit = leftBit * (2**(len(initialValue) - 1)) # Put the left most bit into the appropriate place
        workingValue = (workingValue >> 1) | leftBit

if __name__ == '__main__':
    main(*sys.argv)
