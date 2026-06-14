"""
3960. Frequency Balance Subarray - Medium


You are given an integer array nums.

Define a frequency balance subarray as follows:

 - If the subarray contains only one distinct value, it is frequency balanced.

 - Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times, and both frequencies occur among the distinct values.

Return an integer denoting the length of the longest frequency balance subarray.



Example 1:

Input: nums = [1,2,2,1,2,3,3,3]

Output: 5

Explanation:

 - The longest frequency balance subarray is [2, 1, 2, 3, 3].

 - The elements that appear most frequently are 2 and 3, both appearing twice.

 - The remaining element 1 appears once, meeting the requirements.


Example 2:

Input: nums = [5,5,5,5]

Output: 4

Explanation:

 - The longest frequency balance subarray is [5, 5, 5, 5].

 - The element that appears most frequently is 5.

 - There are no other elements meeting the requirements.


Example 3:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

Since all elements appear only once, the length of the longest frequency balance subarray is 1.



Constraints:

1 <= nums.length <= 10^3
1 <= nums[i] <= 10^9
"""

from collections import defaultdict


class Solution:
    def getLength(self, nums: list[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            freq = defaultdict(int)
            freq_cnt = defaultdict(int)
            
            mx_freq = 0
            for j in range(i, n):
                x = nums[j]
                freq_cnt[freq[x]] -= 1
                freq[x] += 1
                freq_cnt[freq[x]] += 1
                mx_freq = max(mx_freq, freq[x])

                total = len(freq)
                if total == 1 or (mx_freq % 2 == 0 and 
                                  freq_cnt[mx_freq // 2] == total - freq_cnt[mx_freq] != 0):
                    ans = max(ans, j - i + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.getLength([1, 2, 2, 1, 2, 3, 3, 3]))  # 5

    # Example 2
    print(sol.getLength([5, 5, 5, 5]))  # 4

    # Example 3
    print(sol.getLength([1, 2, 3, 4]))  # 1
