"""
3911. K-th Smallest Remaining Even Integer in Subarray Queries - Hard


You are given an integer array nums where nums is strictly increasing.

You are also given a 2D integer array queries, where queries[i] = [li, ri, ki].

For each query [li, ri, ki]:

 - Consider the subarray nums[li..ri]

 - From the infinite sequence of all positive even integers: 2, 4, 6, 8, 10, 12, 14, ...

 - Remove all elements that appear in the subarray nums[li..ri].

 - Find the kith smallest integer remaining in the sequence after the removals.

Return an integer array ans, where ans[i] is the result for the ith query.



Example 1:

Input: nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]

Output: [2,6,6]

Explanation:

i  queries[i]  nums[li..ri]  Removed  Remaining     k  ans[i]
0  [0, 2, 1]   [1, 4, 7]     [4]      2, 6, 8, ...  1  2
1  [1, 1, 2]   [4]           [4]      2, 6, 8, ...  2  6
2  [0, 0, 3]   [1]           []       2, 4, 6, ...  3  6

Thus, ans = [2, 6, 6].


Example 2:

Input: nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]

Output: [6,2,12]

Explanation:

i  queries[i]  nums[li..ri]  Removed  Remaining          k  ans[i]
0  [0, 1, 2]   [2, 5]        [2]      4, 6, 8, ...       2  6
1  [1, 2, 1]   [5, 8]        [8]      2, 4, 6, ...       1  2
2  [0, 2, 4]   [2, 5, 8]     [2, 8]   4, 6, 10, 12, ...  4  12

Thus, ans = [6, 2, 12].


Example 3:

Input: nums = [3,6], queries = [[0,1,1],[1,1,3]]

Output: [2,8]

Explanation:

i  queries[i]  nums[li..ri]  Removed  Remaining     k  ans[i]
0  [0, 1, 1]   [3, 6]        [6]      2, 4, 8, ...  1  2
1  [1, 1, 3]   [6]           [6]      2, 4, 8, ...  3  8

Thus, ans = [2, 8].



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
nums is strictly increasing
1 <= queries.length <= 10^5
queries[i] = [li, ri, ki]
0 <= li <= ri < nums.length
1 <= ki <= 10^9
"""

from bisect import bisect_left, bisect_right


class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even = [i for i, x in  enumerate(nums) if x % 2 == 0]
        missing = [nums[idx] // 2 - i - 1 for i, idx in enumerate(even)]
        
        ans = []
        for l, r, k in queries:
            lo = bisect_left(even, l)
            hi = bisect_right(even, r)
            p = bisect_left(missing, k - lo, lo=lo, hi=hi) - lo
            ans.append((p + k) * 2)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.kthRemainingInteger([1, 4, 7], [[0, 2, 1], [1, 1, 2], [0, 0, 3]]))  # [2, 6, 6]

    # Example 2
    print(sol.kthRemainingInteger([2, 5, 8], [[0, 1, 2], [1, 2, 1], [0, 2, 4]]))  # [6, 2, 12]

    # Example 3
    print(sol.kthRemainingInteger([3, 6], [[0, 1, 1], [1, 1, 3]]))  # [2, 8]
