"""
4059. Lexicographically Largest Power Array - Hard


You are given an integer array nums of length n. You may rearrange its elements to form any permutation perm.

Define an array power of length 15. For each 0 <= i < 15, power[i] is the largest integer j, where 0 <= j <= n, such that the first j elements of perm all have the (14 - i)th bit set.

Bit positions are indexed from right to left, starting with the 0th bit.

Return the lexicographically largest possible power array.



Example 1:

Input: nums = [7,5]

Output: [0,0,0,0,0,0,0,0,0,0,0,0,2,1,2]

Explanation:

Choose perm = [7, 5].

 - Both elements have bit 2 set, so power[12] = 2.

 - The first element has bit 1 set, but the second does not, so power[13] = 1.

 - Both elements have bit 0 set, so power[14] = 2.

All higher bits are unset in the first element, so the remaining entries are 0.


Example 2:

Input: nums = [3,1,7]

Output: [0,0,0,0,0,0,0,0,0,0,0,0,1,2,3]

Explanation:

Choose perm = [7, 3, 1].

 - The first element has bit 2 set, but the second does not, so power[12] = 1.

 - The first two elements have bit 1 set, but the third does not, so power[13] = 2.

 - All three elements have bit 0 set, so power[14] = 3.

All higher bits are unset in the first element, so the remaining entries are 0.



Constraints:

1 <= nums.length <= 5 * 10^4
0 <= nums[i] < 2^15
"""


class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        ans = [0] * 15

        groups = [nums]
        for k in range(max(nums).bit_length() - 1, -1, -1):
            i = 0
            while i < len(groups) and all(x >> k & 1 for x in groups[i]):
                ans[k] += len(groups[i])
                i += 1
            
            if i < len(groups):
                left = [x for x in groups[i] if x >> k & 1]
                right = [x for x in groups[i] if (x >> k & 1) == 0]
                groups[i] = left
                groups.insert(i + 1, right)
                ans[k] += len(left)
        
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.largestPower([7, 5]))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2]

    # Example 2
    print(sol.largestPower([3, 1, 7]))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
