"""
3726. Remove Zeros in Decimal Representation - Easy


You are given a positive integer n.

Return the integer obtained by removing all zeros from the decimal representation of n.



Example 1:

Input: n = 1020030

Output: 123

Explanation:

After removing all zeros from 1020030, we get 123.


Example 2:

Input: n = 1

Output: 1

Explanation:

1 has no zero in its decimal representation. Therefore, the answer is 1.



Constraints:

1 <= n <= 10^15
"""


class Solution:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace("0", ""))
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.removeZeros(1020030))  # 123

    # Example 2
    print(sol.removeZeros(1))  # 1
    