#Stupid sort in O(N^2) Runtime

def selection_sorted(A):
    R=[]
    while len(A) > 0:
        m = min(A)
        for i in range (len(A)):
            if A[i] == m:
                del A[i]
            R.append(m)
    return R

#HeapSort : O(nlog(n)) Runtime
#BSTSort: O(nlog(n)) Runtime
#MergeSort: n(log(n))
def mergesort(A):
    if len(A) > 2: 
        B = A[:len(A)//2]
        C = A[len(A)/2:]
        mergesort(B)
        mergesort(C)
        #merge(A,B,C) #Need to code
#QuickSort: O(n^2) WORST CASE , O(nlog(n)) USUALLY
def quicksort(A, l = 0, h= None):
    if l < h:
        i = partition(A,l,h)
        quicksort(A,l,i-1)
        quicksort(A,i+1,h)


def pivot(A,l,r):
    p = A[l]
    i = l+1
    j = r
    while  i < j:
        while A[i] < p and i < j:
            i+=1
        while A[j]>p:
            j=j-1
        if i < j:
            A[i],A[j] = A[j], A[i]
    A[0],A[j] = A[j] = A[j],A[0]
    return j

def true_quicksort(A,l,r):
    if l <r:
        m = pivot(A,l,r)
        true_quicksort(A,l,m-1)
        true_quicksort(A,m+1,r)

def order_stat(A,i,l=0, r = None):
    if r == None:
        r = len(A)-1
    p = partition(A,i,l,r)
    x = p-l
    if x+1 == i:
        return A[p]
    elif x+1 >i:
        return order_stat(A,i,l,p=1)
    else:
        return order_stat(A,i-x-1)
        
def LCS(A,B, D =None):
    if (A,B) in D:
        return D[(A,B)]
    if D = None:
        D = {}
    if len(A) == 0 or len(B) == 0:
        return ""
    if A[0] == B[0]:
        A[0] + LCS(A[1:],B[1:])
    else:
        sol1 = LCS(A[1:],B)
        sol2= LCS(A,B[1:])
        if len(sol1) > len(sol2):
            return sol1
        else:
            return sol2

print(LCS('Antoine Assaf', 'Avant interior'))

    
        