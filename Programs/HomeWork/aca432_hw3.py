'''
Name: Antoine Assaf
netID: aca432
Homework 3
'''

import ctypes

class aList:

  def __init__(self, s = None):
    """Create an empty array."""
    self._n = 0                                    
    self._capacity = 1                             
    self._A = self._make_array(self._capacity)     
    if s != None:
        for j in s:
            self.append(j)

  def __iter__(self):
      for i in range(len(self)):
          yield self._A[i]
    
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    if isinstance(k,slice):
      A=aList()
      for j in range(*k.indices(self._n)):               
          A.append(self._A[j])
      return A
    if k < 0:
      k = self._n+k
    if not 0 <= k < self._n:
      k = k%self._n
    return self._A[k]                             

  def __delitem__(self,i):
      if isinstance(i,slice):
          for j in reversed(range(*i.indices(self._n))):               
              del self[j]
      else:
          if i<0:
              i=self._n+i
          for j in range(i,self._n-1):
              self._A[j]=self._A[j+1]
          self[-1]=None        
          self._n-=1      
      
  def __setitem__(self,i,x):
      if i<0:
          i=self._n+i
      self._A[i]=x  

  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                 
      self._resize(2 * self._capacity)             
    self._A[self._n] = obj
    self._n += 1
    
  def __add__(self,B):
      R = aList()
      if self._n >= len(B):
          for i in range(self._n):
              try:
                  if B[i] == None or i > (len(B)-1):
                      R.append(self._A[i])
                  else:  
                      R.append(self._A[i]+B[i])
              except IndexError:
                  R.append(self._A[i])
      else:
          for i in range(len(B)):
              try:
                  if self._A[i] == None or i > self._n:
                      R.append(B[i])
                  else:  
                      R.append(self._A[i]+B[i])
              except IndexError:
                  R.append(B[i])
      return R
     
  def __iadd__(self,B):
      return (self+B)
      
      
  def __sub__(self, B):
      R = aList()
      if self._n >= len(B):
          for i in range(self._n):
              try:
                  if B[i] == None or i > (len(B)-1):
                      R.append(self._A[i])
                  else:  
                      R.append(self._A[i]-B[i])
              except IndexError:
                  R.append(self._A[i])
      else:
          for i in range(len(B)):
              try:
                  if self._A[i] == None or i > self._n:
                      R.append(B[i])
                  else:  
                      R.append(self._A[i]-B[i])
              except IndexError:
                  R.append(B[i])
      return R
      
  def __isub__(self,B):
      return (self-B)
      
  def __mul__(self, i):
          R = aList()
          for ele in self._A:
              for j in range (i):
                  R.append(ele)
          return R
          
  def __imul__(self,B):
      return (self*B)

  def __rmul__(self,i):
      R = aList()
      for ele in self._A:
          R.append(ele*i)
      return R
      
  def _resize(self, c):                            
    """Resize internal array to capacity c."""
    B = self._make_array(c)                       
    for k in range(self._n):                       
      B[k] = self._A[k]
    self._A = B                                   
    self._capacity = c

  def _make_array(self, c):                        
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()              

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""

    if self._n == self._capacity:                  
      self._resize(2 * self._capacity)            
    for j in range(self._n, k, -1):               
      self._A[j] = self._A[j-1]
    self._A[k] = value                             
    self._n += 1
      
  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    for k in range(self._n):
      if self._A[k] == value:              
        for j in range(k, self._n - 1):    
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        
        self._n -= 1                       
        return                             
    raise ValueError('value not found')    
    
  def __contains__(self,x):
      for y in self._A:
          if x==y:
              return True
          return False
          
  def is_empty(self):
      if self._n == 0:
          return True
      else:
          return False
    
  def __str__(self):
      s = '['
      for i in range(self._n):
          if i != self._n - 1:
              s+=str(self._A[i]) + ','
          else:
              s+= str(self._A[i])
      s+= ']'
      return s
    
  def count(self,x):
      c=0
      for y in self._A:
          if x==y:
              c+=1
      return c
      
  def index(self,x):
      for i in range(self._n):
          if self._A[i]==x:
              return i
      return None

  def select(self, t):
      R = aList()
      for j in range(self._n):
          if j in t:
              R.append(self._A[j])
      return R
      
      #Itterate backwards
  def revitr(self): 
      for i in range(len(self)):
          yield self._A[-i-1]
          
#-TEST CODE-#
#lst = aList([5,6,7,8])
#lst3 = aList((1,3,5,7,8,9))
#for i in lst.revitr():
#    print (i)
#print(lst)
#print(lst.select([0,2]))
#print(iter(lst))
##lst3.remove(3)
#
#del lst[0:2]
#print(len(lst))
#print(len(lst3))
#print(lst3-lst)
#s = 'abcdefghij'
#lst2 = aList(s)
#print(lst2[522])
#print(len(lst))
#print(lst)
#print(lst.is_empty())
#print(lst[-1])
#print(lst.__getitem__(0))
