"""
Revised Methods:
    We had to modify get and put, because they are used in our delete method and needed revisions for AVAIL marker.
    - delete: modified to use AVAIL marker to indicate deleted slots instead of rehashing the keys in same cluster.
    - get: modified to skip all AVAIL markers while searching.
    - put: modified to treat AVAIL markers as available slots while inserting.  
"""
class LinearProbingHashST:
    INIT_CAPACITY = 11

    def __init__(self, m=None, max_load = 0.50):
        self.n = 0  
        self.m = m or LinearProbingHashST.INIT_CAPACITY 
        self.max_load = max_load
        self.keys = [None for _ in range(self.m)]
        self.vals = [None for _ in range(self.m)]
        self.AVAIL = object()

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.m

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

    def get(self, key):
        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.vals[i]
            elif self.keys[i] == self.AVAIL: 
                i = (i + 1) % self.m
            else:
                i = (i + 1) % self.m
        return None


    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        if self.n / self.m >= self.max_load:
            self.resize(2 * self.m)

        i = self.hash(key)
        while self.keys[i] is not None and self.keys[i] != self.AVAIL:
            if self.keys[i] == key:
                self.vals[i] = val
                return
            i = (i + 1) % self.m
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def delete(self, key):
        if not self.contains(key):
            return

        i = self.hash(key)
        while self.keys[i] != key:
            i = (i + 1) % self.m

        self.keys[i] = self.AVAIL
        self.vals[i] = None
        self.n -= 1

        if self.n > 0 and self.n <= self.m / 8:
            self.resize(self.m // 2)
    
    def resize(self, capacity):
        tmp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self.keys[i] is not None:
                tmp.put(self.keys[i], self.vals[i])

        self.m = tmp.m
        self.keys = tmp.keys
        self.vals = tmp.vals
    
    def load_factor(self):
        return self.n / self.m 

    def expected_insert_probes(self):
        n_probes = 0
        clustersizes = []
        current = 0
        for key in self.keys:
            if key is not None and key != self.DELETED:
                current += 1
            else:
                if current > 0:
                    clustersizes.append(current)
                    current = 0
        if current > 0:
            clustersizes.append(current)

        for size in clustersizes:
            n_probes += size * (size + 1) / 2
        return n_probes / self.n if self.n > 0 else 0

    def theoretical_insert_probes(self):
        lf = self.load_factor()
        return 0.5 * (1 + 1 / (1 - lf)) if lf < 1 else float('inf')
