"""
3779. Minimum Number of Operations to Have Distinct Elements - Medium


You are given an integer array nums.

In one operation, you remove the first three elements of the current array. If there are fewer than three elements remaining, all remaining elements are removed.

Repeat this operation until the array is empty or contains no duplicate values.

Return an integer denoting the number of operations required.



Example 1:

Input: nums = [3,8,3,6,5,8]

Output: 1

Explanation:

In the first operation, we remove the first three elements. The remaining elements [6, 5, 8] are all distinct, so we stop. Only one operation is needed.


Example 2:

Input: nums = [2,2]

Output: 1

Explanation:

After one operation, the array becomes empty, which meets the stopping condition.


Example 3:

Input: nums = [4,3,5,1,2]

Output: 0

Explanation:

All elements in the array are distinct, therefore no operations are needed.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        st = set()
        for i in range(n - 1, -1, -1):
            if nums[i] in st:
                return i // 3 + 1
            st.add(nums[i])

        return 0


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([3, 8, 3, 6, 5, 8]))  # 1

    # Example 2
    print(sol.minOperations([2, 2]))  # 1

    # Example 3
    print(sol.minOperations([4, 3, 5, 1, 2]))  # 0
