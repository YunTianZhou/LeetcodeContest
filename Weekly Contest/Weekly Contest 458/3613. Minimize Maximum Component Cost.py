"""
3613. Minimize Maximum Component Cost - Medium


You are given an undirected connected graph with n nodes labeled from 0 to n - 1 and a 2D integer array edges where edges[i] = [ui, vi, wi] denotes an undirected edge between node ui and node vi with weight wi, and an integer k.

You are allowed to remove any number of edges from the graph such that the resulting graph has at most k connected components.

The cost of a component is defined as the maximum edge weight in that component. If a component has no edges, its cost is 0.

Return the minimum possible value of the maximum cost among all components after such removals.



Example 1:

Input: n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2

Output: 4

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/04/19/minimizemaximumm.jpg)

Remove the edge between nodes 3 and 4 (weight 6).

The resulting components have costs of 0 and 4, so the overall maximum cost is 4.


Example 2:

Input: n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1

Output: 5

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/04/19/minmax2.jpg)

No edge can be removed, since allowing only one component (k = 1) requires the graph to stay fully connected.

That single component's cost equals its largest edge weight, which is 5.



Constraints:

1 <= n <= 5 * 10^4
0 <= edges.length <= 10^5
edges[i].length == 3
0 <= ui, vi < n
1 <= wi <= 10^6
1 <= k <= n
The input graph is connected.
"""

from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k >= n:
            return 0

        uf = list(range(n))

        def find(x):
            while x != uf[x]:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        
        edges.sort(key=lambda x: x[2])
        components = n
        for a, b, w in edges:
            a = find(a)
            b = find(b)
            if a != b:
                uf[a] = b
                components -= 1
                if components <= k:
                    return w


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minCost(5, [[0, 1, 4], [1, 2, 3], [1, 3, 2], [3, 4, 6]], 2))  # 4

    # Example 2
    print(sol.minCost(4, [[0, 1, 5], [1, 2, 5], [2, 3, 5]], 1))  # 5
