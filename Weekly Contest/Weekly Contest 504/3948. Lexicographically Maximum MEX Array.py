"""
3948. Lexicographically Maximum MEX Array - Hard


You are given an integer array nums.

You want to construct an array result by repeatedly performing the following operation until nums becomes empty:

 - Choose an integer k such that 1 <= k <= len(nums).

 - Compute the MEX of the first k elements of nums.

 - Append this MEX to result.

 - Remove the first k elements from nums.

Return the lexicographically maximum array result that can be obtained after performing the operations.

The MEX of an array is the smallest non-negative integer not present in the array.

An array a is lexicographically greater than an array b if in the first position where a and b differ, array a has an element that is greater than the corresponding element in b. If the first min(a.length, b.length) elements do not differ, then the longer array is the lexicographically greater one.



Example 1:

Input: nums = [0,1,0]

Output: [2,1]

Explanation:

 - Take the first k = 2 elements [0, 1] which has MEX = 2. Current result = [2].

 - Remaining array [0] has MEX = 1. Thus, the final result = [2, 1].


Example 2:

Input: nums = [1,0,2]

Output: [3]

Explanation:

 - Take the first k = 3 elements [1, 0, 2] which has MEX = 3.

 - nums is now empty. Thus, the final result = [3].


Example 3:

Input: nums = [3,1]

Output: [0,0]

Explanation:

 - Take k = 1, first element [3] has MEX = 0. Current result = [0].

 - Remaining array [1] has MEX = 0. Thus, the final result = [0, 0].



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""

from collections import defaultdict


class Solution:
    def maximumMEX(self, nums: list[int]) -> list[int]:
        n = len(nums)

        mp = defaultdict(list)
        for i in range(n - 1, -1, -1):
            mp[nums[i]].append(i)

        res = []
        i = 0
        while i < n:
            j = i
            x = 0
            while mp[x]:
                j = max(j, mp[x][-1])
                x += 1

            for k in range(i, j + 1):
                mp[nums[k]].pop()
            
            res.append(x)
            i = j + 1

        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumMEX([0, 1, 0]))  # [2, 1]

    # Example 2
    print(sol.maximumMEX([1, 0, 2]))  # [3]

    # Example 3
    print(sol.maximumMEX([3, 1]))  # [0, 0]
