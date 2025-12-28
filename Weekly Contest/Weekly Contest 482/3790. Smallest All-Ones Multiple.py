"""
3790. Smallest All-Ones Multiple - Medium


You are given a positive integer k.

Find the smallest integer n divisible by k that consists of only the digit 1 in its decimal representation (e.g., 1, 11, 111, ...).

Return an integer denoting the number of digits in the decimal representation of n. If no such n exists, return -1.



Example 1:

Input: k = 3

Output: 3

Explanation:

n = 111 because 111 is divisible by 3, but 1 and 11 are not. The length of n = 111 is 3.


Example 2:

Input: k = 7

Output: 6

Explanation:

n = 111111. The length of n = 111111 is 6.


Example 3:

Input: k = 2

Output: -1

Explanation:

There does not exist a valid n that is a multiple of 2.



Constraints:

2 <= k <= 10^5
"""


class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        x = 1
        for d in range(1, k + 1):
            if x == 0:
                return d
            x = (x * 10 + 1) % k
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minAllOneMultiple(3))  # 3

    # Example 2
    print(sol.minAllOneMultiple(7))  # 6

    # Example 3
    print(sol.minAllOneMultiple(2))  # -1
    