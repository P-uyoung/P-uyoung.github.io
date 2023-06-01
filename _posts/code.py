def solution(m, n, board):
    answer = 0
    order = [0 for _ in range(n)]
    
    def addScore():
        erase = set()
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] == '0':
                    continue
                check = board[y][x]+ board[y][x+1] + board[y+1][x] + board[y+1][x+1]
                if check == board[y][x]*4:
                    erase.update([(y,x), (y,x+1), (y+1,x), (y+1,x+1)])
        return erase
    
    def setBlock(erase):
        erase = sorted(erase, key=lambda x: x[0])
        for y, x in erase:
            n = order[x]
            board[y] = board[y][:x] + board[n][x] + board[y][x+1:]
            board[n] = board[n][:x] + '0' + board[n][x+1:] 
            order[x] += 1 
        
                    
    while True:
        for i in range(len(board)):
            print(board[i])
        print()
        erase = addScore()
        if len(erase) == 0:
            return answer
        answer += len(erase)
        setBlock(erase)
    
    return -1

print(solution(8,5 ,["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]))