#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = 0 
try:
    n = int(sys.argv[1]) 
except:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4") 
    sys.exit(1)

solutions = []
col = set()
pos_diag = set() 
neg_diag = set()

def solve(r):
    if r == n: 
        copy = solutions[:]
        solutions.append(copy)
        return  
    for c in range(n):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue
        
        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        solutions.append([r, c])
        
        solve(r + 1)
        
        col.remove(c)
        pos_diag.remove(r + c) 
        neg_diag.remove(r - c)
        solutions.pop()
        
solve(0)
for solution in solutions:
    print(solution)
