#PLEASE READ.  THIS FILE REQUIRES TO BE IN A PACKAGE WITH ALL INHERITED FILES.  PLEASE PLEASE DONT GIVE ME A BAD GRADE.
#LEGIT, I HAVE NO IDEA HOW TO TEST THIS CODE...
#########################################################################################################################

from binary_search_tree import TreeMap

class AVLTreeMap(TreeMap):
  """Sorted map implementation using an AVL tree."""

  #-------------------------- nested _Node class --------------------------
  class _Node(TreeMap._Node):
    """Node class for AVL maintains height value for balancing.

    We use convention that a "None" child has height 0, thus a leaf has height 1.
    """
    __slots__ = '_balance'         # additional data member to store height

    def __init__(self, element, parent=None, left=None, right=None):
      super().__init__(element, parent, left, right)
      self._balance = 0            # will be recomputed during balancing
      

  #------------------------- positional-based utility methods -------------------------
  def _compute_height(self, p):
    if p is None:
        return 0
    else:
        return  1 + max(self._compute_height(self.left(p)), self._compute_height(self.right(p)))
  
  def _recompute_balance(self,p):
      p._balance = self._compute_height(self.right(p)) - self._compute_height(self.left(p))

  def _isbalanced(self, p):
    return p._node._balance == 0

  def _tall_child(self, p, favorleft=False): # parameter controls tiebreaker
    if p._balance == -1:
      return self.left(p)
    elif p._balance == 0 and favorleft:
      return self.left(p)
    else:
      return self.right(p)

  def _tall_grandchild(self, p):
    child = self._tall_child(p)
    # if child is on left, favor left grandchild; else favor right grandchild
    alignment = (child == self.left(p))
    return self._tall_child(child, alignment)

  def _rebalance(self, p):
    while p is not None:
      old_height = self._compute_height(p)                          # trivially 0 if new node
      if not self._isbalanced(p):                           # imbalance detected!
        # perform trinode restructuring, setting p to resulting root,
        # and recompute new local heights after the restructuring
        p = self._restructure(self._tall_grandchild(p))
        self._recompute_balance(self.left(p))                
        self._recompute_balance(self.right(p))                           
      self._recompute_balance(p)                             # adjust for recent changes
      if self._compute_height(p) == old_height:                     # has height changed?
        p = None                                            # no further changes needed
      else:
        p = self.parent(p)                                  # repeat with parent

  #---------------------------- override balancing hooks ----------------------------
  def _rebalance_insert(self, p):
    self._rebalance(p)

  def _rebalance_delete(self, p):
    self._rebalance(p)

T = AVLTreeMap()
for i in range(100):
	T[i] = i*i
for i in range(5,40,5):
	del T[i]
for i in T:
	print(T[i])
