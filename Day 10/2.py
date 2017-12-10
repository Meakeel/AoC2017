def encrpyt(data, numberInLoops):
    denseArray = []
    currentPosition = 0
    skipSize = 0
    
    matrix = [ord(x) for x in data] + [17, 31, 73, 47, 23]

    for round in range(64):
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

    #calculate the sparse hash list 16 numbers

    for x in range(0, 16):
        subslice = numberInLoops[16 * x:16 * x + 16]

        toAdd = subslice[0]
        for sub in range(1, len(subslice)):
            toAdd = toAdd ^ subslice[sub]

        toHex = '%02x' % toAdd
        denseArray.append(toHex)
    
    print(''.join(denseArray))
    
    return 0

puzzleInput = "189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"
#puzzleInput="1,2,3"
puzzleInputLoops = [x for x in range(0, 256)]
result = encrpyt(puzzleInput, puzzleInputLoops)
