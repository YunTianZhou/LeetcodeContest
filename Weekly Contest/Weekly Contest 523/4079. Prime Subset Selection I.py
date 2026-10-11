"""
4079. Prime Subset Selection I - Medium


You are given two integers n and s.

Consider all prime numbers less than or equal to n. Select some of these primes such that:

 - The sum of the selected primes is less than or equal to s.

 - The number of selected primes is maximized.

 - Each prime can be selected at most once.

Return an integer array containing the selected primes in increasing order. If multiple optimal selections exist, return any of them.

If no prime can be selected, return an empty array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.



Example 1:

Input: n = 7, s = 20

Output: [2,3,5,7]

Explanation:

The prime numbers less than or equal to n = 7 are 2, 3, 5, and 7.

The sum of all these primes is 2 + 3 + 5 + 7 = 17, which is less than or equal to s = 20.

Thus, the answer is [2, 3, 5, 7].


Example 2:

Input: n = 15, s = 15

Output: [3,5,7]

Explanation:

The prime numbers less than or equal to n = 15 are 2, 3, 5, 7, 11, and 13.

One possible selection is [3, 5, 7], whose sum is 3 + 5 + 7 = 15.

The four smallest available primes have sum 2 + 3 + 5 + 7 = 17, which exceeds s = 15. Therefore, selecting four or more primes is impossible, and the maximum number of selected primes is three.

Thus, [3, 5, 7] is one possible answer. Other valid answers include [2, 3, 5], [2, 3, 7], and [2, 5, 7].


Example 3:

Input: n = 5, s = 1

Output: []

Explanation:

The smallest prime number is 2, which is greater than s = 1.

Thus, no prime can be selected, so the answer is an empty array.



Constraints:

1 <= n <= 10^6
1 <= s <= 10^9
"""

from bisect import bisect_right
from itertools import accumulate


m = 10 ** 6

is_prime = [True] * (m + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, m + 1) if is_prime[i]]
pref = list(accumulate(primes))


class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        i = bisect_right(primes, n)
        j = bisect_right(pref, s, 0, i)
        return primes[: j]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxPrimes(7, 20))  # [2, 3, 5, 7]

    # Example 2
    print(sol.maxPrimes(15, 15))  # [2, 3, 5]

    # Example 3
    print(sol.maxPrimes(5, 1))  # []
