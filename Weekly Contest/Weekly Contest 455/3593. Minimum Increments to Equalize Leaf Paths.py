"""
3593. Minimum Increments to Equalize Leaf Paths - Medium


You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an edge from node ui to vi .

Each node i has an associated cost given by cost[i], representing the cost to traverse that node.

The score of a path is defined as the sum of the costs of all nodes along the path.

Your goal is to make the scores of all root-to-leaf paths equal by increasing the cost of any number of nodes by any non-negative amount.

Return the minimum number of nodes whose cost must be increased to make all root-to-leaf path scores equal.

 

Example 1:

Input: n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]

Output: 1

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/05/28/screenshot-2025-05-28-at-134018.png)

There are two root-to-leaf paths:

Path 0 → 1 has a score of 2 + 1 = 3.
Path 0 → 2 has a score of 2 + 3 = 5.
To make all root-to-leaf path scores equal to 5, increase the cost of node 1 by 2.
Only one node is increased, so the output is 1.


Example 2:

Input: n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]

Output: 0

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/05/28/screenshot-2025-05-28-at-134249.png)

There is only one root-to-leaf path:

Path 0 → 1 → 2 has a score of 5 + 1 + 4 = 10.

Since only one root-to-leaf path exists, all path costs are trivially equal, and the output is 0.


Example 3:

Input: n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7]

Output: 1

Explanation:

[graph3](https://assets.leetcode.com/uploads/2025/05/28/screenshot-2025-05-28-at-135704.png)

There are three root-to-leaf paths:

Path 0 → 4 has a score of 3 + 7 = 10.
Path 0 → 1 → 2 has a score of 3 + 4 + 1 = 8.
Path 0 → 1 → 3 has a score of 3 + 4 + 1 = 8.
To make all root-to-leaf path scores equal to 10, increase the cost of node 1 by 2. Thus, the output is 1.

 

Constraints:

2 <= n <= 10^5
edges.length == n - 1
edges[i] == [ui, vi]
0 <= ui, vi < n
cost.length == n
1 <= cost[i] <= 10^9
The input is generated such that edges represents a valid tree.
"""

from typing import List


class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(a, fa):
            cnt = 0
            values = []

            for b in graph[a]:
                if b == fa:
                    continue
                sub_cnt, sub_value = dfs(b, a)
                cnt += sub_cnt
                values.append(sub_value)
            
            max_value = max(values, default=0)
            value = max_value + cost[a]
            cnt += sum(1 for x in values if x < max_value)

            return cnt, value
        
        cnt, _ = dfs(0, -1)
        return cnt
    

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minIncrease(3, [[0, 1], [0, 2]], [2, 1, 3]))  # 1

    # Example 2
    print(sol.minIncrease(3, [[0, 1], [1, 2]], [5, 1, 4]))  # 0

    # Example 3
    print(sol.minIncrease(5, [[0, 4], [0, 1], [1, 2], [1, 3]], [3, 4, 1, 1, 7]))  # 1
