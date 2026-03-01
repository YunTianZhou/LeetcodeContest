"""
3854. Minimum Operations to Make Array Parity Alternating - Medium


You are given an integer array nums.

An array is called parity alternating if for every index i where 0 <= i < n - 1, nums[i] and nums[i + 1] have different parity (one is even and the other is odd).

In one operation, you may choose any index i and either increase nums[i] by 1 or decrease nums[i] by 1.

Return an integer array answer of length 2 where:

 - answer[0] is the minimum number of operations required to make the array parity alternating.

  - answer[1] is the minimum possible value of max(nums) - min(nums) taken over all arrays that are parity alternating and can be obtained by performing exactly answer[0] operations.

An array of length 1 is considered parity alternating.



Example 1:

Input: nums = [-2,-3,1,4]

Output: [2,6]

Explanation:

Applying the following operations:

 - Increase nums[2] by 1, resulting in nums = [-2, -3, 2, 4].

 - Decrease nums[3] by 1, resulting in nums = [-2, -3, 2, 3].

The resulting array is parity alternating, and the value of max(nums) - min(nums) = 3 - (-3) = 6 is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.


Example 2:

Input: nums = [0,2,-2]

Output: [1,3]

Explanation:

Applying the following operation:

 - Decrease nums[1] by 1, resulting in nums = [0, 1, -2].

The resulting array is parity alternating, and the value of max(nums) - min(nums) = 1 - (-2) = 3 is the minimum possible among all parity alternating arrays obtainable using exactly 1 operation.


Example 3:

Input: nums = [7]

Output: [0,0]

Explanation:

No operations are required. The array is already parity alternating, and the value of max(nums) - min(nums) = 7 - 7 = 0, which is the minimum possible.



Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]
            
        mx = max(nums)
        mn = min(nums)
        
        def solve(parity):
            has_mx = has_mn = 0
            cost = 0
            for x in nums:
                if x % 2 == parity:
                    has_mx = has_mx or x == mx
                    has_mn = has_mn or x == mn
                else:
                    cost += 1
                parity ^= 1

            diff = mx - mn
            if has_mx != has_mn:
                diff -= 1
            elif not has_mx and not has_mn:
                diff -= 2
    
            return [cost, max(1, diff)]

        return min(solve(0), solve(1))


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.makeParityAlternating([-2, -3, 1, 4]))  # [2, 6]

    # Example 2
    print(sol.makeParityAlternating([0, 2, -2]))  # [1, 3]

    # Example 3
    print(sol.makeParityAlternating([7]))  # [0, 0]
