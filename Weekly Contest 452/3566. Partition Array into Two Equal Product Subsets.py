"""
3566. Partition Array into Two Equal Product Subsets - Medium


You are given an integer array nums containing distinct positive integers and an integer target.

Determine if you can partition nums into two non-empty disjoint subsets, with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target.

Return true if such a partition exists and false otherwise.

A subset of an array is a selection of elements of the array.
 


Example 1:

Input: nums = [3,1,6,8,4], target = 24

Output: true

Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.


Example 2:

Input: nums = [2,5,3,7], target = 15

Output: false

Explanation: There is no way to partition nums into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.



Constraints:

3 <= nums.length <= 12
1 <= target <= 10^15
1 <= nums[i] <= 100
All elements of nums are distinct.
"""

from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
            
        product = 1
        for x in nums:
            product *= x
            if product > target * target:
                return False
            
        if product != target * target:
            return False

        def dfs(i, curr):
            if i == n:
                return curr == 1
            return dfs(i + 1, curr) or (curr % nums[i] == 0 and dfs(i + 1, curr // nums[i]))

        return dfs(0, target)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.checkEqualPartitions([3, 1, 6, 8, 4], 24))  # True

    # Example 2
    print(sol.checkEqualPartitions([2, 5, 3, 7], 15))     # False

    # Additional test cases
    print(sol.checkEqualPartitions([2, 3, 4, 6], 12))     # True: [2,6] and [3,4]
    print(sol.checkEqualPartitions([10, 2, 5, 3], 30))    # False
    print(sol.checkEqualPartitions([2, 3, 5], 30))        # False
