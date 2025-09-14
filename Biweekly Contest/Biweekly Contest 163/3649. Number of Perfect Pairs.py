"""
3649. Number of Perfect Pairs - Medium


You are given an integer array nums.

A pair of indices (i, j) is called perfect if the following conditions are satisfied:

i < j
Let a = nums[i], b = nums[j]. Then:
    min(|a - b|, |a + b|) <= min(|a|, |b|)
    max(|a - b|, |a + b|) >= max(|a|, |b|)

Return the number of distinct perfect pairs.

Note: The absolute value |x| refers to the non-negative value of x.



Example 1:

Input: nums = [0,1,2,3]

Output: 2

Explanation:

There are 2 perfect pairs:

(i, j)  (a, b)  min(|a - b|, |a + b|)      min(|a|, |b|)  max(|a - b|, |a + b|)      max(|a|, |b|)
(1, 2)  (1, 2)  min(|1 - 2|, |1 + 2|) = 1  1              max(|1 - 2|, |1 + 2|) = 3  2
(2, 3)  (2, 3)  min(|2 - 3|, |2 + 3|) = 1  2              max(|2 - 3|, |2 + 3|) = 5  3


Example 2:

Input: nums = [-3,2,-1,4]

Output: 4

Explanation:

There are 4 perfect pairs:

(i, j)  (a, b)   min(|a - b|, |a + b|)            min(|a|, |b|)  max(|a - b|, |a + b|)            max(|a|, |b|)
(0, 1)  (-3, 2)  min(|-3 - 2|, |-3 + 2|) = 1      2              max(|-3 - 2|, |-3 + 2|) = 5      3
(0, 3)  (-3, 4)  min(|-3 - 4|, |-3 + 4|) = 1      3              max(|-3 - 4|, |-3 + 4|) = 7      4
(1, 2)  (2, -1)  min(|2 - (-1)|, |2 + (-1)|) = 1  1              max(|2 - (-1)|, |2 + (-1)|) = 3  2
(1, 3)  (2, 4)   min(|2 - 4|, |2 + 4|) = 2        2              max(|2 - 4|, |2 + 4|) = 6        4


Example 3:

Input: nums = [1,10,100,1000]

Output: 0

Explanation:

There are no perfect pairs. Thus, the answer is 0.



Constraints:

2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(sorted(map(abs, nums)))

        ans = 0
        j = 0
        for i in range(n):
            while nums[j] * 2 < nums[i]:
                j += 1
            ans += i - j
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.perfectPairs([0, 1, 2, 3]))  # 2

    # Example 2
    print(sol.perfectPairs([-3, 2, -1, 4]))  # 4

    # Example 3
    print(sol.perfectPairs([1, 10, 100, 1000]))  # 0
