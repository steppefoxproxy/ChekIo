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

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
