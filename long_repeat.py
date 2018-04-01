def long_repeat(line):
    temp = {'none':0}
    buf = ''
    for i in line:
        #print(i)
        if temp.get(i) == None:
            temp.update({i:1})
        elif temp.get(i) != None and i == buf:
            temp.update({i:(temp.get(i)+1)})
        else:
            temp.update({i:1})
        buf = i
    print(temp)    
    return (max(temp.values()))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
