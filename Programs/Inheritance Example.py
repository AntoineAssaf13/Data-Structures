class Counter:
    def __init__(self):
        self._x = 0
    def inc(self):
        self._x+=1
    def value(self):
        return self._x
    def __str__(self):
        return str(self._x)
    
class Lcounter(Counter):
    def __init__(self, i):
        super().__init__()
        self._i = i
    def inc(self):
        self._x += self._i
            
