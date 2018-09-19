class hashDict:

    def __init__(self):
        self._T = [[] for i in range (10)]
        
    def __setitem__(self,k,v):
        bucket = hash(k)%len(self._T)
        for i in  range (len(self._T[bucket])):
            if self._T[bucket][i][0] == k:
                self._T[bucket][i] = (k,v)
                return
        self._T[bucket].append((k,v))
        
    def __getitem__(self,k):
        bucket = self.T[hash(k)%len(self._T)]
        for k2,v2 in bucket:
            if k == k2:
                return v2
    def __delitem__(self,k):
        bucket = self.T[hash(k)%len(self._T)]
        for i in range(len(bucket)):
            if k == bucket[i][0]:
                del bucket[i]
                return
    
    def __iter__(self):
        for bucket in self._T:
            for k,v in bucket:
                yield k