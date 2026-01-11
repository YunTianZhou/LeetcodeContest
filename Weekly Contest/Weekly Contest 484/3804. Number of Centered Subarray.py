"""
3804. Number of Centered Subarrays - Medium


You are given an integer array nums.

A subarray of nums is called centered if the sum of its elements is equal to at least one element within that same subarray.

Return the number of centered subarrays of nums.



Example 1:

Input: nums = [-1,1,0]

Output: 5

Explanation:

 - All single-element subarrays ([-1], [1], [0]) are centered.

 - The subarray [1, 0] has a sum of 1, which is present in the subarray.

 - The subarray [-1, 1, 0] has a sum of 0, which is present in the subarray.

 - Thus, the answer is 5.


Example 2:

Input: nums = [2,-3]

Output: 2

Explanation:

Only single-element subarrays ([2], [-3]) are centered.



Constraints:

1 <= nums.length <= 500
-10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            sm = 0
            st = set()
            for j in range(i, n):
                sm += nums[j]
                st.add(nums[j])
                if sm in st:
                    ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.centeredSubarrays([-1, 1, 0]))  # 5

    # Example 2
    print(sol.centeredSubarrays([2, -3]))  # 2
    