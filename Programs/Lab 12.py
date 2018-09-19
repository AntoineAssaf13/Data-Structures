import random
def sortselect(A,k):
    if len(A) <= 5:
        A.sort()
        return A[k]
    groups5 = []
    index = 0
    medianlist = []
    for i in range(len(A)//5):
        e = A[index:index+5]
        e.sort()
        groups5.append(e)
        index+=5
    if A[index:]:
        e = A[index:]
        e.sort()
    groups5.append(e)
    for ele in groups5:
        if len(ele) == 5:
            medianlist.append(ele[2])
        else:
            medianlist.append(ele[len(ele)//2])
    MoM = sortselect(medianlist,len(medianlist)//2)
    small_l = []
    large_l = []
    for ele in A:
        if ele < MoM:
            small_l.append(ele)
        elif ele > MoM:
            large_l.append(ele)
    if len(small_l) == k:
        return MoM
    if len(small_l) < k:
        return sortselect(large_l,k-1-len(small_l))
    else:
        return sortselect(small_l,k)


A=list(range(222))
random.shuffle(A)
print([sortselect(A,i) for i in range(222)])

