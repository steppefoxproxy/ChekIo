def checkio(text):
    dic = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    arrayresult = {}
    for char in dic:
        count = 0
        for i in text:
            if i == char:
                count+=1
        if count != 0:
            arrayresult.update({char: count})
            #arrayresult.update({count: char})
    #print(arrayresult)
    z = max(arrayresult.values())
    
    for key, value in arrayresult.items():
        #print (key,value)
        if value == z:
            return key
    
    return None
        
    
    #replace this for solution


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    #assert checkio("How do you do?") == "o", "O is most wanted"
    #assert checkio("One") == "e", "All letter only once."
    #assert checkio("Oops!") == "o", "Don't forget about lower case."
    #assert checkio("AAaooo!!!!") == "a", "Only letters."
    #assert checkio("abe") == "a", "The First."
    #print("Start the long test")
    #assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    #print("The local tests are done.")
