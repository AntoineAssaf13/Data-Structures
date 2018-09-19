  #--------------#
  #Initial Method#
  #--------------#

def prefix_average(A):
    R = []
    for i in range (len(A)): #N Times
        S = 0
        S = sum(A[:i+1]) #0(1)#
        avg = S/(i+1) #0(1)#
        R.append(avg) #0(1)# ---> < N^2 Because nested loop so you can have it N * N times
    return R
    
    #----------#
    #Correction#
    #----------#

def prefix_average2(A):
    sums = []
    for x in A: # N Times
        sums.append(x +(sums[-1] if len(sums) > 0 else 0)) #0(1)
    return [(sums[i])/(i + 1) for i in range (len(sums))] #*N
    

    
    
    
print(prefix_average2([1,2,3,4,5]))

    
    

