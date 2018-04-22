def between_markers(text: str, begin: str, end: str) -> str:
    idbegin = text.find(begin,0,len(text))
    idend = text.find(end,0,len(text))
    if idbegin == -1 and idend ==-1:
		return(text)
	elif idbegin == -1:
		return(text[0:idend:])
	elif idend == -1:
		return(text[idbegin+len(begin)::])
	elif idbegin < idend:
		return(text[idbegin+len(begin):idend:])
	elif idbegin > idend:
		return('')
        
def checkio(expression):
    list_char = ['(',')','[',']','{','}']
    #print(list_char[1])
    print(between_markers(expression,list_char[0],list_char[1] ))
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("((5+3)*2+1)"))
    #assert checkio("((5+3)*2+1)") == True, "Simple"
    #assert checkio("{[(3+1)+2]+}") == True, "Different types"
    #assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    #assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    #assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    #assert checkio("2+3") == True, "No brackets, no problem"
