"""
3747. Count Distinct Integers After Removing Zeros - Medium


You are given a positive integer n.

For every integer x from 1 to n, we write down the integer obtained by removing all zeros from the decimal representation of x.

Return an integer denoting the number of distinct integers written down.



Example 1:

Input: n = 10

Output: 9

Explanation:

The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).


Example 2:

Input: n = 3

Output: 3

Explanation:

The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).



Constraints:

1 <= n <= 10^15
"""


class Solution:
    def countDistinct(self, n: int) -> int:
        ans = base = 1
        while n:
            n, x = divmod(n, 10)
            if x == 0:
                ans = 0
            else:
                ans += (x - 1) * base
            base *= 9
        
        ans += (base - 9) // 8
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countDistinct(10))  # 9

    # Example 2
    print(sol.countDistinct(3))  # 3
    