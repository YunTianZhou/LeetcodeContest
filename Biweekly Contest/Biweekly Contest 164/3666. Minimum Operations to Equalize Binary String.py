"""
3666. Minimum Operations to Equalize Binary String - Hard


You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.



Example 1:

Input: s = "110", k = 1

Output: 1

Explanation:

There is one '0' in s.

Since k = 1, we can flip it directly in one operation.


Example 2:

Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:

Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".

Thus, the minimum number of operations is 2.


Example 3:

Input: s = "101", k = 2

Output: -1

Explanation:

Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.



Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.
1 <= k <= s.length
"""

from math import ceil, inf


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count("0")

        if z == 0:
            return 0
        if k == n:
            return 1 if z == n else -1

        ans = inf
        if z % 2 == 0:
            m = max(ceil(z / k), ceil(z / (n - k)))
            ans = min(ans, m + (m % 2))
        if z % 2 == k % 2:
            m = max(ceil(z / k), ceil((n - z) / (n - k)))
            ans = min(ans, m | 1)
        
        return -1 if ans == inf else ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations("110", 1))  # 1

    # Example 2
    print(sol.minOperations("0101", 3))  # 2

    # Example 3
    print(sol.minOperations("101", 2))  # -1
    