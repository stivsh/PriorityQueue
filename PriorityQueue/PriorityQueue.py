from collections import namedtuple

HeapElement = namedtuple('HeapElement', ['priority', 'key'])

def Lofinx(inx):
    """return the lavel of heap depth for index"""
    
    return (inx+1).bit_length()-1
  
    
def firstinL(L):
    """return the first index in the heap layer"""
    
    return 2**L-1


def parentinx(inx):
    """return the index of the parent node in the
        index belongs to root return negative value"""
    
    L = Lofinx(inx)
    return firstinL(L-1)+int((inx-firstinL(L))/2)


def childinxs(inx):
    """return the indexes of the cildren nodes,
        may be greater than the size of the heap"""
    
    L = Lofinx(inx)
    ch1 = firstinL(L+1)+2*(inx-firstinL(L))
    ch2 = ch1+1
    return ch1, ch2


class PriorityQueue:
    
    def __init__(self):
        self.heap = []
        self.indexes = {}
        
        
    def __add_to_heap__(self, priority, key):
        """Add value to the heap, key mast not be in the heap."""
        
        value = HeapElement(priority, key)
        self.heap.append(value)
        self.indexes[value.key] = len(self.heap)-1
        self.__restore_heap_up__(len(self.heap)-1)
        
        
    def __swap__(self,inx1,inx2):
        """Swap two elements in the heap. Heap is not consist after swapping."""
        
        val1 = self.heap[inx1]
        val2 = self.heap[inx2]
        self.heap[inx1] = val2
        self.heap[inx2] = val1
        self.indexes[val2.key]=inx1
        self.indexes[val1.key]=inx2
    
    
    def __restore_heap_down__(self, index):
        """Restore heap recursevly startind from this index,
            this node swaps with the child with higрest priority"""
        
        inx_of_max = index
        ch1,ch2 = childinxs(index)
        
        if ch1<len(self.heap):
            if self.heap[ch1].priority > self.heap[inx_of_max].priority:
                inx_of_max = ch1
                
        if ch2<len(self.heap):
            if self.heap[ch2].priority > self.heap[inx_of_max].priority:
                inx_of_max = ch2

        if inx_of_max != index:
            self.__swap__(inx_of_max,index)
            self.__restore_heap_down__(inx_of_max)
                
        
    def __restore_heap_up__(self,index):
        """Restore heap recursevly startind from this index,
            this node swaps with the parent node if it has higher priority"""
        
        if index > 0:
            pinx = parentinx(index)
            if self.heap[index].priority > self.heap[pinx].priority:
                self.__swap__(index,pinx)
                self.__restore_heap_up__(pinx)
            
    def has(self, key):
        """check if the key exists in the heap"""
        return key in self.indexes
        

    def removekey(self, key):
        """Remove this key from heap"""
        if key not in self.indexes:
            return
        
        index = self.indexes[key]
        while index != 0:
            pinx = parentinx(index)
            self.__swap__(pinx,index) 
            index = pinx
        self.pop()
    
    
    def push(self, priority, key):
        """Add element into heap, if this key already in the heap and priority in the heap is lower,
        the new priority set up, if the priority less then existant nothing happen."""
        
        if key in self.indexes:
            heap_inx = self.indexes[key]
            if self.heap[heap_inx].priority <= priority:
                self.removekey(key)
            else:
                return
        self.__add_to_heap__(priority, key)
    
    
    def pop(self):
        """Return the key with the greatest prioryty"""
        if len(self.heap):
            self.__swap__(0,len(self.heap)-1)
            value = self.heap.pop()
            del self.indexes[value.key]
            if len(self.heap):
                self.__restore_heap_down__(0)
                
            return value.key
        else:
            raise IndexError()
            
            
    def size(self):
        return len(self.heap)
        