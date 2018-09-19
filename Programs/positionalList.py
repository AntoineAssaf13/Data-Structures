class PositionalList:
    class Node:
        __slots__ = ('_prev','_next','_data') #Saves space and stores data
        def __init__(self, prev, data, nxt): #This is what Node looks like
            self._prev = prev
            self._next = nxt
            self._data = data
    class Position:
        def __init__(self, node, lst):
            self._node = node
            self._list = lst
        def element(self):
            return self._node._data
            
    def __init__(self):
        self._len = 0
        self._head = self.Node(None, None, None)
        self._tail = self.Node(self._head,None,None)
        self._head._next = self._tail #So now we have the empty list [X,X,Head]<->[Tail,X,X]
    
    def _add_between(self, ln, rn, x): #Take the left and right node to know where to add between
        nn = self.Node(ln,x,rn) #create new node
        ln._next = nn
        rn._prev = nn
        
    def add_first(self,x): #Add after first element of list
        self._add_between(self._head,self._head._next,x)
    def add_last(self,x): #Add after last element of list
        self._add_between(self._tail, self._tail._prev,x)
    def add_before(self, p, x):
        self._add_between(p._node._prev, p._node, x)
    def add_after(self, p, x):
        self._add_between(p._node, p._node._next, x)
    def delete(self, p): #Define everything you want to change, give it a name
        rn = p._node._next
        ln = p._node._prev
        mn = p._node
        ln._next = rn
        rn.prev = ln
        mn._next = None
        mn._prev = None #the node's arrows has been moved to None isolated, while the ln and rn are now connected
        p._node = rn
    def replace(self, p, x):
        p._node._data = x
    def first(self):
        return self.Position(self._head._next,self)
    def after(self, p):
        np = self.Position(p._node._next, self) #Create the new position
        if np._node == self._tail:
            return None
        else:
            return np
    def before(self, p):
        np = self.Position(p._node._prev, self) #Create the new position
        if np._node == self._head:
            return None
        else:
            return np
    def __iter__(self):
        p = self.first()
        while p:
            yield (p.element())
            p = self.after(p)
            
    