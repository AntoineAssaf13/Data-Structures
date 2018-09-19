"""
Antoine Assaf - aca432
CS 1134
Homework 1
"""
#Question 1:
''' O(n), O(n), O(n^2), O(n), O(n^3) '''

#Question 2:
def merge(i1, i2):
    lst = []
    if len(i1) >= len(i2):
        max_len = len(i1)
    else:
        max_len = len(i2)
    
    for i in range (max_len):
        try:
            lst.append(i1[i])
            lst.append(i2[i])
        except IndexError:
            if i > (len(i1)-1):
                lst.append(i2[i])
    return lst

print([i for i in merge(range(5),range(100,105))])    
print([i for i in merge( range(5),range(100,101))])
print([i for i in merge( range(1),range(100,105))])

#Question 3:
class Polynomial:
    def __init__(self, a):
        lst = []
        for ele in a:
            lst.append(ele)
        self._vals = lst
        self._expo = (len(self._vals) - 1)
    def evaluate (self, x):
        curr_expo = self._expo
        num = 0
        for ele in self._vals:
            num += ele * (x ** curr_expo)
            curr_expo -= 1
        return num
    def __str__(self):
        curr_expo = self._expo
        string = ''
        for ele in self._vals:
            if curr_expo != 0:
                string += str(ele) + 'x^' + str(curr_expo) + '+'
            else:
                string += str(ele)
            
            curr_expo -= 1
        return string

P=Polynomial((6,2,1,8))
print(str(P))
print([P.evaluate(i) for i in range(10)])

#Question 4
def f(n):
    return 1/pow(2,n)

def sigma(func,a,b):
    answer = 0
    for i in range (a, b + 1):
        answer += func(i)
    return answer

print(sigma(f,2,10))
        
            
            
            
        
            
        
            

