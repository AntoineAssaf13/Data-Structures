"""
Antoine Assaf - aca432
CS 1134
Homework 2
"""

#Problem 1:
''' This function runs an n amount of times depending on the length of the sequence.'''
def find_minmax(seq):
    if len(seq) == 1:
        return seq[0], seq[0]
    else:
        a, b = find_minmax(seq[1:])
        if a > seq[0]:
            if b < seq[0]:
                return a, b
            else:
                return a, seq[0]
        else:
            if b < seq[0]:
                return seq[0], b
            else:
                return seq[0], seq[0]

result = find_minmax([3,4,5,6,7,2,99,1])
print('The minimum value of this sequence is', result[1], 'and the maximum is', result[0])

#Problem 2:
def log(n):
    if n <= 1:
        return 0
    else:
        answer = 1 + log(n/2)
        return answer
        
print(log(16))


#Problem 3:
def is_unique(lst):
    if len(lst) == 0:
        return True
    else:
        if lst[0] in lst[1:]:
            return False
        else:
            return is_unique(lst[1:])
print(is_unique([9,2,3,4,5,9]))

#Problem 4:
def subsets(n):
    if len(n) == 0:
        return [[]]
    sub = []
    sub_temp = subsets(n[1:])
    for i in sub_temp:
        sub.append(i[:])
    for ele in sub_temp:
        ele.append(n[0])
    sub.extend(sub_temp)
    return sub

print(subsets([1,2,3]))

#Problem 5
def palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False

print(palindrome('laval'))

#Problem 6
def arrange(lst, k, i = 0):
        if len(lst) == i:
            return []
        new = arrange(lst, k, i+1)
        if lst[i] <= k:
            new.insert(0,lst[i])
        elif lst[i] > k:
            new.append(lst[i])
        return new

print(arrange([9,8,7,6,4,3,2,1], 5))