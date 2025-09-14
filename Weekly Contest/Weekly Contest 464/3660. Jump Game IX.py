"""
3660. Jump Game IX - Medium


You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

Jump to index j where j > i is allowed only if nums[j] < nums[i].
Jump to index j where j < i is allowed only if nums[j] > nums[i].

For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.



Example 1:

Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

For i = 0: No jump increases the value.
For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.

Thus, ans = [2, 2, 3].


Example 2:

Input: nums = [2,3,1]

Output: [3,3,3]

Explanation:

For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.

Thus, ans = [3, 3, 3].



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from typing import List
from collections import deque


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [0] * n
        ans[0] = nums[0]
        for i in range(1, n):
            ans[i] = max(ans[i - 1], nums[i])

        dq = deque()
        for i in range(n - 1, -1, -1):
            if not dq or nums[i] < nums[dq[-1]]:
                dq.append(i)
            while dq and ans[i] <= nums[dq[0]]:
                dq.popleft()
            if dq:
                ans[i] = max(ans[i], ans[dq[0]])

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxValue([2, 1, 3]))  # [2, 2, 3]

    # Example 2
    print(sol.maxValue([2, 3, 1]))  # [3, 3, 3]
    