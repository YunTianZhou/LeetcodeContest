"""
4081. Prime Subset Selection II - Hard


You are given two integers n and s.

Consider all prime numbers less than or equal to n. Select a subset of these primes such that:

 - Each prime can be selected at most once.

 - The sum of the selected primes is as large as possible while remaining less than or equal to s.

 - Among subsets with the maximum sum, select one containing the fewest primes.

 - If multiple subsets remain tied, select the one whose elements, written in increasing order, form the lexicographically smallest array.

Return an integer array containing the selected primes in increasing order. If no valid non-empty subset exists, return an empty array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

A subset is a selection of zero or more distinct elements from a set.

An array a is lexicographically smaller than an array b if, at the first position where they differ, a has a smaller element. If all elements up to the length of the shorter array are equal, the shorter array is lexicographically smaller.



Example 1:

Input: n = 7, s = 20

Output: [2, 3, 5, 7]

Explanation:

The prime numbers less than or equal to n = 7 are 2, 3, 5, and 7.

The sum of all these primes is 2 + 3 + 5 + 7 = 17, which is less than or equal to s = 20.

Thus, the answer is [2, 3, 5, 7].


Example 2:

Input: n = 15, s = 18

Output: [5,13]

Explanation:

The prime numbers less than or equal to 15 are 2, 3, 5, 7, 11, and 13.

The subsets with sum 18 are [5, 13], [7, 11], [2, 3, 13], and [2, 5, 11]. Since this sum equals s, it is the maximum possible sum.

Among these subsets, [5, 13] and [7, 11] contain the fewest primes: two.

Between these two subsets, [5, 13] is lexicographically smaller because its first element, 5, is smaller than 7. Thus, the answer is [5, 13].


Example 3:

Input: n = 5, s = 1

Output: []

Explanation:

The smallest prime number is 2, which is greater than s = 1.

Thus, no prime can be selected, so the answer is an empty array.



Constraints:

1 <= n <= 1000
1 <= s <= 1000
"""

from bisect import bisect_right
from math import inf


m = 1000

is_prime = [True] * (m + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, m + 1) if is_prime[i]]


class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        k = bisect_right(primes, n)
        
        dp = [1] + [inf] * s
        last = [[] for _ in range(s + 1)]

        for i in range(k - 1, -1, -1):
            p = primes[i]
            for j in range(s, p - 1, -1):
                x = dp[j - p] + 1
                if x <= dp[j]:
                    dp[j] = x
                    last[j].append(p)

        mx = s
        while dp[mx] == inf:
            mx -= 1

        ans = []
        x = 0
        while mx > 0:
            j = -1
            while last[mx][j] <= x:
                j -= 1
            
            x = last[mx][j]
            ans.append(x)
            mx -= x

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxPrimeSubset(7, 20))  # [2, 3, 5, 7]

    # Example 2
    print(sol.maxPrimeSubset(15, 18))  # [5, 13]

    # Example 3
    print(sol.maxPrimeSubset(5, 1))  # []
