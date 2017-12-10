def encrpyt(data, numberInLoops):
    currentPosition = 0
    skipSize = 0

    matrix = [int(x) for x in data.split(',')]
    
    for i in range(len(matrix)):
        arrayToReverse = []

        # Get the numbers to reverse
        for x in range(matrix[i]):
            n = (currentPosition + x) % len(numberInLoops)
            arrayToReverse.append(numberInLoops[n])
        
        # revserse them
        arrayToReverse.reverse()

        # and send them back
        for x in range(matrix[i]):
            n = (currentPosition + x) % len(numberInLoops)
            numberInLoops[n] = arrayToReverse[x]

        currentPosition += matrix[i]
        currentPosition += skipSize
        currentPosition = currentPosition % len(numberInLoops)

        skipSize += 1 
    return numberInLoops[0] * numberInLoops[1]


input = "3, 4, 1, 5"
inputLoops = [x for x in range(0, 5)]
result = encrpyt(input, inputLoops)
print(result)

puzzleInput = "189, 1, 111, 246, 254, 2, 0, 120, 215, 93, 255, 50, 84, 15, 94, 62"
puzzleInputLoops = [x for x in range(0,256)]
result = encrpyt(puzzleInput, puzzleInputLoops)
print(result)
