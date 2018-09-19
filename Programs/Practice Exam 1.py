#Question 2:
'''
6n+12 = O(n)    f(n) = O(g(n))
f(n) = 6n +12   g(n) = n
f(n) < cg(n)    n > n0
gn+12 < cn      n > n0
g+12/n < c      n > n0
18 <c           n0 = 1
'''
#Question 3: Theta(n log(n))

#Question 4:
def summation(x,n):
    total = 0
    product = 1
    for i in range(n+1):
        total += product
        product *= x
    return total
'''Runtime O(N)'''
print(summation(3,2))

#Question 5:
'''Runtime O(N^2)'''
def anyincommon(A,B):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i +=1
        else:
            return True
    return False
print(anyincommon([1,2,3,4,5,10,11],[6,7,8,9,11]))    
'''Runtime O(N)'''

def anyincommon1(A,B):
    for a in A:
        if(binarySearch(a,B)):
                return True
    return False

def binarySearch(key, L):
    low = 0
    high = len(L) - 1
    while (low <= high):
        mid = (low+high)//2
        if L[mid] == key:
            return True
        elif L[mid] > key:
            high = mid - 1
        else:
            low = mid+1
    return False
print(anyincommon1([1,2,3,4,5,10,11],[6,7,8,9,11]))   

#Question 6:
'''
i) 0,1,2,3,4
ii)0,0,0,0,0
iii)0,0,0,0,0
'''
#Question 7:
'''
i)Runtime without recursive call O(N)
ii) N recursive calls
iii) Runtime of N^2: N recursive calls of N runtime
'''
#iv)
def rev(A, x = None):
    if x == None:
        x = len(A) - 1
    if x == 0:
        return [A[x]]
    else:
        return [A[x]] + rev(A, x - 1)
 
print(rev([1,2,3,4,5,6]))

'''
i) O(i)
ii)n recursive calls
iii) O(N) total runtime
'''

#viii)
'''
push all elements into a stack, then proceed to reappending it into the list using pop
Runtime = O(N)
'''

#Question 8
def flipArray(A):
    n = len(A)
    B = []
    for i in range(n):
        temp = []
        for j in range (len(A[i])):
            temp.append(A[j][i])
        B.append(temp)
    return B

def reflip(A):
    B = zip(*A)
    return B



A = [[1,2,3],[4,5,6],[7,8,9]]
B = flipArray(A)
print(B)
C = reflip(A)
print(C)
#Question 9
def f(n,i=0):
    if n>0:
        i=f(n-1,i)
        i=f(n-1,i)
    print(i)
    return i+1
'''Runtime: (2^n)'''
#Question 10:
import collections

class flipstack:
    def __init__(self):
        self.q=collections.deque()

    def push(self,i):
        self.q.append(i)

    def pop(self):
        return self.q.pop()

    def flip(self):
        temp_q=collections.deque()
        for i in range(len(self.q)):
            temp_q.append(self.q.pop())
        self.q=temp_q    

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        return str(self.q)

#Question 11:
def binary(n):
    if n == 0:
        return ''
    else:
        new_n = n//2
        return str(binary(new_n)) + str(n%2)

print(binary(130))
