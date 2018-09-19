import heapq

class Passenger:
    def __init__(self, first, last, status, fair, bags):
        self._first = first
        self._last = last
        self._stat = status
        self._fair = fair
        self._bags = bags
        self.num = 0
    def __lt__(self, p):
        stat1 = self.check_status()
        stat2 = p.check_status()
        if stat1 == stat2:
            if self._bags > p._bags: #This wasn't well explained on Piazza, I'm making it the higher the num of bags, the higher the status
                stat1 += 1
            elif self._bags < p._bags:
                stat2 +=1
        if stat1 == stat2:
            if self._fair > p._fair:
                stat1 += 1
            elif self._fair < p._fair:
                stat2 += 1
        if stat1 == stat2:
            if self.num > p.num:
                stat1+=1
            elif self.num < p.num:
                stat2 += 1
        return stat1 <= stat2
    
    def check_status(self):
        if self._stat == 'None':
            return 0
        elif self._stat == 'Gold':
            return 1
        elif self._stat == 'Silver':
            return 2
        elif self._stat == 'Platinum':
            return 3
        elif self._stat == '1K':
            return 4
        elif self._stat == 'Global Services':
            return 5
        elif self._stat == 'Employee':
            return 6
        
            
class Flight:
    def __init__(self, cap):
        self._cap = cap
        self._num = 0
        self._final = False
        self._l = []
    def board (self, passenger):
        if self._final == False:        
            self._l.append(passenger)
            self._num +=1
            passenger.num = self._num
        else:
            print('Cannot add to flight since it has been finalized')
    def finalize(self):
        self._final = True
        heapq.heapify(self._l)
    def whoToRemove(self):
        remove_list = []
        e = self._num - self._cap
        if self._final == False:
            print('Cannot check, finalize must be called first')
        else:
            if e <= 0:
                print('Noone to remove')
                return remove_list
            else:
                for i in range (e):
                    remove_list.append(heapq.heappop(self._l))
        return remove_list
        