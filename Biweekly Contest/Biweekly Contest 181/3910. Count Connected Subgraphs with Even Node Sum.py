"""
3910. Count Connected Subgraphs with Even Node Sum - Hard


You are given an undirected graph with n nodes labeled from 0 to n - 1. Node i has a value of nums[i], which is either 0 or 1. The edges of the graph are given by a 2D array edges where edges[i] = [ui, vi] represents an edge between node ui and node vi.

For a non-empty subset s of nodes in the graph, we consider the induced subgraph of s generated as follows:

 - We keep only the nodes in s.

 - We keep only the edges whose two endpoints are both in s.

Return an integer representing the number of non-empty subsets s of nodes in the graph such that:

 - The induced subgraph of s is connected.

 - The sum of node values in s is even.



Example 1:

Input: nums = [1,0,1], edges = [[0,1],[1,2]]

Output: 2

Explanation:

s        connected?  sum of node values  counted?
[0]      Yes         1                   No
[1]      Yes         0                   Yes
[2]      Yes         1                   No
[0,1]    Yes         1                   No
[0,2]    No 1 -> 2   2                   No
[1,2]    Yes         1                   No
[0,1,2]  Yes         2                   Yes


Example 2:

Input: nums = [1], edges = []

Output: 0

Explanation:

s    connected?  sum of node values  counted?
[0]  Yes         1                   No



Constraints:

1 <= n == nums.length <= 13
nums[i] is 0 or 1.
0 <= edges.length <= n * (n - 1) / 2
edges[i] = [ui, vi]
0 <= ui < vi < n
All edges are distinct.
"""


class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)

        g = [0] * n
        for a, b in edges:
            g[a] |= 1 << b
            g[b] |= 1 << a

        odd = sum(x << i for i, x in enumerate(nums))
        ok = [False] * (1 << n)

        ans = 0
        for s in range(1, 1 << n):
            x = s
            while x:
                b = x & -x
                t = s ^ b
                if t == 0 or ok[t] and g[b.bit_length() - 1] & t:
                    ok[s] = True
                    break
                x ^= b
            
            ans += ok[s] and ((s & odd).bit_count() & 1) == 0

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.evenSumSubgraphs([1, 0, 1], [[0, 1], [1, 2]]))  # 2

    # Example 2
    print(sol.evenSumSubgraphs([1], []))  # 0
