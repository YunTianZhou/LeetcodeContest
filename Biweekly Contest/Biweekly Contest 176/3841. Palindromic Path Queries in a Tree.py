"""
3841. Palindromic Path Queries in a Tree - Hard


You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

 - "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.

 - "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.

Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi" can be rearranged into a palindrome, and false otherwise.



Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:

 - "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
 - "update 1 b": Update node 1 to 'b', now s = "abc".
 - "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.

Thus, answer = [true, false].


Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:

 - "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
 - "update 0 b": Update node 0 to 'b', now s = "bbca".
 - "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
 - "update 3 a": Update node 3 to 'a', s = "bbca".
 - "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.

Thus, answer = [false, false, true].



Constraints:

1 <= n == s.length <= 5 * 10^4
edges.length == n - 1
edges[i] = [ui, vi]
0 <= ui, vi <= n - 1
s consists of lowercase English letters.
The input is generated such that edges represents a valid tree.
1 <= queries.length <= 5 * 10^4
queries[i] = "update ui c" or
queries[i] = "query ui vi"
0 <= ui, vi <= n - 1
c is a lowercase English letter.
"""

from typing import List


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] ^= delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total ^= self.tree[idx]
            idx -= idx & -idx
        return total

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        s = list(ord(c) - ord("a") for c in s)

        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        m = n.bit_length()
        jump = [[0] * n for _ in range(m)]
        bit = BinaryIndexedTree(n + 1)

        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        time = 0

        def dfs(a, fa, d):
            depth[a] = d
            jump[0][a] = fa

            nonlocal time
            time += 1
            tin[a] = time
            for b in tree[a]:
                if b == fa:
                    continue
                dfs(b, a, d + 1)
            tout[a] = time

            bit.update(tin[a], 1 << s[a])
            bit.update(tout[a] + 1, 1 << s[a])

        dfs(0, 0, 0)

        for i in range(1, m):
            for a in range(n):
                jump[i][a] = jump[i - 1][jump[i - 1][a]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            d = depth[a] - depth[b]
            for i in range(m):
                if d >> i & 1:
                    a = jump[i][a]

            if a == b:
                return a

            for i in range(m - 1, -1, -1):
                if jump[i][a] != jump[i][b]:
                    a = jump[i][a]
                    b = jump[i][b]

            return jump[0][a]

        ans = []
        for q in queries:
            op, x, y = q.split()
            a = int(x)
            if op[0] == "u":
                c = ord(y) - ord("a")
                mask = (1 << c) ^ (1 << s[a])
                s[a] = c
                bit.update(tin[a], mask)
                bit.update(tout[a] + 1, mask)
            else:
                b = int(y)
                l = lca(a, b)
                mask = bit.query(tin[a]) ^ bit.query(tin[b]) ^ (1 << s[l])
                ans.append(mask & (mask - 1) == 0)
        
        return ans



if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.palindromePath(3, [[0, 1], [1, 2]], "aac", 
                             ["query 0 2", "update 1 b", "query 0 2"]))  # [True, False]

    # Example 2
    print(sol.palindromePath(4, [[0, 1], [0, 2], [0, 3]], "abca", 
                             ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]))  # [False, False, True]
