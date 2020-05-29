from itertools import combinations, permutations

''' The elements of array are row indeces of queens on a chess board.
Let N-queens stay on board of N*N game. '''
listin = [1,3,0,2] #sample Case of N=4 

def is_solution(listin):
    for (i1,i2) in combinations(range(len(listin)),2):
        if abs(i1-i2)==abs(listin[i1]-listin[i2]):
            return False
    return True

for perm in permutations(range(n)): #replace N
    if is_solution(perm):
        print(perm)
        break
    
''' Brute efficient till 13N '''