"""
3859. Count Subarrays With K Distinct Integers - Hard


You are given an integer array nums and two integers k and m.

Return an integer denoting the count of subarrays of nums such that:

 - The subarray contains exactly k distinct integers.

 - Within the subarray, each distinct integer appears at least m times.



Example 1:

Input: nums = [1,2,1,2,2], k = 2, m = 2

Output: 2

Explanation:

The possible subarrays with k = 2 distinct integers, each appearing at least m = 2 times are:

Subarray         Distinct numbers  Frequency
[1, 2, 1, 2]     {1, 2} → 2        {1: 2, 2: 2}
[1, 2, 1, 2, 2]  {1, 2} → 2        {1: 2, 2: 3}

Thus, the answer is 2.


Example 2:

Input: nums = [3,1,2,4], k = 2, m = 1

Output: 3

Explanation:

The possible subarrays with k = 2 distinct integers, each appearing at least m = 1 times are:

Subarray  Distinct numbers  Frequency
[3, 1]    {3, 1} → 2        {3: 1, 1: 1}
[1, 2]    {1, 2} → 2        {1: 1, 2: 1}
[2, 4]    {2, 4} → 2        {2: 1, 4: 1}

Thus, the answer is 3.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k, m <= nums.length
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        def solve(limit):
            cnt = {}
            ans = j = cnt_m = 0
            
            for i, x in enumerate(nums):
                cnt[x] = cnt.get(x, 0) + 1
                if cnt[x] == m:
                    cnt_m += 1

                while len(cnt) >= limit and cnt_m >= k:
                    y = nums[j]
                    if cnt[y] == m:
                        cnt_m -= 1
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        del cnt[y]
                    j += 1
                
                ans += i - j
            
            return ans
        
        return solve(k + 1) - solve(k)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countSubarrays([1, 2, 1, 2, 2], 2, 2))  # 2

    # Example 2
    print(sol.countSubarrays([3, 1, 2, 4], 2, 1))  # 3
