"""
3703. Remove K-Balanced Substrings - Medium


You are given a string s consisting of '(' and ')', and an integer k.

A string is k-balanced if it is exactly k consecutive '(' followed by k consecutive ')', i.e., '(' * k + ')' * k.

For example, if k = 3, k-balanced is "((()))".

You must repeatedly remove all non-overlapping k-balanced substrings from s, and then join the remaining parts. Continue this process until no k-balanced substring exists.

Return the final string after all possible removals.



Example 1:

Input: s = "(())", k = 1

Output: ""

Explanation:

k-balanced substring is "()"

Step  Current s  k-balanced  Result s
1     (())       ([()])      ()
2     ()         ()          Empty

Thus, the final string is "".


Example 2:

Input: s = "(()(", k = 1

Output: "(("

Explanation:

k-balanced substring is "()"

Step  Current s  k-balanced  Result s
1     (()(       ([()](      ((
2     ((         -           ((

Thus, the final string is "((".


Example 3:

Input: s = "((()))()()()", k = 3

Output: "()()()"

Explanation:

k-balanced substring is "((()))"

Step  Current s     k-balanced      Result s
1     ((()))()()()  [((()))]()()()  ()()()
2     ()()()        -               ()()()

Thus, the final string is "()()()".



Constraints:

2 <= s.length <= 10^5
s consists only of '(' and ')'.
1 <= k <= s.length / 2
"""

from typing import List


class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if len(stack) >= 2 and c == ")" and stack[-1][1] >= k and stack[-2][1] >= k:
                stack.pop()
                stack[-1][1] -= k
                
                if stack[-1][1] == 0:
                    stack.pop()

        return "".join(k * c for c, k in stack)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.removeSubstring("(())", 1))  # ""

    # Example 2
    print(sol.removeSubstring("(()(", 1))  # "(("

    # Example 3
    print(sol.removeSubstring("((()))()()()", 3))  # "()()()
    