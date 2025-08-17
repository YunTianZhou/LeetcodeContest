from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.component_count = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        self.component_count -= 1

        return True
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def count_components(self) -> int:
        return self.component_count


# If you want to use this class in a solution, you can do so like this:
class Solution:
    def func(self, n: int, edges: List[List[int]]) -> int:
        uf = list(range(n))

        def find(x: int) -> int:
            while x != uf[x]:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        
        for a, b in edges:
            uf[find(a)] = find(b)

        components = set(find(i) for i in range(n))
        return len(components)
