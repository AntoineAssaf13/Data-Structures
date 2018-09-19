def repetitions(A):
    for a in range(len(A)):
        for b in range(a): #check index before a, a never 0 because b is
            if A[a] == A[b]:
                return True
    return False
    
print(repetitions([1,2,3,4,5,6]))
