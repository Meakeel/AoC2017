def processStream(stream):
    ignore_garbage = False
    result = 0
    open_data = 0
    garbage_count = 0
    open_garbage = False
    
    for c in stream:
        if open_garbage:
            if ignore_garbage:
                ignore_garbage = False
            elif c == '>':
                open_garbage = False
            elif c == '!':
                ignore_garbage = True
            else:
                garbage_count += 1
        else:
            if c == '{':
                open_data += 1
            elif c == '<':
                open_garbage = True
            elif c == '}':
                result += open_data
                open_data -= 1
    return garbage_count


# opens file with name of "test.txt"
f = open("e:\Personal\Advent of Code\Day 9\input.txt", "r")
wholeString = f.readline()

result = processStream(wholeString)
print(result)
