"""
3962. Maximum Subarray Sum After at Most K Swaps - Hard


You are given an integer array nums and an integer k.

You are allowed to perform at most k swap operations on the array.

In one swap operation, you may choose any two indices i and j and swap nums[i] and nums[j].

Return an integer denoting the maximum possible subarray sum after performing the swaps.



Example 1:

Input: nums = [1,-1,0,2], k = 1

Output: 3

Explanation:

 - We can swap on indices 1 and 3, resulting in the array [1, 2, 0, -1].

 - The subarray [1, 2] has a sum of 3, which is the maximum possible subarray sum after at most k = 1 swap.


Example 2:

Input: nums = [4,3,2,4], k = 2

Output: 13

Explanation:

The maximum possible subarray sum after at most k = 2 swaps is the sum of the entire array, which is 13.


Example 3:

Input: nums = [-1,-2], k = 0

Output: -1

Explanation:

 - k = 0 swaps are allowed.

 - The possible subarrays are [-1], [-2], and [-1, -2], with sums -1, -2, and -3 respectively.

 - Among these sums, the maximum is -1.



Constraints:

1 <= nums.length <= 1500
-10^5 <= nums[i] <= 10^5
0 <= k <= nums.length
"""

from heapq import heappop, heappush


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        cnt_pos = sum(x > 0 for x in nums)
        if cnt_pos == 0:
            return max(nums)
        elif cnt_pos <= k + 1:
            return sum(x for x in nums if x > 0)

        sorted_nums = sorted(((x, i) for i, x in enumerate(nums)), reverse=True)

        val = [0] * n
        rank = [0] * n
        for i, (x, j) in enumerate(sorted_nums):
            val[i] = x
            rank[j] = i
        
        ans = 0
        for l in range(n):
            used = [False] * n
            cand = []
            selected = []

            op = k
            i = sm = 0
            for r in range(l, n):
                rnk = rank[r]

                if not used[rnk]:
                    used[rnk] = True
                    if selected and rnk > selected[0]:
                        link = heappop(selected)
                        sm += val[link]
                        heappush(selected, rnk)
                        heappush(cand, -link)
                    else:
                        sm += val[rnk]
                        heappush(cand, -rnk)
                else:
                    link = heappop(selected)
                    sm += val[link]
                    op += 1
                    heappush(cand, -rnk)
                    heappush(cand, -link)

                while i < n and op > 0:
                    if not used[i]:
                        if cand and -cand[0] > i:
                            j = -heappop(cand)
                            used[i] = True
                            sm += val[i] - val[j]
                            op -= 1
                            heappush(selected, j)
                        else:
                            break
                    i += 1

                ans = max(ans, sm)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxSum([1, -1, 0, 2], 1))  # 3

    # Example 2
    print(sol.maxSum([4, 3, 2, 4], 2))  # 13

    # Example 3
    print(sol.maxSum([-1, -2], 0))  # -1
