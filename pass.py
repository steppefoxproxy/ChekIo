def checkio(data):
    passdic = '1234567890qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ'
    num = False
    low = False
    up = False
    if data.__len__() < 10: 
        return False
    for word in data:
        if passdic.find(word) == -1:
            return False
        if passdic[:10:].find(word) != -1 and not num:
            num = True
        if passdic[10:36:].find(word) != -1 and not low:
            low = True
        if passdic[36:62:].find(word) != -1 and not up:
            up = True
            
    #print (data.__len__(), num,low,up)
    if num and low and up:
        return True
    else:
        return False

#Some hints
#Just check all conditions
#print(checkio('ULFFunH8ni'))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
