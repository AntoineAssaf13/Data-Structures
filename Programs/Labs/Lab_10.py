import random

class HT:
    def __init__(self):
        self._T = [[None for i in range (10)] for i in range (2)]
        self._len = 0
        self._r = random.random()
        self._container = 10
    def hash1(self,k):
        return hash((k,0,self._r))%len(self._T[0])
    def hash2(self,k):
        return hash((k,1,self._r))%len(self._T[1])
    def __len__(self):
        return self._len
    def __getitem__(self, k):
        bucket = self.hash1(k)
        if self._T[0][bucket][0] == k:
            return self._T[0][bucket][1]
        else:
            bucket = self.hash2(k)
            if self._T[1][bucket][0] == k:
                return self._T[1][bucket][1]
    def __setitem__(self,k,v):
        counter = 0
        while True:
            if counter == 2*self._len:
                lst = []
                for ele in self:
                    lst.append(ele)
                self._container *= 2
                self._T = [[None for i in range (self._container)] for i in range (2)]
                self._r = random.random()
                for ele in lst:
                    self.__setitem__(ele[0],ele[1])
            bucket = self.hash1(k)
            if self._T[0][bucket] == None:
                self._T[0][bucket] = (k,v)
                self._len += 1
                break
            elif self._T[0][bucket][0] == k:
                self._T[0][bucket] = (k,v)
                break
            else:
                new_val = self._T[0][bucket]
                self._T[0][bucket] = (k,v)
                k = new_val[0]
                v = new_val[1]
            bucket = self.hash2(k)
            if self._T[1][bucket] == None:
                self._T[1][bucket] =(k,v)
                self._len +=1
                break
            elif self._T[1][bucket][0] == k:
                self._T[1][bucket] = (k,v)
                break
            else:
                new_val = self._T[1][bucket]
                self._T[1][bucket] = (k,v)
                k = new_val[0]
                v = new_val[1]
            counter += 1
            
    def __delitem__(self,k):
        h = self.hash1(k)
        if self._T[0][h] and self._T[0][h][0] == k:
            self._T[0][h] = None
        h = self.hash2(k)
        if self._T[1][h] and self._T[1][h][0] == k:
            self._T[1][h] = None
        self._len -= 1
                
    def __iter__(self):
        for tup in self._T[0]:
            if tup != None:
                yield tup
        for tup2 in self._T[1]:
            if tup2 != None:
                yield tup2
                
    def items(self):
        lst = []
        for tup in self._T[0]:
            if tup != None:
                lst.append(tup)
        for tup2 in self._T[1]:
            if tup2 != None:
                lst.append(tup2)
        return lst
    
    def values(self):
        lst = []
        for tup in self._T[0]:
            if tup != None:
                lst.append(tup[1])
        for tup2 in self._T[1]:
            if tup2 != None:
                lst.append(tup2[1])
        return lst
    
    def keys(self):
        lst = []
        for tup in self._T[0]:
            if tup != None:
                lst.append(tup[0])
        for tup2 in self._T[1]:
            if tup2 != None:
                lst.append(tup2[0])
        return lst
        
    def __contains__(self, k):
        h = self.hash1(k)
        if self._T[0][h] and self._T[0][h][0] == k:
            return True
        h = self.hash2(k)
        if self._T[0][h] and self._T[1][h][0] == k:
            return True
        
    
        
    
                
                    
                    
            
        
    
        

T=HT()

for i in range(200):
    T[i]=i*i
for i in T.keys():
    T[i]=T[i]+1
for i in range(5,400):
    if i in T:
        del T[i]
K=list(T.items())
K.sort()
print(K)
print(len(K))
