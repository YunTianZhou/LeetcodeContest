"""
3920. Maximize Fixed Points After Deletions - Hard


You are given an integer array nums.

A position i is called a fixed point if nums[i] == i.

You are allowed to delete any number of elements (including zero) from the array. After each deletion, the remaining elements shift left, and indices are reassigned starting from 0.

Return an integer denoting the maximum number of fixed points that can be achieved after performing any number of deletions.



Example 1:

Input: nums = [0,2,1]

Output: 2

Explanation:

 - Now, nums[0] = 0 and nums[1] = 1, so both indices are fixed points.

 - Delete nums[1] = 2. The array becomes [0, 1].

 - Thus, the answer is 2.


Example 2:

Input: nums = [3,1,2]

Output: 2

Explanation:

 - Do not delete any elements. The array remains [3, 1, 2].

 - Here, nums[1] = 1 and nums[2] = 2, so these indices are fixed points.

 - Thus, the answer is 2.


Example 3:

Input: nums = [1,0,1,2]

Output: 3

Explanation:

 - Delete nums[0] = 1. The array becomes [0, 1, 2].

 - Now, nums[0] = 0, nums[1] = 1, and nums[2] = 2, so all indices are fixed points.

 - Thus, the answer is 3.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""

from bisect import bisect_right


class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        pts = [(x, i - x) for i, x in enumerate(nums) if i >= x]
        pts.sort(key=lambda x: (x[0],-x[1]))

        a = []
        for _, x in pts:
            i = bisect_right(a, x)
            if i < len(a):
                a[i] = x
            else:
                a.append(x)
        
        return len(a)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxFixedPoints([0, 2, 1]))  # 2

    # Example 2
    print(sol.maxFixedPoints([3, 1, 2]))  # 2

    # Example 3
    print(sol.maxFixedPoints([1, 0, 1, 2]))  # 3
