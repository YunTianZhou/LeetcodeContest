"""
3615. Longest Palindromic Path in Graph - Hard


You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1 and a 2D array edges, where edges[i] = [ui, vi] indicates an edge between nodes ui and vi.

You are also given a string label of length n, where label[i] is the character associated with node i.

You may start at any node and move to any adjacent node, visiting each node at most once.

Return the maximum possible length of a palindrome that can be formed by visiting a set of unique nodes along a valid path.



Example 1:

Input: n = 3, edges = [[0,1],[1,2]], label = "aba"

Output: 3

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/06/13/screenshot-2025-06-13-at-230714.png)

The longest palindromic path is from node 0 to node 2 via node 1, following the path 0 → 1 → 2 forming string "aba".

This is a valid palindrome of length 3.


Example 2:

Input: n = 3, edges = [[0,1],[0,2]], label = "abc"

Output: 1

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/06/13/screenshot-2025-06-13-at-230017.png)

No path with more than one node forms a palindrome.

The best option is any single node, giving a palindrome of length 1.


Example 3:

Input: n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac"

Output: 3

Explanation:

[graph3](https://assets.leetcode.com/uploads/2025/06/13/screenshot-2025-06-13-at-230508.png)

The longest palindromic path is from node 0 to node 1, following the path 0 → 3 → 1, forming string "bcb".

This is a valid palindrome of length 3.



Constraints:

1 <= n <= 14
n - 1 <= edges.length <= n * (n - 1) / 2
edges[i] == [ui, vi]
0 <= ui, vi <= n - 1
ui != vi
label.length == n
label consists of lowercase English letters.
There are no duplicate edges.
"""

from typing import List
from collections import deque


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph = [[] for _ in range(n)]
        dq = deque((a, a, 1, 0) for a in range(n))
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            if label[a] == label[b]:
                if a > b:
                    a, b = b, a
                dq.append((a, b, 2, 0))
        
        visit = set()
        ans = 0
        while dq:
            a, b, k, mask = dq.popleft()
            ans = max(ans, k)
            mask |= 1 << a | 1 << b
            for next_a in graph[a]:
                if mask & (1 << next_a):
                    continue
                for next_b in graph[b]:
                    if mask & (1 << next_b) or next_a == next_b:
                        continue
                    if label[next_a] == label[next_b]:
                        if next_a > next_b:
                            next_a, next_b = next_b, next_a
                        if (next_a, next_b, mask) not in visit:
                            visit.add((next_a, next_b, mask))
                            dq.append((next_a, next_b, k + 2, mask))

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxLen(3, [[0, 1], [1, 2]], "aba"))  # 3

    # Example 2
    print(sol.maxLen(3, [[0, 1], [0, 2]], "abc"))  # 1

    # Example 3
    print(sol.maxLen(4, [[0, 2], [0, 3], [3, 1]], "bbac"))  # 3
