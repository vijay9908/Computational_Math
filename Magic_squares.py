from itertools import permutations

''' We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant'''
''' magic constant = n(n^2+1)//2 '''

for p in permutations(range(1,10)):
    if sum(p[0:3])==15 and sum(p[3:6])==15 and sum(p[0::3])==15 and sum(p[1::3])==15 and (p[0]+p[4]+p[8]==15) and (p[2]+p[4]+p[6]==15):
        print(p)
        break

