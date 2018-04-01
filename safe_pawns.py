def safe_pawns(pawns):
    chess = 'abcdefgh'
    save = set()
    count = 0
    for cell in pawns:
        # print(cell[0])
        # print(chess.find(cell[0],0,len(chess)))
        if chess.find(cell[0], 0, len(chess)) != 0:
            save.add(str(chess[chess.find(cell[0], 0, len(chess))-1])+str(int(cell[1])+1))
        if chess.find(cell[0], 0, len(chess)) != len(chess)-1:
            save.add(str(chess[chess.find(cell[0], 0, len(chess)) + 1])+str(int(cell[1])+1))
        # break
    for cell in pawns:
        if cell in save:
            count+=1
    return (save, count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
