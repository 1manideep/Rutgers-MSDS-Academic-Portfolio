class LinkedList:

  #-------------------------- nested _Node class --------------------------
  class _Node:
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- list methods -------------------------------
  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0                          

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def front(self):
    if self.is_empty():
      raise ValueError('list is empty')
    return self._head._element              # front aligned with head of list

  def remove_front(self):
    if self.is_empty():
      raise ValueError('list is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as list is empty
      self._tail = None                     # removed head had been the tail
    return answer
  
  def add_to_front(self, e):
      self._head = self._Node(e, self._head)   
      if self.is_empty():
            self._tail = self._head
      self._size += 1
  
  def add_to_rear(self, e):
      newest = self._Node(e, None)            # node will be new tail node
      if self.is_empty():
          self._head = newest                   # special case: previously empty
      else:
          self._tail._next = newest
      self._tail = newest                     # update reference to tail node
      self._size += 1

  def __repr__(self):
      elements = []
      cursor = self._head 
      while cursor is not None:
          elements.append(str(cursor._element))
          cursor = cursor._next
      
      return " -> ".join(elements)

  def find(self, e):
      cursor = self._head 
      while cursor is not None:
          if cursor._element == e:
              return cursor
          cursor = cursor._next

  def findPredecessor(self, e):
      predecessor = None
      cursor = self._head 
      while cursor is not None:
          if cursor._element == e:
              return predecessor, cursor
          predecessor = cursor
          cursor = cursor._next      
 
  def insert(self, insertAt, e):
      predecessor, cursor = self.findPredecessor(insertAt)
      if cursor is None:
          raise ValueError('Not in list')
          
      if predecessor is None:
          self.add_to_front(e)
      else:
          predecessor._next = self._Node(e, cursor)
          
  def delete(self, e):
      predecessor, cursor = self.findPredecessor(e)
      if cursor is None:
          raise ValueError('Not in list')
          
      if predecessor is None:
          self.remove_front()
      else:
          predecessor._next = cursor._next
          if self._tail == cursor:
              self._tail = predecessor
              
  # 1
  def size(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current._next
        return count

  # 2
  def search(self, target):
        def _search_recursive(node):
            if node is None:
                return False
            if node._element == target:
                return True
            return _search_recursive(node._next)
        return _search_recursive(self._head)

  # 3
  def second_to_last(self):
        if self._head is None or self._head._next is None:
            raise ValueError("List must have at least two elements")
        current = self._head
        while current._next._next is not None:
            current = current._next
        return current._element

  # 4
  def reverse(self):
        prev = None
        current = self._head
        while current is not None:
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node
        self._head = prev

  # 5
  def removeDuplicates(self):
        current = self._head
        while current is not None and current._next is not None:
            if current._element == current._next._element:
                current._next = current._next._next
                self._size -= 1
            else:
                current = current._next

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_to_front(3)
    ll.add_to_front(2)
    ll.add_to_front(2)
    ll.add_to_front(1)
    print("Original List:", ll)
    print("Size of list:", ll.size())
    ll.removeDuplicates()
    print("List after removing duplicates:", ll)
    ll.reverse()
    print("Reversed List:", ll)
    print("Second to Last Element:", ll.second_to_last())
    print("Search for 2:", ll.search(2))
