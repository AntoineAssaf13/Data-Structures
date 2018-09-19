import random

class BST:
    class _Position:
        def __init__(self, node, bst):
            self._bst = bst
            self._node = node
        def element(self):
            return self._node._data
    class _Node:
        def __init__(self,parent,left,right,data):
            self._left=left
            self._right=right
            self._parent=parent
            self._data=data
            if self._parent:
                self._depth = self._parent._depth + 1
            else:
                self._depth = 0
    def __init__(self):
        self._root=None
        self._len = 0
    def _make_position(self,node):
        return BST._Position(node,self)
    def insert(self,x):
        if self._root == None:
            self._root=BST._Node(None,None,None,x)
        else:
            self._rec_insert(self._root,x)
        self._len += 1
    def _rec_insert(self,n,x):
        if x<n._data:
            if n._left == None:
                n._left=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._left,x)
        else:
            if n._right == None:
                n._right=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._right,x)
    def search_le(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_le(self._root,x)
    def _rec_search_le(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_search_le(n._right,x)
                if rv:
                    return rv
                else:
                    return n._data
            else:
                return n._data
#Question 1              
    def __iter__(self, n = None):
        if n == None:
            n = self._root
        if n._left:
            for ele in self.__iter__(n._left):
                yield ele
        yield n._data
        if n._right:
            for ele in self.__iter__(n._right):
                yield ele
#Question 2
    def search_ge(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_ge(self._root,x)
    def _rec_search_ge(self,n,x):
        if x>n._data:
            if n._right:
                return self._rec_search_ge(n._right,x)
            else:
                return None
        else:
            if n._left:
                rv=self._rec_search_ge(n._left,x)
                if rv:
                    return rv
                else:
                    return n._data
            else:
                return n._data
#Question 3
    def __len__(self):
        return self._len
#Question 4:
    def _print_out_helper(self, n):
        if n._left:
            for node in self._print_out_helper(n._left):
                yield node
        yield n
        if n._right:
            for node in self._print_out_helper(n._right):
                yield node
    
    def print(self):
        height = self._root._depth
        for ele in self._print_out_helper(self._root):
            if ele._depth > height:
                height = ele._depth
        height += 1
        branches = [[str(x) for x in self] for i in range (height)]
        counter = 0
        for ele in self._print_out_helper(self._root):
            for j in range(height):
                if j != ele._depth:
                    branches[j][counter] = " "*len(str(ele._data))
            counter +=1
        for ele in range(len(branches)):
            branches[ele] = " ".join(branches[ele])
        print('\n'.join(branches))
            

#Question 5:
    def last(self):
        p = BST._Position(self._root, self)._node
        while p._right:
            p = p._right
        return self._make_position(p)
    def first(self):
        p = BST._Position(self._root, self)._node
        while p._left:
            p = p._left
        return self._make_position(p)
    def after(self, p): #Assuming they are ints, I asked about this and was told it was ok.
        new_p = self.pos_ge(p.element()+1)
        return new_p
    def before(self, p):
        new_p = self.pos_le(p.element()-1)
        return new_p
#Question 6:
    def pos_ge(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_pos_ge(self._root,x)
    def _rec_pos_ge(self,n,x):
        if x>n._data:
            if n._right:
                return self._rec_pos_ge(n._right,x)
            else:
                return None
        else:
            if n._left:
                rv=self._rec_pos_ge(n._left,x)
                if rv:
                    return rv
                else:
                    return self._make_position(n)
            else:
                return self._make_position(n)
                
    def pos_le(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_pos_le(self._root,x)
    def _rec_pos_le(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_pos_le(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_pos_le(n._right,x)
                if rv:
                    return rv
                else:
                    return self._make_position(n)
            else:
                return self._make_position(n)

#Question 7:
    def range(self,x,y):
        for ele in self:
            if ele >= x and ele < y:
                yield ele
    def pos_range(self,x,y):
        small = self.pos_le(x)
        big = self.pos_ge(y)
        t = small
        while t and t.element() < big.element():
            yield t
            t = self.after(t)
#Question 8: On soyder since the window isn't large it might look distorted but it shouldn't be, pycharm will prove this.
def qu8(T, n = 32, d=16, l = False):
    if l:
        return
    new_l = (d==0)
    T.insert(n)
    qu8(T, n-d, d//2, new_l)
    qu8(T, n+d, d//2, new_l)
    
T8 = BST()
qu8(T8, 32,16)
T8.print()
print('------------------------------------------------------------------------------')
    

#Question 9
T9 = BST()
for i in range(10):
    T9.insert(i)
    T9.insert(20-i)
T9.print()
        
        



T=BST()
#L=list(range(10,100,10))
#random.shuffle(L)
L = [50,40,70,20,30,10,60,90,80]
for i in L:
    T.insert(i)
for ele in T:
    print(ele)
print('----------------------------------------------')
for i in range(5,105,5):
    print(T.search_le(i))
print('----------------------------------------------')
for i in range(5,105,5):
    print(T.search_ge(i))
print('----------------------------------------------')
print(T.search_ge(45))
print(T.search_le(45))
print(len(T))
T.print()
print(T.first().element())
print(T.last().element())
print(T.after(T.first()).element())
print(T.before(T.before(T.last())).element())
print([ele for ele in T.range(20,70)])
print([p.element() for p in T.pos_range(20,70)])