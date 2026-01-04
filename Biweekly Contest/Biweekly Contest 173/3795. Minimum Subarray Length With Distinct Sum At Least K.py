"""
3795. Minimum Subarray Length With Distinct Sum At Least K - Medium


You are given an integer array nums and an integer k.

Return the minimum length of a subarray whose sum of the distinct values present in that subarray (each value counted once) is at least k. If no such subarray exists, return -1.



Example 1:

Input: nums = [2,2,3,1], k = 4

Output: 2

Explanation:

The subarray [2, 3] has distinct elements {2, 3} whose sum is 2 + 3 = 5, which is ​​​​​​​at least k = 4. Thus, the answer is 2.


Example 2:

Input: nums = [3,2,3,4], k = 5

Output: 2

Explanation:

The subarray [3, 2] has distinct elements {3, 2} whose sum is 3 + 2 = 5, which is ​​​​​​​at least k = 5. Thus, the answer is 2.


Example 3:

Input: nums = [5,5,4], k = 5

Output: 1

Explanation:

The subarray [5] has distinct elements {5} whose sum is 5, which is at least k = 5. Thus, the answer is 1.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^9
"""

from typing import List
from collections import defaultdict
from math import inf


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        sm = j = 0
        ans = inf
        for i, x in enumerate(nums):
            if cnt[x] == 0:
                sm += x
            cnt[x] += 1

            while sm >= k:
                ans = min(ans, i - j + 1)

                y = nums[j]
                cnt[y] -= 1
                if cnt[y] == 0:
                    sm -= y
                j += 1

        return -1 if ans == inf else ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minLength([2, 2, 3, 1], 4))  # 2

    # Example 2
    print(sol.minLength([3, 2, 3, 4], 5))  # 2

    # Example 3
    print(sol.minLength([5, 5, 4], 5))  # 1
    