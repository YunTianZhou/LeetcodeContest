"""
3585. Find Weighted Median Node in Tree - Hard


You are given an integer n and an undirected, weighted tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates an edge from node ui to vi with weight wi.

The weighted median node is defined as the first node x on the path from ui to vi such that the sum of edge weights from ui to x is greater than or equal to half of the total path weight.

You are given a 2D integer array queries. For each queries[j] = [uj, vj], determine the weighted median node along the path from uj to vj.

Return an array ans, where ans[j] is the node index of the weighted median for queries[j].

 

Example 1:

Input: n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]

Output: [0,1]

Explanation:

(graph1)[https://assets.leetcode.com/uploads/2025/05/26/screenshot-2025-05-26-at-193447.png]

+---------+------+--------------+--------------------+------+------------------------------------------------------+--------+
| Query   | Path | Edge Weights | Total Path Weight  | Half | Explanation                                          | Answer |
+---------+------+--------------+--------------------+------+------------------------------------------------------+--------+
| [1, 0]  | 1→0  | [7]          | 7                  | 3.5  | Sum from 1→0 = 7 >= 3.5, median is node 0.           | 0      |
+---------+------+--------------+--------------------+------+------------------------------------------------------+--------+
| [0, 1]  | 0→1  | [7]          | 7                  | 3.5  | Sum from 0→1 = 7 >= 3.5, median is node 1.           | 1      |
+---------+------+--------------+--------------------+------+------------------------------------------------------+--------+


Example 2:

Input: n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]]

Output: [1,0,2]

Explanation:

(graph2)[https://assets.leetcode.com/uploads/2025/05/26/screenshot-2025-05-26-at-193610.png]

+---------+-------------+--------------+--------------------+------+------------------------------------------------------+--------+
| Query   | Path        | Edge Weights | Total Path Weight  | Half | Explanation                                          | Answer |
+---------+-------------+--------------+--------------------+------+------------------------------------------------------+--------+
| [0, 1]  | 0→1         | [2]          | 2                  | 1    | Sum from 0→1 = 2 >= 1, median is node 1.             | 1      |
+---------+-------------+--------------+--------------------+------+------------------------------------------------------+--------+
| [2, 0]  | 2→0         | [4]          | 4                  | 2    | Sum from 2→0 = 4 >= 2, median is node 0.             | 0      |
+---------+-------------+--------------+--------------------+------+------------------------------------------------------+--------+
| [1, 2]  | 1→0→2       | [2, 4]       | 6                  | 3    | Sum from 1→0 = 2 < 3; 1→2 = 6 >= 3, median is node 2.| 2      |
+---------+-------------+--------------+--------------------+------+------------------------------------------------------+--------+


Example 3:

Input: n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]]

Output: [2,2]

Explanation:

(graph3)[https://assets.leetcode.com/uploads/2025/05/26/screenshot-2025-05-26-at-193857.png]

+---------+------------------+----------------+--------------------+------+------------------------------------------------------------------------------------------+--------+
| Query   | Path             | Edge Weights   | Total Path Weight  | Half | Explanation                                                                              | Answer |
+---------+------------------+----------------+--------------------+------+------------------------------------------------------------------------------------------+--------+
| [3, 4]  | 3→1→0→2→4       | [1, 2, 5, 3]   | 11                 | 5.5  | Sum 3→1 = 1 < 5.5; 3→0 = 3 < 5.5; 3→2 = 8 >= 5.5, median is node 2.                       | 2      |
+---------+------------------+----------------+--------------------+------+------------------------------------------------------------------------------------------+--------+
| [1, 2]  | 1→0→2            | [2, 5]         | 7                  | 3.5  | Sum 1→0 = 2 < 3.5; 1→2 = 7 >= 3.5, median is node 2.                                     | 2      |
+---------+------------------+----------------+--------------------+------+------------------------------------------------------------------------------------------+--------+
 


Constraints:

2 <= n <= 10^5
edges.length == n - 1
edges[i] == [ui, vi, wi]
0 <= ui, vi < n
1 <= wi <= 10^9
1 <= queries.length <= 10^5
queries[j] == [uj, vj]
0 <= uj, vj < n
The input is generated such that edges represents a valid tree.
"""

from typing import List


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(n)]
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        LIMIT = n.bit_length()
        depth = [0] * n
        distance = [0] * n
        parent = [[0] * LIMIT for _ in range(n)]

        def dfs(a, par, dst):
            parent[a][0] = par
            depth[a] = dst
            for b, w in tree[a]:
                if b != par:
                    distance[b] = distance[a] + w
                    dfs(b, a, dst + 1)

        dfs(0, 0, 0)

        for k in range(1, LIMIT):
            for i in range(n):
                parent[i][k] = parent[parent[i][k - 1]][k - 1]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            for k in range(LIMIT - 1, -1, -1):
                if depth[parent[a][k]] >= depth[b]:
                    a = parent[a][k]

            if a == b:
                return a

            for k in range(LIMIT - 1, -1, -1):
                if parent[a][k] != parent[b][k]:
                    a = parent[a][k]
                    b = parent[b][k]

            return parent[a][0]

        ans = []
        for a, b in queries:
            if a == b:
                ans.append(a)
                continue

            p = lca(a, b)
            total_weight = distance[a] + distance[b] - 2 * distance[p]
            swap = distance[a] < distance[b]

            if swap:
                a, b = b, a
            
            dst_a = distance[a]
            for k in range((depth[a] - depth[p]).bit_length() - 1, -1, -1):
                if (dst_a - distance[parent[a][k]]) * 2 < total_weight:
                    a = parent[a][k]

            ans.append(a if swap and (dst_a - distance[parent[a][0]]) * 2 > total_weight else parent[a][0])

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.findMedian(2, [[0, 1, 7]], [[1, 0],[0, 1]]))  # [0, 1]

    # Example 2
    print(sol.findMedian(3, [[0, 1, 2],[2, 0, 4]], [[0, 1],[2, 0],[1, 2]]))  # [1, 0, 2]

    # Example 3
    print(sol.findMedian(5, [[0, 1, 2],[0, 2, 5],[1, 3, 1],[2, 4, 3]], [[3, 4],[1, 2]]))  # [2, 2]
