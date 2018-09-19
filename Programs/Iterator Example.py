def myrange(l):
    i = 0
    if i < l:
        yield i #Returns i and continues code
        i+= 1
        print('Hi')

for i in myrange(10):
    print(i)


#-=-=-=-=-=-=-=-=-=#
class myr:
    def __init__(self, l):
        self._l = l
        self._i = -1
    def __next__(self):
        if self._i < self._l:
            self._i += 1
            return self._i
        else:
            raise StopIteration() #throw


I = myr(10)
for i in range (10):
    print(next(I))

while True:
    try:
        print(next(I))
    except StopIteration():
        break
#-=-=-=-=-=-=-=-=-=-=#
def fib():
    a= 0
    b = 1
    yield a
    yield b
    while True:
        a,b =b,a+b
    
for x,y in zip(fib, range(10)):
    print(x)
I = fib()
for i in range (10):
    print(next(I))

while True:
    try:
        print(next(I))
    except StopIteration():
        break