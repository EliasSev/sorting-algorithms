import numpy as np

class Sorting:
    
    def __init__(self, L):
        self._L = L
        self._n = len(L)
        self._record = []
        self._comp = 0

    def clear_record(self):
        self._record = []
        self._comp = 0


    def add_record(self, arr):
        A = arr.copy()
        self._record.append({"arr": A,
                             "comp": self._comp})
        

    def insertion_sort(self):
        A = self._L.copy()
        self.clear_record()

        for i in range(1, self._n):
            key = A[i]
            j = i - 1
            while j > -1 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
                self._comp += 1
            A[j+1] = key
            self.add_record(A)

        return self._record
    

    def quick_sort(self):
        A = self._L.copy()
        self.clear_record()
        p, r = 0, self._n - 1
        self._quick_sort(A, p, r)
        self.add_record(A)  # last step

        return self._record


    def _partition(self, A, p, r):
        x = A[r]
        i = p - 1

        for j in range(p, r):
            if A[j] <= x:
                i += 1 
                A[i], A[j] = A[j], A[i] 
                self.add_record(A)
            self._comp += 1
        A[i+1], A[r] = A[r], A[i+1]

        return i + 1
    

    def _quick_sort(self, A, p, r):
        if p < r:
            q = self._partition(A, p, r)
            self._quick_sort(A, p, q-1)
            self._quick_sort(A, q+1, r)
        

    def bubble_sort(self):
        A = self._L.copy()
        self.clear_record()
        corrected = False

        for i in range(self._n):
            for j in range(self._n-i-1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    corrected = True
                self.add_record(A)
                self._comp += 1
            if not corrected:
                break

        return self._record
    

    def selection_sort(self):
        A = self._L.copy()
        self.clear_record()

        for i in range(0, self._n - 1):
            iMin = i
            for j in range(i+1, self._n):
                if A[j] < A[iMin]:
                    iMin = j
                    self.add_record(A)
                self._comp += 1
            if iMin != i:
                A[iMin], A[i] = A[i], A[iMin]

        self.add_record(A)
        return self._record
    

    def merge_sort(self):
        A = self._L.copy()
        self.clear_record()
        self._merge_sort(A, 0, self._n-1)
        return self._record
    

    def _merge_sort(self, A, l, r):
        if l < r:
            m = l+(r-l) // 2
    
            self._merge_sort(A, l, m)
            self._merge_sort(A, m+1, r)
            self._merge(A, l, m, r)

    
    def _merge(self, A, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        L = [0] * (n1)
        R = [0] * (n2)
    
        for i in range(0, n1):
            L[i] = A[l + i]
        for j in range(0, n2):
            R[j] = A[m + 1 + j]
    
        i = j = 0
        k = l
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
            self._comp += 1
            self.add_record(A)

        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1

            self.add_record(A)

        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1

            self.add_record(A)


    def _is_sorted(self, A):
        n = len(A)
        for i in range(n-1):
            if A[i] > A[i+1]:
                return False
        return True
    

    def bogo_sort(self):
        A = self._L.copy()
        self.clear_record()
        self.add_record(A)
        while self._is_sorted(A) == False:
            np.random.shuffle(A)
            self.add_record(A)
            if len(self._record) >= 25000:
                break
        return self._record
    

    def _heapify(self, A, n, i):
        largest = i 
        l = 2 * i + 1
        r = 2 * i + 2 

        if l < n and A[i] < A[l]:
            largest = l
        if r < n and A[largest] < A[r]:
            largest = r
        if largest != i:
            (A[i], A[largest]) = (A[largest], A[i])

            self._comp += 1
            self.add_record(A)
            self._heapify(A, n, largest)
 
 
    def _heap_sort(self, A):
        n = len(A)

        for i in range(n // 2, -1, -1):
            self._heapify(A, n, i)
    
        for i in range(n - 1, 0, -1):
            (A[i], A[0]) = (A[0], A[i])
            self._heapify(A, i, 0)

    
    def heap_sort(self):
        A = self._L.copy()
        self.clear_record()
        self._heap_sort(A)
        self.add_record(A)

        return self._record


class Distributions:

    def __init__(self, n, lower, upper, inverse=False):
        self.n = n
        self.lower = lower
        self.upper = upper
        self.inverse = inverse


    def linear(self):
        A = np.linspace(self.lower, self.upper, self.n)

        if self.inverse:
            return A[::-1]
        
        np.random.shuffle(A)
        return A
    

    def quadratic(self):
        qlower = np.sqrt(self.lower)
        qupper = np.sqrt(self.upper)
        A = (np.linspace(qlower, qupper, self.n))**2

        if self.inverse:
            return A[::-1]
        
        np.random.shuffle(A)
        return A
    

    def step(self, levels=8):
        m = self.n // levels
        step_upper = self.upper / levels

        A = np.array([])
        for i in range(1, levels):
            B = np.ones(m) * step_upper * i
            A = np.concatenate((A, B))
        B = np.ones(self.n - (levels-1) * m) * self.upper
        A = np.concatenate((A, B))

        if self.inverse:
            return A[::-1]
        
        np.random.shuffle(A)
        return A
    
    
    def logarithmic(self, x0=5):
        A = np.linspace(1, np.exp(x0), self.n)
        A = np.log(A) * self.upper / x0

        if self.inverse:
            return A[::-1]
        
        np.random.shuffle(A)
        return A
    

    def exponential(self):
        A = np.exp(np.linspace(0, np.log(self.upper), self.n))

        if self.inverse:
            return A[::-1]
        
        np.random.shuffle(A)
        return A
    

    def Random(self):
        return np.random.randint(self.lower, self.upper, self.n)
