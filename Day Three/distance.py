
import ulamspiral

val = 312051
inital = 1

s = ulamspiral.UlamSpiral(val)

result1 = [(index, row.index(val)) for index, row in enumerate(s.rows) if val in row]
result2 = [(index, row.index(inital)) for index, row in enumerate(s.rows) if inital in row]

result = abs(result1[0][0] - result2[0][0]) + abs(result1[0][1] - result2[0][1])

print(result)
