"""
3590. Kth Smallest Path XOR Sum - Hard


You are given an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. Each node i has an integer value vals[i], and its parent is given by par[i].

The path XOR sum from the root to a node u is defined as the bitwise XOR of all vals[i] for nodes i on the path from the root node to node u, inclusive.

You are given a 2D integer array queries, where queries[j] = [uj, kj]. For each query, find the kjth smallest distinct path XOR sum among all nodes in the subtree rooted at uj. If there are fewer than kj distinct path XOR sums in that subtree, the answer is -1.

Return an integer array where the jth element is the answer to the jth query.

In a rooted tree, the subtree of a node v includes v and all nodes whose path to the root passes through v, that is, v and its descendants.

 

Example 1:

Input: par = [-1,0,0], vals = [1,1,1], queries = [[0,1],[0,2],[0,3]]

Output: [0,1,-1]

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/05/29/screenshot-2025-05-29-at-204434.png)

Path XORs:

Node 0: 1
Node 1: 1 XOR 1 = 0
Node 2: 1 XOR 1 = 0
Subtree of 0: Subtree rooted at node 0 includes nodes [0, 1, 2] with Path XORs = [1, 0, 0]. The distinct XORs are [0, 1].

Queries:

queries[0] = [0, 1]: The 1st smallest distinct path XOR in the subtree of node 0 is 0.
queries[1] = [0, 2]: The 2nd smallest distinct path XOR in the subtree of node 0 is 1.
queries[2] = [0, 3]: Since there are only two distinct path XORs in this subtree, the answer is -1.
Output: [0, 1, -1]


Example 2:

Input: par = [-1,0,1], vals = [5,2,7], queries = [[0,1],[1,2],[1,3],[2,1]]

Output: [0,7,-1,0]

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/05/29/screenshot-2025-05-29-at-204534.png)

Path XORs:

Node 0: 5
Node 1: 5 XOR 2 = 7
Node 2: 5 XOR 2 XOR 7 = 0
Subtrees and Distinct Path XORs:

Subtree of 0: Subtree rooted at node 0 includes nodes [0, 1, 2] with Path XORs = [5, 7, 0]. The distinct XORs are [0, 5, 7].
Subtree of 1: Subtree rooted at node 1 includes nodes [1, 2] with Path XORs = [7, 0]. The distinct XORs are [0, 7].
Subtree of 2: Subtree rooted at node 2 includes only node [2] with Path XOR = [0]. The distinct XORs are [0].
Queries:

queries[0] = [0, 1]: The 1st smallest distinct path XOR in the subtree of node 0 is 0.
queries[1] = [1, 2]: The 2nd smallest distinct path XOR in the subtree of node 1 is 7.
queries[2] = [1, 3]: Since there are only two distinct path XORs, the answer is -1.
queries[3] = [2, 1]: The 1st smallest distinct path XOR in the subtree of node 2 is 0.
Output: [0, 7, -1, 0]

 

Constraints:

1 <= n == vals.length <= 5 * 10^4
0 <= vals[i] <= 10^5
par.length == n
par[0] == -1
0 <= par[i] < n for i in [1, n - 1]
1 <= queries.length <= 5 * 10^4
queries[j] == [uj, kj]
0 <= uj < n
1 <= kj <= n
The input is generated such that the parent array par represents a valid tree.
"""

from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet


class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(vals), len(queries)

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)

        off = defaultdict(list)
        for i, (a, k) in enumerate(queries):
            off[a].append((k, i))

        ans = [0] * m
        def dfs(a, x):
            x ^= vals[a]
            mp = SortedSet([x])

            for b in tree[a]:
                sub = dfs(b, x)
                if len(mp) < len(sub):
                    # We know that every mp of each node will be passed at most h (the height of the tree) times
                    # And Processing each node will take O(n * log(n)) time in the worst case (combining two sets)
                    # So the complexity of this operation is O(n * log(n) * h), which is quadratic in the worst case, right?
                    # But this optimization ensures that if a node only have one child, it will process in O(log(n)) time
                    # Therefore, the processing complexity becomes O(n * log(n)) only if the current node has more than one child
                    # 1. If every node has more than one child, then the height of the tree is at most O(log n)
                    #    O(n * log(n))     *     O(log(n)) = O(n * log(n)^2)
                    #    processing              height
                    # 2. And if the height of the tree is O(n), then every node has only one child
                    #    O(log(n))         *     O(n)      = O(n * log(n))
                    #    processing              height
                    # Therefore, case 1 is the worst case, and case 2 is the best case
                    # So the overall complexity is O(n * log(n)^2) in the worst case, and O(n * log(n)) in the best case
                    mp, sub = sub, mp
                mp.update(sub)

            for k, i in off[a]:
                ans[i] = -1 if k - 1 >= len(mp) else mp[k - 1]

            return mp
        
        dfs(0, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.kthSmallest([-1, 0, 0], [1, 1, 1], [[0, 1], [0, 2], [0, 3]]))  # [0, 1, -1]

    # Example 2
    print(sol.kthSmallest([-1, 0, 1], [5, 2, 7], [[0, 1], [1, 2], [1, 3], [2, 1]]))  # [0, 7, -1, 0]
