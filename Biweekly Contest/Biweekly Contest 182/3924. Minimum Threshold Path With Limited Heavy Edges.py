"""
3924. Minimum Threshold Path With Limited Heavy Edges - Hard


There is an undirected weighted graph with n nodes labeled from 0 to n - 1.

The graph is represented by a 2D integer array edges, where each edge edges[i] = [ui, vi, w​​​​​​​i] indicates that there is an undirected edge between nodes ui and vi with weight w​​​​​​​i.

You are also given integers source, target and k.

A threshold value determines whether an edge is considered light or heavy:

 - An edge is light if its weight is less than or equal to threshold.

 - An edge is heavy if its weight is greater than threshold.

A path from source to target is valid if it contains at most k heavy edges.

Return the minimum integer threshold such that at least one valid path exists from source to target. If no such path exists, return -1.



Example 1:

[graph1](https://assets.leetcode.com/uploads/2025/10/13/g6.png)

Input: n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1

Output: 4

Explanation:

The minimum threshold such that a path from node 0 to node 3 uses at most 1 heavy edge is 4.

 - Light edges: [1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]

 - Heavy edges: [0, 1, 5]

A valid path is 0 → 1 → 4 → 3. It uses only 1 heavy edge ([0, 1, 5]), which satisfies the limit k = 1.

Any smaller threshold would make it impossible to reach node 3 without exceeding 1 heavy edge.


Example 2:

[graph2](https://assets.leetcode.com/uploads/2025/10/12/g3_f.png)

Input: n = 6, edges = [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], source = 0, target = 4, k = 1

Output: -1

Explanation:

There is no path from node 0 to node 4. Since the target cannot be reached, the output is -1.


Example 3:

[graph3](https://assets.leetcode.com/uploads/2025/10/12/g5.png)

Input: n = 4, edges = [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], source = 0, target = 0, k = 0

Output: 0

Explanation:

The source and target are the same node. No edges need to be traversed, so the minimum threshold is 0.



Constraints:

1 <= n <= 10^3
0 <= edges.length <= 10^3
edges[i] = [ui, vi, wi]
0 <= ui, vi <= n - 1
1 <= wi <= 10^9
0 <= source, target <= n - 1
0 <= k <= edges.length
"""

from bisect import bisect_left
from collections import deque


class Solution:
    def minimumThreshold(self, n: int, edges: list[list[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        
        g = [[] for _ in range(n)]
        weights = [0]
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))
            weights.append(w)
        weights.sort()

        def ok(threshold):
            dq = deque([(source, 0)])
            vis = [False] * n

            while dq:
                a, c = dq.pop()
                if c > k: 
                    return False
                if a == target: 
                    return True
                if vis[a]: 
                    continue
                vis[a] = True

                for b, w in g[a]:
                    if vis[b]:
                        continue
                    if w <= threshold:
                        dq.append((b, c))
                    else:
                        dq.appendleft((b, c + 1))
            
            return False

        if not ok(weights[-1]): 
            return -1
        return weights[bisect_left(weights, True, key=ok)]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minimumThreshold(6, [[0, 1, 5], [1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]], 0, 3, 1))  # 4

    # Example 2
    print(sol.minimumThreshold(6, [[0, 1, 3], [1, 2, 4], [3, 4, 5], [4, 5, 6]], 0, 4, 1))  # -1

    # Example 3
    print(sol.minimumThreshold(4, [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 0, 2]], 0, 0, 0))  # 0
