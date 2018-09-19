#-----------------------TREE CLASS--------------------------
import math

class Tree:

    #------------------------------- nested Position class -------------------

    class Position:

        """An abstraction representing the location of a single element within a tree.

        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)            # opposite of __eq__

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return self.root()== None

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):                 # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):                  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)        # start _height2 recursion

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():                        # use same order as positions()
            # but yield each element
            yield p.element()

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()                            # return entire preorder iteration

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start recursion
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                           # visit p before its subtrees
        for c in self.children(p):                        # for each child c
            # do preorder of c's subtree
            for other in self._subtree_preorder(c):
                # yielding each to our caller
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):                        # for each child c
            # do postorder of c's subtree
            for other in self._subtree_postorder(c):
                # yielding each to our caller
                yield other
        # visit p after its subtrees
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            # known positions not yet yielded
            fringe = LinkedQueue()
            fringe.enqueue(self.root())        # starting with the root
            while not fringe.is_empty():
                # remove from front of the queue
                p = fringe.dequeue()
                yield p                          # report this position
                for c in self.children(p):
                    # add children to back of queue
                    fringe.enqueue(c)

    #-------------------------- nested _Node class --------------------------
    class _Node:

        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right'  # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    #------------------------------- utility methods -------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #-------------------------- binary tree constructor ----------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None

    #-------------------------- public accessors --------------------------
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count

    def sibling(self, p):
        """Return a Position representing p s sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    #-------------------------- nonpublic mutators --------------------------

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left = self._Node(e, node)                  # node is its parent
        return self._make_position(node._left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right = self._Node(e, node)                 # node is its parent
        return self._make_position(node._right)

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent   # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        node._parent = node              # convention for deprecated node
        return node._element

    def attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        # all 3 trees must be same type
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        if not t1.is_empty():         # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
        if not t2.is_empty():         # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty

#-------------------ADD METHODS HERE-------------------
            
    def Max(self, p = None, high = None):
        if p == None:
            p = self.root()
        curr = p.element()
        if high == None or curr > high:
            high = curr
        if self.is_leaf(p):
            return high
        else:
            if self.right(p) != None:
                high = self.Max(p = self.right(p), high = high)
            if self.left(p) != None:
                high = self.Max(p = self.left(p), high = high)
            return high
        
    def leaves_list(self, p = None, lst = []):
        if p == None:
            p = self.root()
        if self.is_leaf(p):
            lst.append(p.element())
            return
        else:
            self.leaves_list(p = self.left(p), lst = lst)
            self.leaves_list(p = self.right(p), lst = lst)
        return lst
    
    def balancedTree_helper(self, p):
        if p == None:
            return 0
        if self.is_leaf(p):
            return 1
        else:
            left = self.balancedTree_helper(self.left(p))
            right = self.balancedTree_helper(self.right(p))
            if right >= left:
                return 1 + self.balancedTree_helper(self.right(p))
            elif left > right:
                return 1+ self.balancedTree_helper(self.left(p))
            
    def balancedTree(self, p = None):
        if p == None:
            p = self.root()
        if self.is_leaf(p):
            return True
        b = math.fabs(self.balancedTree_helper(self.right(p)) - self.balancedTree_helper(p)) <= 1
        self.balancedTree(self.left(p))
        self.balancedTree(self.right(p))
        return b
    
    def iterative_inorder(self):
        p = self.root()
        n = None
        parent = None
        while p != None:
            if parent == self.parent(p):
                if self.is_leaf(p):
                    yield p.element()
                    n = self.parent(p)
                elif self.left(p) != None:
                    n = self.left(p)
                elif self.right(p) != None:
                    n = self.right(p)
            elif parent == self.left(p):
                yield p.element()
                if self.right(p) != None:
                    n = self.right(p)
            else:
                n = self.parent(p)
            parent = p
            p = n
            
def create_expression_tree(prefix_exp_str, n = None):
    if n == None:
        return create_expression_tree(prefix_exp_str.split(), 0)[0]
    T = Tree()
    if n >= len(prefix_exp_str):
        return(T, n)
    if prefix_exp_str[n].isnumeric():
        T.add_root(int(prefix_exp_str[n]))
        return(T, n+1)
    T.add_root(prefix_exp_str[n])
    LT, end = create_expression_tree(prefix_exp_str, n+1)
    RT, end = create_expression_tree(prefix_exp_str, end)
    T.attach(T.root(), LT, RT)
    return(T, end)


def prefix_to_postfix(prefix_exp_str, T = None ,p = None, lst = []):
    if T == None:
        T = create_expression_tree(prefix_exp_str)
        p = T.root()
    if isinstance(p.element(), int):
        lst.append(str(p.element()))
        return
    if T.left(p):
        prefix_to_postfix(prefix_exp_str,T, T.left(p), lst)
    if T.right(p):
        prefix_to_postfix(prefix_exp_str, T, T.right(p), lst)
    lst.append(p.element())
    return lst

#Not sure if this is linear but I thought it to be more efficient than using the same style than question 
#Also I have NO clue how to return this in a non list form.  Please Duc. Be nice.
                    
            
#TEST FUNCTIONS


def balancedTree(n, start=0):
    T = Tree()
    if start < n:
        mid = (n + start) // 2
        T.attach(T.add_root(mid), balancedTree(mid, start), balancedTree(n, mid + 1))
    return T

def levelTree(n, start = 0):
    T1 = Tree()
    if start < n:
        T1.attach(T1.add_root(n), levelTree(n-1, start), levelTree(n-1, start))
    return T1
    
T1 = balancedTree(15)
T2 = levelTree(5)
print(T1.Max())
print(T2.Max())
print(T1.leaves_list())
print(T1.balancedTree())
ET = create_expression_tree('* 2 + - 15 6 4')
print(prefix_to_postfix('* 2 + - 15 6 4'))
for item in T1.iterative_inorder():
    print(item, end=' ')
    print()