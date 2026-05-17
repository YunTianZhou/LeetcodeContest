"""
3932. Count K-th Roots in a Range - Medium


You are given three integers l, r, and k.

An integer y is said to be a perfect kth power if there exists an integer x such that y = x^k.

Return the number of integers y in the range [l, r] (inclusive) that are perfect kth powers.



Example 1:

Input: l = 1, r = 9, k = 3

Output: 2

Explanation:

The perfect cubes in the range [1, 9] are:

 - 1 = 13
 - 8 = 23

Hence, the answer is 2.


Example 2:

Input: l = 8, r = 30, k = 2

Output: 3

Explanation:

The perfect squares in the range [8, 30] are:

 - 9 = 32
 - 16 = 42
 - 25 = 52

Hence, the answer is 3.



Constraints:

0 <= l <= r <= 10^9
1 <= k <= 30
"""


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def f(x):
            if x < 0:
                return 0
            
            res = int(x ** (1 / k))
            if (res + 1) ** k <= x:
                res += 1
            return res + 1

        return f(r) - f(l - 1)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countKthRoots(1, 9, 3))  # 2

    # Example 2
    print(sol.countKthRoots(8, 30, 2))  # 3
