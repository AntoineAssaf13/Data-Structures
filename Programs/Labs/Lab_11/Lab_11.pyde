class PQ:
    class Node:
        def __init__(self, ele, parent = None, left = None, right = None):
            self._data = ele
            self._p = parent
            self._l = left
            self._r = right
        
    def __init__(self):
        self._root = None
        self._size = 0
    
    def fuck_merge(self,T2):
        n1 = self._root
        n2 = T2._root
        while n2 and n1:
            if n2._data > n1._data:
                n1._l = nn
                n2 = n2._l
            
            
    def merge(self, T2):
        n1 = self._root
        n2 = T2._root
        condition = False
        if n1._data > n2._data:
            condition = True
        while n2 and n1: 
            if n2._data > n1._data:
                next = n1._l
                n1._l = n2
                n1 = next
                n2 = n2._l
            else:
                next = n2._l
                n2._l = n1
                n2 = next
                n1 = n1._l    
        if condition:
            if n1 != None:
                p = T2._root
                while p._l:
                    p = p._l
                p._l = n1
            self._root = T2._root
            T2._root = None
        else:
            if n2 != None:
                p = self._root
                while p._l:
                    p = p._l
                p._l = n2
            T2._root = None
    
    def insert(self, e):
        Temp_T = PQ()
        Temp_T._root = PQ.Node(e)
        self.merge(Temp_T)
    def extract_min(self):
        LT = PQ()
        LT._root = self._root._l
        RT = PQ()
        RT._root = self._root._r
        LT.merge(RT)
        self._root = LT._root
    def flip(self,n):
        n._l, n._r = n._r, n._l
    def flip_left(self, n = None):
            if n == None:
                n = self._root
            self.flip(n)
            if self._l:
                return self.flip_left(n = n._left)
            
            
    
            


#Just Call draw_tree on the root node and it will draw the tree
#Your node class must use ._l ._r and ._data
def subtree_size(node):
    if node is None:
      return 0
    else:
      return 1+subtree_size(node._l)+subtree_size(node._r)

def draw_tree(node,level=1,x=500,parx=None,pary=None):
    XSEP=15
    YSEP=30
    fill(0)
    textAlign(CENTER,CENTER)
    textSize(15)
    lsize=subtree_size(node._l)
    myx,myy=x+lsize*XSEP,YSEP*level
    text(str(node._data),myx,myy)
    if node._l is not None:
      draw_tree(node._l,level+1,x,myx,myy)
    if node._r is not None:
      draw_tree(node._r,level+1,x+(lsize+1)*XSEP,myx,myy)
    if parx is not None:
      strokeWeight(10)
      stroke(0,255,0,30)
      line(parx,pary,myx,myy)

def setup():
    size(1000,1000)
def draw():
    draw_tree(T1._root)
    
T1 = PQ()
T2 = PQ()
T1._root = PQ.Node(1)
T1._root._r = PQ.Node(8, T1._root)
T2._root = PQ.Node(2)
T2._root._r = PQ.Node(12, T2._root)
T2._root._l = PQ.Node(3, T2._root)
T1.merge(T2)
#T1.insert(10)