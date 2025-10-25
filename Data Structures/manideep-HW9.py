##### Q1
def count_number_of_transpositions(a):
    #we split array in half and then do merge and count on each half, then combine.
    def f(b, c, d, e):
        if d == e:
            return 0
        m = (d + e) // 2
        x = f(b, c, d, m)
        y = f(b, c, m + 1, e)
        z = g(b, c, d, m, e)
        return x + y + z
    #as the question says nlogn we can use something similar to merge sort as it has same time complexity
    def g(b, c, d, m, e):
        i, j, k = d, m + 1, d
        r = 0

        while i <= m and j <= e:
            if b[i] <= b[j]:
                c[k] = b[i]
                i += 1
            else:
                c[k] = b[j]
                r += (m - i + 1)
                j += 1
            k += 1

        while i <= m:
            c[k] = b[i]
            i += 1
            k += 1

        while j <= e:
            c[k] = b[j]
            j += 1
            k += 1

        for i in range(d, e + 1):
            b[i] = c[i]

        return r

    c = [0] * len(a)
    return f(a, c, 0, len(a) - 1)

#print(count_number_of_transpositions([8, 4, 2, 1]))

""" output :
(base) manideep@Manideeps-Air ~ % python3 /Users/manideep/Downloads/sort.py
6
"""




##### Q2
def print_transpositions(S):
    b = []
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] > S[j]:
                b.append((S[i], S[j]))
                print(f"({S[i]}, {S[j]})")
    return b

#print_transpositions([8, 4, 2, 1])

""" output :
(base) manideep@Manideeps-Air ~ % python3 /Users/manideep/Downloads/sort.py
(8, 4)
(8, 2)
(8, 1)
(4, 2)
(4, 1)
(2, 1)
"""



#### Q3
from random import shuffle
class Sort:
    
    def __init__(self, N):
        self._list = [x for x in range(N)]
        shuffle(self._list)
        
    def first(self):
        return self._list[0]
    
    def second(self):
        return self._list[1]
    
    def swap_top_two(self):
        self._list[0], self._list[1] = self._list[1], self._list[0]
        
    def move_first_to_bottom(self):
        first = self._list.pop(0)
        self._list.append(first)
        
    def sort(self):
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        n = self.size()  

        for i in range(n):
            for j in range(n - 1):
                if self._list[j] > self._list[j + 1]:  
                    self._list[j], self._list[j + 1] = self._list[j + 1], self._list[j]

    def is_sorted(self):
        for i in range(self.size()-1):
            if self._list[i] > self._list[i+1]:
                return False
        return True
    
    def size(self):
        return len(self._list)
    
    def __repr__(self):
        return str(self._list)
        
c = Sort(20)
print("BEFORE:", c)       
print() 
 
c.sort()
print("AFTER:", c)       

print(c.is_sorted())  

"""output : 
        (base) manideep@Manideeps-Air ~ % python3 /Users/manideep/Downloads/sort.py    
BEFORE: [8, 3, 14, 9, 4, 17, 10, 12, 11, 6, 13, 1, 16, 0, 18, 2, 19, 7, 5, 15]

AFTER: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
True
(base) manideep@Manideeps-Air ~ % 
        """
