"""
3639. Minimum Time to Activate String - Medium


You are given a string s of length n and an integer array order, where order is a permutation of the numbers in the range [0, n - 1].

Starting from time t = 0, replace the character at index order[t] in s with '*' at each time step.

A substring is valid if it contains at least one '*'.

A string is active if the total number of valid substrings is greater than or equal to k.

Return the minimum time t at which the string s becomes active. If it is impossible, return -1.



Example 1:

Input: s = "abc", order = [1,0,2], k = 2

Output: 0

Explanation:

t  order[t]  Modified s  Valid Substrings        Count  Active (Count >= k)
0  1         "a*c"       "*", "a*", "*c", "a*c"  4      Yes

The string s becomes active at t = 0. Thus, the answer is 0.


Example 2:

Input: s = "cat", order = [0,2,1], k = 6

Output: 2

Explanation:

t  order[t]  Modified s  Valid Substrings              Count  Active (Count >= k)
0  0         "*at"       "*", "*a", "*at"              3      No
1  2         "*a*"       "*", "*a", "*a*", "a*", "*"   5      No
2  1         "***"       All substrings (contain '*')  6      Yes

The string s becomes active at t = 2. Thus, the answer is 2.


Example 3:

Input: s = "xy", order = [0,1], k = 4

Output: -1

Explanation:

Even after all replacements, it is impossible to obtain k = 4 valid substrings. Thus, the answer is -1.



Constraints:

1 <= n == s.length <= 10^5
order.length == n
0 <= order[i] <= n - 1
s consists of lowercase English letters.
order is a permutation of integers from 0 to n - 1.
1 <= k <= 10^9
"""

from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        
        prev = list(range(-1, n))
        nxt = list(range(1, n + 2))
        count = n * (n + 1) // 2
        if count < k:
            return -1
        
        for t, i in reversed(list(enumerate(order))):
            pi = prev[i]
            ni = nxt[i]
            count -= (i - pi) * (ni - i)
            if count < k:
                return t
            nxt[pi] = ni
            prev[ni] = pi


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minTime("abc", [1, 0, 2], 2))  # 0

    # Example 2
    print(sol.minTime("cat", [0, 2, 1], 6))  # 2

    # Example 3
    print(sol.minTime("xy", [0, 1], 4))  # -1
