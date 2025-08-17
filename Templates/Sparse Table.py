from typing import List


class SparseTable:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        k = self.log[self.n] + 1
        self.st = [[0] * k for _ in range(self.n)]
        
        for i in range(self.n):
            self.st[i][0] = data[i]
        
        for j in range(1, k):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = self.combine(self.st[i][j-1], self.st[i + (1 << (j - 1))][j-1])

    def query(self, l: int, r: int) -> int:
        j = self.log[r - l + 1]
        return self.combine(self.st[l][j], self.st[r - (1 << j) + 1][j])
    
    def combine(self, a: int, b: int) -> int:
        return min(a, b)
        # return max(a, b)
        # return gcd(a, b)
