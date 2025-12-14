"""
3777. Minimum Deletions to Make Alternating Substring - Hard


You are given a string s of length n consisting only of the characters 'A' and 'B'.

You are also given a 2D integer array queries of length q, where each queries[i] is one of the following:

 - [1, j]: Flip the character at index j of s i.e. 'A' changes to 'B' (and vice versa). This operation mutates s and affects subsequent queries.

 - [2, l, r]: Compute the minimum number of character deletions required to make the substring s[l..r] alternating. This operation does not modify s; the length of s remains n.

A substring is alternating if no two adjacent characters are equal. A substring of length 1 is always alternating.

Return an integer array answer, where answer[i] is the result of the ith query of type [2, l, r].



Example 1:

Input: s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]

Output: [0,2]

Explanation:

i  ueries[i]  j  l  r  s before query  s[l..r]  Result                          Answer
0  2, 1, 2]   -  1  2  "ABA"           "BA"     Already alternating             0
1  1, 1]      1  -  -  "ABA"           -        Flip s[1] from 'B' to 'A'       -
2  [2, 0, 2]  -  0  2  "AAA"           "AAA"    Delete any two 'A's to get "A"  2

Thus, the answer is [0, 2].


Example 2:

Input: s = "ABB", queries = [[2,0,2],[1,2],[2,0,2]]

Output: [1,0]

Explanation:

i  queries[i]  j  l  r  s before query  s[l..r]  Result                      Answer
0  [2, 0, 2]   -  0  2  "ABB"           "ABB"    Delete one 'B' to get "AB"  1
1  [1, 2]      2  -  -  "ABB"           -        Flip s[2] from 'B' to 'A'   -
2  [2, 0, 2]   -  0  2  "ABA"           "ABA"    Already alternating         0

Thus, the answer is [1, 0].


Example 3:

Input: s = "BABA", queries = [[2,0,3],[1,1],[2,1,3]]

Output: [0,1]

Explanation:

i  queries[i]  j  l  r  s before query  s[l..r]  Result                      Answer
0  [2, 0, 3]   -  0  3  "BABA"          "BABA"   Already alternating         0
1  [1, 1]      1  -  -  "BABA"          -        Flip s[1] from 'A' to 'B'   -
2  [2, 1, 3]   -  1  3  "BBBA"          "BBA"    Delete one 'B' to get "BA"  1

Thus, the answer is [0, 1].



Constraints:

1 <= n == s.length <= 10^5
s[i] is either 'A' or 'B'.
1 <= q == queries.length <= 10^5
queries[i].length == 2 or 3
queries[i] == [1, j] or,
queries[i] == [2, l, r]
0 <= j <= n - 1
0 <= l <= r <= n - 1
"""

from typing import List


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

    def range_query(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        s = list(s)

        bit = BinaryIndexedTree(n + 1)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                bit.update(i + 1, 1)

        ans = []
        for query in queries:
            if query[0] == 1:
                i = query[1]
                s[i] = "B" if s[i] == "A" else "A"
                if i > 0:
                    bit.update(i + 1, 1 if s[i] == s[i - 1] else -1)
                if i + 1 < n:
                    bit.update(i + 2, 1 if s[i] == s[i + 1] else -1)         
            else:
                ans.append(bit.range_query(query[1] + 2, query[2] + 1))

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minDeletions("ABA", [[2, 1, 2], [1, 1], [2, 0, 2]]))  # [0, 2]

    # Example 2
    print(sol.minDeletions("ABB", [[2, 0, 2], [1, 2], [2, 0, 2]]))  # [1, 0]

    # Example 3
    print(sol.minDeletions("BABA", [[2, 0, 3], [1, 1], [2, 1, 3]]))  # [0, 1]
