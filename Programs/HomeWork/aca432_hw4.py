"""
Antoine Assaf - aca432
CS 1134
Homework 1
"""
#Question 1:
def insomewhere(X, s):
    if len(X) == 0:
        return False
    if isinstance(X[0], list):
        return bool(insomewhere(X[0],s) + insomewhere(X[1:],s))
    elif s in X:
        return True
    else:
        return insomewhere(X[1: ],s)
        
#Question 2:          
A=[[1,2],[3,[[[4],5]],6],7,8]
print(insomewhere(A,6))

def unnest(X):
    if len(X) == 0:
        return X
    if isinstance(X[0], list):
        return unnest(X[0]) + unnest(X[1:])
    else:
        return X[:1] + unnest(X[1:])
    
print(unnest(A))

#Question 3:
def print2d(X):
    print('[')
    for ele in X:
        print('',ele)
    print(']')

print2d([[i]*5 for i in range(5)]) 

#Question 4:
def triangle(n):
    x = n-1
    while x >= 0:
        yield [i for i in range(n,x,-1)]
        x -= 1

print2d(triangle(5))

#Question 5:
def table(f, xrange, yrange):
    for i in yrange:
        yield [f(j,i) for j in xrange]

print2d(table(pow,[1,2,10], range(10,15)))

#Question 6:
def nest(x,n):
    for i in range (n):
        x = [x]
    return x

B = nest('nest',2)
print(B)
print(unnest(B))

#Question 7:
C=[[1],[1]]*5
print(C)
C[3][0]=5
print(C)


