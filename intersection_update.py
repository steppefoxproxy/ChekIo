def checkio(first, second):
    firstarray = set(first.split(','))
    secondarray = set(second.split(','))
    result = ''
    # print(firstarray,secondarray)
    firstarray.intersection_update(secondarray)
    # print(sorted(firstarray))
    result = ','.join(sorted(firstarray))
    # print(result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # checkio("one,two,three", "four,five,one,two,six,three")
     assert checkio("hello,world", "hello,earth") == "hello", "Hello"
     assert checkio("one,two,three", "four,five,six") == "", "Too different"
     assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
