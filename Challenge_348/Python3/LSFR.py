import sys
import re

def main(*args):
    if len(args) != 5:
        print("Invalid arguments, use: [<tap-positions>] <feedback function> <initial value> <clock steps>")
    LFSR(args[1], args[2], args[3], args[4])       

def LFSR(tapPositions, function, initialValue, clockAmount):
    tapPositions = [2**int(item) for item in re.split('\[|,|\]',tapPositions) if item !=''] # Get proper bit positions from the tap positions
    print(initialValue)
    workingValue = bin(initialValue)
    for clockStep in range(0, int(clockAmount)):
        leftBit = 0
        for bitPosition in tapPositions:
            if function == "XOR":
                leftBit = ((bin(bitPosition) & bin(workingValue) >> bitPosition)) ^ bin(leftBit)
        print(leftBit)   
    print(tapPositions)

def test():
    print("hello")

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        test()
    else:
        main(*sys.argv)
