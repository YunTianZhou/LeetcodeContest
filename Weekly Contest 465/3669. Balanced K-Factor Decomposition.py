"""
3669. Balanced K-Factor Decomposition - Medium


Given two integers n and k, split the number n into exactly k positive integers such that the product of these integers is equal to n.

Return any one split in which the maximum difference between any two numbers is minimized. You may return the result in any order.



Example 1:

Input: n = 100, k = 2

Output: [10,10]

Explanation:

The split [10, 10] yields 10 * 10 = 100 and a max-min difference of 0, which is minimal.


Example 2:

Input: n = 44, k = 3

Output: [2,2,11]

Explanation:

Split [1, 1, 44] yields a difference of 43
Split [1, 2, 22] yields a difference of 21
Split [1, 4, 11] yields a difference of 10
Split [2, 2, 11] yields a difference of 9

Therefore, [2, 2, 11] is the optimal split with the smallest difference 9.



Constraints:

4 <= n <= 10^5
2 <= k <= 5
k is strictly less than the total number of positive divisors of n.
"""

from typing import List
from math import inf


m = 10 ** 5
divisors = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(i, m + 1, i):
        divisors[j].append(i)

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        mn = inf
        ans = []
        factors = [0] * k

        def dfs(n, i):
            if i == k:
                if n == 1:
                    nonlocal mn, ans
                    curr = factors[-1] - factors[0]
                    if curr < mn:
                        mn = curr
                        ans = factors.copy()
                return
            
            start = factors[i - 1] if i else 1
            for factor in divisors[n]:
                if factor >= start:
                    factors[i] = factor
                    dfs(n // factor, i + 1)
        
        dfs(n, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minDifference(100, 2))  # [10, 10]

    # Example 2
    print(sol.minDifference(44, 3))  # [2, 2, 11]
