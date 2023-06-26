
from typing import *

def exist(board: List[List[str]], word: str) -> bool:
    def forwardtrack(x, y, seen, substr):
        if len(word) == 1 and board[0][0] == word:
            return True

        if (x,y) in seen or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        
        if substr + board[x][y] == word:
            return True

        if len(seen) >= len(word):
            return False

        if substr == word[:len(seen)] and word[len(seen)] != board[x][y]:
            return False
        
        if substr != word[:len(seen)]:
            return False
        
        
        else:
            dup_seen = seen.copy()
            dup_seen.add((x,y))
            new = substr + board[x][y]
            a = forwardtrack(x - 1, y, dup_seen, new)
            b = forwardtrack(x + 1, y, dup_seen, new)
            c = forwardtrack(x, y - 1, dup_seen, new)
            d = forwardtrack(x, y + 1, dup_seen, new)
            return a or b or c or d
            # seen.remove((x,y))
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if forwardtrack(x,y, set(), ''):
                return True 
            
    return False

print(exist([["a","a"]], "aa"))

