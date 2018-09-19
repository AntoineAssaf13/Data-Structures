#Tree

class BinaryTree:
    #Node and position classes come first
    class Node:
        def __init__(self, left, right, parent, data):
            self._left = left
            self._right = right
            self._parent = parent
            self._data = data
    class Position:
        def __init__(self, node, tree):
            self._tree = tree
            self._node = node
        def element(self):
            return self._node._data
    #Now for the actual Tree functions
    def __init__(self):
        self._size = 0
        self._root = None
    def isempty(self):
        return self._size == 0 
    def root(self):
        return self.Position(self._root, self)
    def left(self, p):
        return self.Position(p._node._left, self)
    def right(self, p):
        return self.Position(p._node._right, self)
    def parent(self, p):
        return self.Position(p._node._parent, self)
    def sibling(self, p):
        if p == self.left(self.parent(p)):
            return self.right(self.parent(p)) #Checks if you are the right child of your parent
        else:
            return self.left(self.parent(p))
    def children(self, p):
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)
    def add_root(self,d):
        if self.is_empty():
            self._root = self.Node(None,None,None, d)
            self._size = 1
            return self.Position(self._root, self)
        else:
            raise ValueError ('Root already exists')
    def add_left(self, p, d):
        if p._node._left:
            raise ValueError ('Already has a left child')
        else:
            p._node._left = self.Node(None,None,p._node, d)
            self._size += 1
            return self.Position(p._node._left, self)
    def add_right(self, p, d):
        if p._node._right:
            raise ValueError ('Already has a right child')
        else:
            p._node._right = self.Node(None,None,p._node, d)
            self._size += 1
            return self.Position(p._node._right, self)
    def delete(self, p):
        if self.num_children(p) == 2: #need to code num_children
            raise ValueError('Cannot have more than one child to delete')
        else:
            par = self.parent(p)
            if p == self.right(par):
                if self.is_leaf(p):
                    par._node._right = None
                else:
                    if p._node._right:
                        par._node._right = p._node._right
                        p._node._right.par = par._node
                    else:
                        par._node._right = p._node._left
                        p._node._left.par = par._node
                p._node = None
                self._size -= 1
                #CODE FOR LEFT CHILD DELETION
    def attach(self, p, T1, T2):
        if not self.is_leaf(p):
            raise ValueError ('Position needs to refer to leaf')
        else:
            p._node._left = T1._root
            p._node._right = T2.root
            T1._root._par = T2._root._par = p._node
            T1._root = T2._root = None
            self._size += T1._size + T2._size
            T1._size = T2._size = 0
    def f (self, p):
        yield p.element()
        l = self.left(p)
        r = self.right(p)
        if l:
            yield from self.f(l)
        if r:
            yield from self.f(r)
            