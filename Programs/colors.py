class Color:
    def __init__(self,r,g,b):
        self._r = r
        self._g = g
        self._b = b
    def __hash__(self):
        return hash((self._r,self._g,self._b)) #relies on system
        

