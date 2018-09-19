import timeit
class PList:
    class _Node:
        __slots__='_data','_prev','_next'
        def __init__(self,data,prev,next):
            self._data=data
            self._prev=prev
            self._next=next
    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    def __init__(self):
        self._head=self._Node(None,None,None)
        self._head._next=self._tail=self._Node(None,self._head,None)
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node._next)
        node._next._prev=newNode
        node._next=newNode
        self._size+=1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail._prev)
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node._prev)
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node._prev._next=node._next
        node._next._prev=node._prev
        node._prev=node._next=node._data=None
        self._size-=1
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        while pos:
            yield pos.data()
            pos=self.before(pos)

            
class Counters:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
#################################            
    class Counter:
        def __init__(self,position,counters, outer):
            self._outerCounter = outer
            self._counters = counters
            self._position=position
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count            
    def __init__(self):
        self._L=PList()
    def _validate(self,counter):
        if counter._outerCounter is not self:
            raise ValueError('counter does not belong to this Counter')
#########################################################################
    def new_counter(self,name):
        if len(self._L) == 0 or self._L.last().data().last().data()._count != 0:
            self._L.add_last(PList())
        self._L.last().data().add_last(Counters._Item(name))
        return Counters.Counter(self._L.last().data().last(),self._L.last(),self)
#########################################################
    def delete_counter(self,counter):
        self._validate(counter)
        counter._counters.data().delete(counter._position)
        if len(counter._counters.data())==0:
            self._L.delete(counter._counters)
        counter._position = None
        counter._counters = None
        counter._outerCounter = None
########################################################
    def increment_counter(self,counter):
        self._validate(counter)
        count = counter._counters.data().delete(counter._position)
        count._count += 1
        previous_plist = self._L.before(counter._counters)
        if len(counter._counters.data()) == 0:
            self._L.delete(counter._counters)
        if previous_plist is None:
            self._L.add_first(PList())
            counter._position = self._L.first().data().add_last(count)
            counter._counters = self._L.first()
        elif previous_plist.data().last().data()._count == count._count:
            counter._position = previous_plist.data().add_last(count)
            counter._counters = previous_plist
        else:
            counter._counters = self._L.add_after(previous_plist, PList())
            counter._position = counter._counters.data().add_last(count)
    def __iter__(self):
        counters = self._L.first()
        while counters:
            counter = counters.data().first()
            while counter:
                yield Counters.Counter(counter, counters, self) #I'm sorry
                counter = counters.data().after(counter)
            counters = self._L.after(counters)
#Old Counters
class Old_Counters:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
    class Counter:
        def __init__(self,position,counter):
            self._position=position
            self._counter = counter
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count   
    def _validate(self, counter):
        if counter._counter is not self:
            raise ValueError ('Counter does not belong to Counters')
    def __init__(self):
        self._L=PList()
    def new_counter(self,name):
        self._L.add_last(Counters._Item(name))
        return Old_Counters.Counter(self._L.last(), self)
    def delete_counter(self,counter):
        self._validate(counter)
        self._L.delete(counter._position)
        counter._position=None
    def increment_counter(self,counter):
        self._validate(counter)
        counter._position.data()._count+=1
        before_position=self._L.before(counter._position)
        while (before_position and 
              before_position.data()._count
              < counter.count()):
            new_position=self._L.add_before(before_position,counter._position.data())
            self._L.delete(counter._position)
            counter._position=new_position
            before_position=self._L.before(counter._position)
    def __iter__(self):
        position=self._L.first()
        while position:
            yield Old_Counters.Counter(position,self)
            position=self._L.after(position)
#C=Counters()           
#D=Counters()
#cc=C.new_counter("A counter in C")
#D.increment_counter(cc)
D=Counters()
names=("John","Guruprasad","Jason","Duc","Eric","Xinran","Kent","Leon","Ian")
counters=[D.new_counter(name) for name in names]

for i in range(100):
    for cp in counters:
        D.increment_counter(cp) 
for i in range(len(counters)):
    for j in range(i):
        D.increment_counter(counters[i])
D.delete_counter(counters[3])
for d in D:
    print(d.name(),d.count())
    
def old():
    C=Counters()
    names=("John"*100)
    counters=[C.new_counter(name) for name in names]
    for i in range(1000):
        for cp in counters:
            C.increment_counter(cp) 
        
def new():
    C=Counters()
    names=("John"*100)
    counters=[C.new_counter(name) for name in names]
    for i in range(1000):
        for cp in counters:
            C.increment_counter(cp) 
        


    
print('NEW:')
print(timeit.Timer('new()', 'from __main__ import new').timeit(1))
print('\n')
print('OLD:')
print(timeit.Timer('old()', 'from __main__ import old').timeit(1))

