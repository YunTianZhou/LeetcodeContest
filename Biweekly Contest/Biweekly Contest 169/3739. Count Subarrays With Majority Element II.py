"""
3737. Count Subarrays With Majority Element II - Hard


You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.



Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

 - nums[1..1] = [2]

 - nums[2..2] = [2]

 - nums[1..2] = [2,2]

 - nums[0..2] = [1,2,2]

 - nums[1..3] = [2,2,3]

So there are 5 such subarrays.


Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

All 10 subarrays have 1 as the majority element.


Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= target <= 10^9
"""

from typing import List
from collections import defaultdict


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1

        ans = sm = curr = 0
        for x in nums:
            if x == target:
                curr += cnt[sm]
                sm += 1
            else:
                sm -= 1
                curr -= cnt[sm]
            
            ans += curr
            cnt[sm] += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countMajoritySubarrays([1, 2, 2, 3], 2))  # 5

    # Example 2
    print(sol.countMajoritySubarrays([1, 1, 1, 1], 1))  # 10

    # Example 3
    print(sol.countMajoritySubarrays([1, 2, 3], 4))  # 0
    