from queue import PriorityQueue

#Q1
class StackUsingPriorityQueue:
    def __init__(self):
        self.priority_queue = PriorityQueue()
        self.order = 0 
    
    def push(self, item):
        self.priority_queue.put((-self.order, item))
        self.order += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("empty!")
        return self.priority_queue.get()[1]

    def is_empty(self):
        return self.priority_queue.empty()

# Q2
class QueueUsingPriorityQueue:
    def __init__(self):
       self.priority_queue = PriorityQueue()
       self.order = 0 
    
    
    def enqueue(self, item):
        self.priority_queue.put((self.order, item))
        self.order += 1
    
    def dequeue(self):
        if self.priority_queue.empty():
            raise IndexError("empty!")
        return self.priority_queue.get()[1]
    
    def is_empty(self):
        return self.priority_queue.empty()    
    
#Q3
#assuming using i in for loop won't count as another variable here.
def findKthElement(lst, k):
    min_heap = PriorityQueue(maxsize=k)
    for i in lst:
        if min_heap.qsize() < k:
            min_heap.put(i) 
        else:
            if i > min_heap.queue[0]: 
                min_heap.get()         
                min_heap.put(i)      

    return min_heap.get()
