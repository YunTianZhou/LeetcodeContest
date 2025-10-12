"""
3715. Sum of Perfect Square Ancestors - Hard


You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given an integer array nums, where nums[i] is the positive integer assigned to node i.

Define a value ti as the number of ancestors of node i such that the product nums[i] * nums[ancestor] is a perfect square.

Return the sum of all ti values for all nodes i in range [1, n - 1].

Note:

 - In a rooted tree, the ancestors of node i are all nodes on the path from node i to the root node 0, excluding i itself.



Example 1:

Input: n = 3, edges = [[0,1],[1,2]], nums = [2,8,2]

Output: 3

Explanation:

i  Ancestors  nums[i] * nums[ancestor]        Square Check                       ti
1  [0]        nums[1] * nums[0] = 8 * 2 = 16  16 is a perfect square             1
2  [1, 0]     nums[2] * nums[1] = 2 * 8 = 16  Both 4 and 16 are perfect squares  2
              nums[2] * nums[0] = 2 * 2 = 4   

Thus, the total number of valid ancestor pairs across all non-root nodes is 1 + 2 = 3.


Example 2:

Input: n = 3, edges = [[0,1],[0,2]], nums = [1,2,4]

Output: 1

Explanation:

i  Ancestors  nums[i] * nums[ancestor]       Square Check               ti
1  [0]        nums[1] * nums[0] = 2 * 1 = 2  2 is not a perfect square  0
2  [0]        nums[2] * nums[0] = 4 * 1 = 4  4 is a perfect square      1

Thus, the total number of valid ancestor pairs across all non-root nodes is 1.


Example 3:

Input: n = 4, edges = [[0,1],[0,2],[1,3]], nums = [1,2,9,4]

Output: 2

Explanation:

i  Ancestors  nums[i] * nums[ancestor]       Square Check                ti
1  [0]        nums[1] * nums[0] = 2 * 1 = 2  2 is not a perfect square   0
2  [0]        nums[2] * nums[0] = 9 * 1 = 9  9 is a perfect square       1
3  [1, 0]     nums[3] * nums[1] = 4 * 2 = 8  Only 4 is a perfect square  1
              nums[3] * nums[0] = 4 * 1 = 4

Thus, the total number of valid ancestor pairs across all non-root nodes is 0 + 1 + 1 = 2.



Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i] = [ui, vi]
0 <= ui, vi <= n - 1
nums.length == n
1 <= nums[i] <= 10^5
The input is generated such that edges represents a valid tree.
"""

from typing import List
from collections import defaultdict


m = 10 ** 5
core = [0] * (m + 1)
for i in range(1, m + 1):
    if core[i] == 0:
        for j in range(1, int(((m + 1) // i) ** 0.5) + 1):
            core[i * j * j] = i


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        cnt = defaultdict(int)

        def dfs(a, fa):
            nonlocal ans
            ans += cnt[core[nums[a]]]

            cnt[core[nums[a]]] += 1

            for b in graph[a]:
                if b == fa:
                    continue
                dfs(b, a)

            cnt[core[nums[a]]] -= 1

        dfs(0, -1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.sumOfAncestors(3, [[0, 1], [1, 2]], [2, 8, 2]))  # 3

    # Example 2
    print(sol.sumOfAncestors(3, [[0, 1], [0, 2]], [1, 2, 4]))  # 1

    # Example 3
    print(sol.sumOfAncestors(4, [[0, 1], [0, 2], [1, 3]], [1, 2, 9, 4]))  # 2
    