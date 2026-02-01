"""
3830. Longest Alternating Subarray After Removing At Most One Element - Hard


You are given an integer array nums.

A subarray nums[l..r] is alternating if one of the following holds:

 - nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...

 - nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...

In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between strictly greater and strictly smaller.

You can remove at most one element from nums. Then, you select an alternating subarray from nums.

Return an integer denoting the maximum length of the alternating subarray you can select.

A subarray of length 1 is considered alternating.



Example 1:

Input: nums = [2,1,3,2]

Output: 4

Explanation:

 - Choose not to remove elements.

 - Select the entire array [2, 1, 3, 2], which is alternating because 2 > 1 < 3 > 2.


Example 2:

Input: nums = [3,2,1,2,3,2,1]

Output: 4

Explanation:

 - Choose to remove nums[3] i.e., [3, 2, 1, 2, 3, 2, 1]. The array becomes [3, 2, 1, 3, 2, 1].

 - Select the subarray [3, 2, 1, 3, 2, 1].


Example 3:

Input: nums = [100000,100000]

Output: 1

Explanation:

 - Choose not to remove elements.

 - Select the subarray [100000, 100000].



Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List
from itertools import pairwise


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        inc = dec = 1
        del_inc = del_dec = 1
        ans = 0

        for x, y in pairwise(nums):
            if x < y:
                del_inc = del_dec + 1
                del_dec = dec
                inc = dec + 1
                dec = 1
            elif x > y:
                del_dec = del_inc + 1
                del_inc = inc
                dec = inc + 1
                inc = 1
            else:
                del_inc = inc
                del_dec = dec
                inc = 1
                dec = 1

            ans = max(ans, del_inc, del_dec)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestAlternating([2, 1, 3, 2]))  # 4

    # Example 2
    print(sol.longestAlternating([3, 2, 1, 2, 3, 2, 1]))  # 4

    # Example 3
    print(sol.longestAlternating([100000, 100000]))  # 1
