"""
3748. Count Stable Subarrays - Hard


You are given an integer array nums.

A subarray of nums is called stable if it contains no inversions, i.e., there is no pair of indices i < j such that nums[i] > nums[j].

You are also given a 2D integer array queries of length q, where each queries[i] = [li, ri] represents a query. For each query [li, ri], compute the number of stable subarrays that lie entirely within the segment nums[li..ri].

Return an integer array ans of length q, where ans[i] is the answer to the ith query.​​​​​​​​​​​​​​

Note:

 - A single element subarray is considered stable.



Example 1:

Input: nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]

Output: [2,3,4]

Explanation:

 - For queries[0] = [0, 1], the subarray is [nums[0], nums[1]] = [3, 1].
    - The stable subarrays are [3] and [1]. The total number of stable subarrays is 2.

 - For queries[1] = [1, 2], the subarray is [nums[1], nums[2]] = [1, 2].
    - The stable subarrays are [1], [2], and [1, 2]. The total number of stable subarrays is 3.

 - For queries[2] = [0, 2], the subarray is [nums[0], nums[1], nums[2]] = [3, 1, 2].
    - The stable subarrays are [3], [1], [2], and [1, 2]. The total number of stable subarrays is 4.

Thus, ans = [2, 3, 4].


Example 2:

Input: nums = [2,2], queries = [[0,1],[0,0]]

Output: [3,1]

Explanation:

 - For queries[0] = [0, 1], the subarray is [nums[0], nums[1]] = [2, 2].
    - The stable subarrays are [2], [2], and [2, 2]. The total number of stable subarrays is 3.

 - For queries[1] = [0, 0], the subarray is [nums[0]] = [2].
    - The stable subarray is [2]. The total number of stable subarrays is 1.

Thus, ans = [3, 1].



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= queries.length <= 10^5
queries[i] = [li, ri]
0 <= li <= ri <= nums.length - 1
"""

from typing import List


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        f = [0] * (n + 1)
        s = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + 1 if i > 0 and nums[i - 1] <= nums[i] else 1
            s[i + 1] = s[i] + f[i + 1]

        g = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            g[i + 1] = g[i + 2] + 1 if i + 1 < n and nums[i] <= nums[i + 1] else 1

        return [s[r + 1] - s[l] - (f[l + 1] - 1) * min(r - l + 1, g[l + 1]) for l, r in queries]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countStableSubarrays([3, 1, 2], [[0, 1], [1, 2], [0, 2]]))  # [2, 3, 4]

    # Example 2
    print(sol.countStableSubarrays([2, 2], [[0, 1], [0, 0]]))  # [3, 1]
    