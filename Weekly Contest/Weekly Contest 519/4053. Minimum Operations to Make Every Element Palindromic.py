"""
4053. Minimum Operations to Make Every Element Palindromic - Medium


You are given an integer array nums.

In one operation, you may choose an index i and either increment or decrement nums[i] by 2.

Return the minimum number of operations required to make every element in nums a positive palindrome. Different elements may be changed into different palindromic integers.



Example 1:

Input: nums = [10,12,14,16]

Output: 9

Explanation:

One optimal sequence of operations is:

 - Decrement nums[0] by 2 once to change it from 10 to 8.

 - Decrement nums[1] by 2 twice to change it from 12 to 8.

 - Decrement nums[2] by 2 three times to change it from 14 to 8.

 - Increment nums[3] by 2 three times to change it from 16 to 22.

After 1 + 2 + 3 + 3 = 9 operations, nums = [8, 8, 8, 22], and every element is a positive palindromic integer.

It can be shown that fewer than 9 operations cannot achieve this.


Example 2:

Input: nums = [9,10,11,10]

Output: 2

Explanation:

Decrement nums[1] and nums[3] by 2 once each.

After 2 operations, nums = [9, 8, 11, 8], and every element is a positive palindromic integer.

At least one operation is needed for each of these two elements, so the minimum number of operations is 2.


Example 3:

Input: nums = [125]

Output: 2

Explanation:

Decrement nums[0] by 2 twice to change it from 125 to 121, which is a positive palindromic integer.

A single operation would change it to 123 or 127, neither of which is palindromic. Thus, the minimum number of operations is 2.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from bisect import bisect_right


m = 10
palindroms = [[], []]
for d in range(1, m + 1):
    for k in range(10 ** ((d - 1) // 2), 10 ** ((d + 1) // 2)):
        s = str(k)
        p = int(s + s[: d // 2][::-1])
        palindroms[p % 2].append(p)


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for x in nums:
            a = palindroms[x % 2]
            i = bisect_right(a, x)
            ans += min(x - a[i - 1], a[i] - x) // 2
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([10, 12, 14, 16]))  # 9

    # Example 2
    print(sol.minOperations([9, 10, 11, 10]))  # 2

    # Example 3
    print(sol.minOperations([125]))  # 2
