"""
3890. Integers With Multiple Sum of Two Cubes - Medium


You are given an integer n.

An integer x is considered good if there exist at least two distinct pairs (a, b) such that:

 - a and b are positive integers.

 - a <= b

 - x = a^3 + b^3

Return an array containing all good integers less than or equal to n, sorted in ascending order.



Example 1:

Input: n = 4104

Output: [1729,4104]

Explanation:

Among integers less than or equal to 4104, the good integers are:

 - 1729: 13 + 123 = 1729 and 93 + 103 = 1729.
 - 4104: 23 + 163 = 4104 and 93 + 153 = 4104.

Thus, the answer is [1729, 4104].


Example 2:

Input: n = 578

Output: []

Explanation:

There are no good integers less than or equal to 578, so the answer is an empty array.



Constraints:

1 <= n <= 10^9
"""

from collections import defaultdict
from math import cbrt
from bisect import bisect_right


m = 10 ** 9
k = int(cbrt(m))

cnt = defaultdict(int)
good = []
for a in range(1, k + 1):
    for b in range(a, k + 1):
        x = a ** 3 + b ** 3
        if x > m:
            break
        cnt[x] += 1
        if cnt[x] == 2:
            good.append(x)
good.sort()


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        return good[: bisect_right(good, n)]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.findGoodIntegers(4104))  # [1729, 4104]

    # Example 2
    print(sol.findGoodIntegers(578))  # []
