import numpy as np
import copy

def reallocation(value):
    allResults = []
    matrix = []
    matrix = [int(i) for i in value.split()]
    matrixSize = len(matrix)

    anyMatch = False
    loopCounter = 0
    resultsCounter = 0

    while anyMatch == False:
        # largest number and index
        largestIndex = np.argmax(matrix)
        largestNumber = matrix[largestIndex]
        matrix[largestIndex] = 0

        loopCounter = 0
        for y in range(largestIndex + 1, matrixSize):
            if loopCounter == largestNumber:
                break
            matrix[y] = matrix[y] + 1
            loopCounter = loopCounter + 1

        while loopCounter < largestNumber:
            for z in range(matrixSize):
                if loopCounter == largestNumber:
                    break
                matrix[z] = matrix[z] + 1
                loopCounter = loopCounter + 1
        
        allResults.append(copy.deepcopy(matrix))
        resultsCounter = resultsCounter + 1

        resultCounterThing = 0
        for y in range(len(allResults)):
            if allResults[y] == matrix:
                resultCounterThing = resultCounterThing + 1
            
        if resultCounterThing > 1:
            break

    return(resultsCounter)


input = "0 2 7 0"
result = reallocation(input)
print(result)

resultInput = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
results = reallocation(resultInput)
print(results)
