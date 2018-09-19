class HeapPQ:
    class _Item:
        def __init__(self, k, v):
            self._k = k
            self._v = v
            
    def __init__(self, I = None):
        self._A = []
        if I:
            for k,v in I:
                self.add(k,v)
        
    def __len__(self):
        return len(self._A)
        
    def add(self,k,v):
        self._A.append(self._Item(k,v))
        self._bubble_up(len(self._A)-1)
        
    def _bubble_up(self, i):
        if i == 0:
            return
        elif self._A[i]._k < self._A[self._parent(i)]._k:
            self._swap(i, self._parent(i))
            self._bubble_up(self._parent(i))
    def min(self):
        return(self._A[0]._key, self._A[0]._v)
    
    def remove_min(self):
        rv = self.min()
        self._A[0] = self._A.pop()
        self.bubble_down(0)
        return rv
    def _bubble_down(self, i):
        l = self._left(i)
        r = self._right(i)
        smallest = i
        if self._valid(l) and self._A[l]._k < self._A[smallest]._k:
            smallest = l
        if self._valid(r) and self._A[r]._k < self._A[smallest]._k:
            smallest = r
        if i != smallest:
            self._swap(i, smallest)
            self._bubble_down(smallest)
    def _valid(self, i):
        return i < len(self._A)
    def _swap(self, i, j):
        self._A[i], self._A[j] = self._A[j], self._A[i]
        
    def _left(self, i):
        return self._A[(2*i)+1]
    def _right(self, i):
        return self._A[(2*1)+2]
    def _parent(self, i):
        return self._A[(i-1)//2]
        

