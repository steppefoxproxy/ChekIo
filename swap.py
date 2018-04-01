def swap(items,left,right):
    if left != right:
        temp = items[left]
        items[left] = items[right]
        items[right] = temp
    return items

def checkio(numbers_array):
    dataresult = list(numbers_array)
    i = 1
    j = 0
    swapbool = True
    while swapbool:
        swapbool = False
        while i < dataresult.__len__():
            if (abs(dataresult[i]) - abs(dataresult[i - 1])) < 0:
                swap(dataresult, i - 1, i)
                swapbool = True
            i += 1
        i = 1
    #print(dataresult)
    return dataresult

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
