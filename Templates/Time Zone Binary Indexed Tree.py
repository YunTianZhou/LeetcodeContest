class TimeZoneBinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.now = 0
        self.tree = [0] * (n + 1)
        self.time = [0] * (n + 1)

    def update(self, idx: int, delta: int):
        while idx <= self.n:
            if self.time[idx] < self.now:
                self.time[idx] = self.now
                self.tree[idx] = 0
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        total = 0
        while idx > 0:
            if self.time[idx] == self.now:
                total += self.tree[idx]
            idx -= idx & -idx
        return total

    def range_query(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)

    def reset(self):
        self.now += 1
