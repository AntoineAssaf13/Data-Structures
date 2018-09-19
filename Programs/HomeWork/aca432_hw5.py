"""
Antoine Assaf - aca432
CS 1134
Homework 5
"""
#The list prints out in reverse order, however on Piazza, Prof. said this wasn
class LeakyStack:
    class Node:
        def __init__(self,nxt,data,prev):
            self._nxt = nxt
            self._data = data
            self._prev = prev
    def __init__(self, maxsize):
        self._maxsize = maxsize
        self._len = 0
        self.top = self.Node(None, None, None)
        self.back = self.Node(None, None, self.top)
    def __len__(self):
        return self._len
    def is_empty(self):
        return self._len == None
    def push(self, x):
        if self._len == 0:
            self._len += 1
            self.top = self.Node(self.top,x,None)
            self.back = self.top
        elif self._len < self._maxsize:
            self._len += 1
            self.top = self.Node(self.top,x,self.top._nxt)
            self.top._nxt._prev = self.top
            self.back = self.Node(self.back._prev,x, self.back)
        else:
            self.back = self.back._prev
            self.back._prev._nxt = self.back
            self.top = self.Node(self.top,x,self.top._nxt)           
    def pop(self):
        r = self.top._data
        self.top = self.top._nxt
        self._len -= 1
        return r
    def __str__(self):
        n = self.top
        s = '['
        for i in range(self._len):
            if i < self._len-1:
                s+=str(n._data) + ','
                n = n._nxt
            else:
                s+=str(n._data) +']'
        return s

#Test code
lst1 = LeakyStack(5)
lst1.push(1)
lst1.push(2)
lst1.push(3)
lst1.push(4)
lst1.push(5)
print(len(lst1))
print(lst1)
lst1.push(6)
print(lst1)
lst1.push(7)
print(lst1)
lst1.push(8)
print(lst1)
print(lst1.pop())
print(lst1)
print(len(lst1))
lst1.push(8)
print(lst1)