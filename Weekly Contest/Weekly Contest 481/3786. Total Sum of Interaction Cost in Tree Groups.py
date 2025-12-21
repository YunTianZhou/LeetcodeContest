"""
3786. Total Sum of Interaction Cost in Tree Groups - Hard


You are given an integer n and an undirected tree with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given an integer array group of length n, where group[i] denotes the group label assigned to node i.

 - Two nodes u and v are considered part of the same group if group[u] == group[v].

 - The interaction cost between u and v is defined as the number of edges on the unique path connecting them in the tree.

Return an integer denoting the sum of interaction costs over all unordered pairs (u, v) with u != v such that group[u] == group[v].



Example 1:

Input: n = 3, edges = [[0,1],[1,2]], group = [1,1,1]

Output: 4

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/09/24/screenshot-2025-09-24-at-50538-pm.png)

All nodes belong to group 1. The interaction costs between the pairs of nodes are:

 - Nodes (0, 1): 1
 - Nodes (1, 2): 1
 - Nodes (0, 2): 2

Thus, the total interaction cost is 1 + 1 + 2 = 4.


Example 2:

Input: n = 3, edges = [[0,1],[1,2]], group = [3,2,3]

Output: 2

Explanation:

 - Nodes 0 and 2 belong to group 3. The interaction cost between this pair is 2.

 - Node 1 belongs to a different group and forms no valid pair. Therefore, the total interaction cost is 2.


Example 3:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], group = [1,1,4,4]

Output: 3

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/09/24/screenshot-2025-09-24-at-51312-pm.png)

Nodes belonging to the same groups and their interaction costs are:

 - Group 1: Nodes (0, 1): 1
 - Group 4: Nodes (2, 3): 2

Thus, the total interaction cost is 1 + 2 = 3.


Example 4:

Input: n = 2, edges = [[0,1]], group = [9,8]

Output: 0

Explanation:

All nodes belong to different groups and there are no valid pairs. Therefore, the total interaction cost is 0.



Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i] = [ui, vi]
0 <= ui, vi <= n - 1
group.length == n
1 <= group[i] <= 20
The input is generated such that edges represents a valid tree.
"""

from typing import List


class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        m = max(group)
        
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        total = [0] * (m + 1)
        for x in group:
            total[x] += 1

        ans = 0
            
        def dfs(a, fa):
            nonlocal ans
            
            cnt = [0] * (m + 1)
            cnt[group[a]] += 1
            
            for b in tree[a]:
                if b == fa:
                    continue
                    
                ncnt = dfs(b, a)                
                for g in range(1, m + 1):
                    ans += ncnt[g] * (total[g] - ncnt[g])
                    cnt[g] += ncnt[g]

            return cnt
            
        dfs(0, -1)
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.interactionCosts(3, [[0, 1], [1, 2]], [1, 1, 1]))  # 4

    # Example 2
    print(sol.interactionCosts(3, [[0, 1], [1, 2]], [3, 2, 3]))  # 2

    # Example 3
    print(sol.interactionCosts(4, [[0, 1], [0, 2], [0, 3]], [1, 1, 4, 4]))  # 3

    # Example 4
    print(sol.interactionCosts(2, [[0, 1]], [9, 8]))  # 0
    