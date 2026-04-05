"""
3892. Minimum Operations to Achieve At Least K Peaks - Hard


You are given a circular integer array nums of length n.

An index i is a peak if its value is strictly greater than its neighbors:

 - The previous neighbor of i is nums[i - 1] if i > 0, otherwise nums[n - 1].

 - The next neighbor of i is nums[i + 1] if i < n - 1, otherwise nums[0].

You are allowed to perform the following operation any number of times:

 - Choose any index i and increase nums[i] by 1.

Return an integer denoting the minimum number of operations required to make the array contain at least k peaks. If it is impossible, return -1.



Example 1:

Input: nums = [2,1,2], k = 1

Output: 1

Explanation:

 - To achieve at least k = 1 peak, we can increase nums[2] = 2 to 3.

 - After this operation, nums[2] = 3 is strictly greater than its neighbors nums[0] = 2 and nums[1] = 1.

 - Therefore, the minimum number of operations required is 1.


Example 2:

Input: nums = [4,5,3,6], k = 2

Output: 0

Explanation:

 - The array already contains at least k = 2 peaks with zero operations.

 - Index 1: nums[1] = 5 is strictly greater than its neighbors nums[0] = 4 and nums[2] = 3.

 - Index 3: nums[3] = 6 is strictly greater than its neighbors nums[2] = 3 and nums[0] = 4.

 - Therefore, the minimum number of operations required is 0.


Example 3:

Input: nums = [3,7,3], k = 2

Output: -1

Explanation:

It is impossible to have at least k = 2 peaks in this array. Therefore, the answer is -1.



Constraints:

2 <= n == nums.length <= 5000
-10^5 <= nums[i] <= 10^5
0 <= k <= n
"""

from heapq import heapify, heappop, heappush


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k > n // 2:
            return -1

        left = [n - 1] + list(range(n - 1))
        right = list(range(1, n)) + [0]

        cost = [0] * n
        for i, x in enumerate(nums):
            cost[i] = max(0, max(nums[i - 1], nums[(i + 1) % n]) - x + 1)

        hp = [(x, i) for i, x in enumerate(cost)]
        vis = [False] * n
        heapify(hp)
        
        ans = 0
        while k > 0:
            x, i = heappop(hp)
            if vis[i]:
                continue
            ans += x
            k -= 1

            l = left[i]
            r = right[i]

            cost[i] = cost[l] + cost[r] - x
            heappush(hp, (cost[i], i))

            vis[l] = True
            vis[r] = True
            left[i] = left[l]
            right[i] = right[r]
            left[right[i]] = i
            right[left[i]] = i

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minOperations([2, 1, 2], 1))  # 1

    # Example 2
    print(sol.minOperations([4, 5, 3, 6], 2))  # 0

    # Example 3
    print(sol.minOperations([3, 7, 3], 2))  # -1
