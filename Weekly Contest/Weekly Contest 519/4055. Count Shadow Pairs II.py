"""
4055. Count Shadow Pairs II - Hard


You are given an integer array nums of length n.

A pair of indices (i, j) is called a shadow pair if all of the following conditions are satisfied:

 - 0 <= i < j < n

 - nums[i] < nums[j]

 - There does not exist an index k such that i < k < j and nums[i] < nums[k] < nums[j].

Return the total number of shadow pairs.



Example 1:

Input: nums = [3,1,4,2,5]

Output: 5

Explanation:

(i, j)  nums[i]  nums[j]  Shadow Pair
(0, 2)  3        4        nums[1] = 1 is not strictly between 3 and 4
(1, 2)  1        4        No index k exists such that 1 < k < 2
(1, 3)  1        2        nums[2] = 4 is not strictly between 1 and 2
(2, 4)  4        5        nums[3] = 2 is not strictly between 4 and 5
(3, 4)  2        5        No index k exists such that 3 < k < 4

Thus, the answer is 5.


Example 2:

Input: nums = [6,7,8,9]

Output: 3

Explanation:

(i, j)  nums[i]  nums[j]  Shadow Pair
(0, 1)  6        7        No index k exists such that 0 < k < 1
(1, 2)  7        8        No index k exists such that 1 < k < 2
(2, 3)  8        9        No index k exists such that 2 < k < 3

Thus, the answer is 3.



Constraints:

3 <= n == nums.length <= 5 * 10^4
1 <= nums[i] <= 10^9
"""

from bisect import bisect_left, bisect_right


class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        def dfs(a: list[int], vl: int, vr: int) -> int:
            if vl == vr:
                return 0
            
            mid = (vl + vr) // 2
            ans = 0

            st_upper = []
            st_lower = []
            left = []
            right = []
            for i, x in enumerate(a):
                if x > mid:
                    while st_upper and x <= a[st_upper[-1]]:
                        st_upper.pop()
                    p = bisect_right(st_lower, st_upper[-1]) if st_upper else 0
                    ans += len(st_lower) - p
                    st_upper.append(i)
                    right.append(x)
                else:
                    while st_lower and x > a[st_lower[-1]]:
                        st_lower.pop()
                    st_lower.append(i)
                    left.append(x)
            
            ans += dfs(left, vl, mid)
            ans += dfs(right, mid + 1, vr)
            return ans
        
        xs = sorted(set(nums))
        a = [bisect_left(xs, x) for x in nums]
        return dfs(a, 0, len(xs) - 1)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.shadowPairs([3, 1, 4, 2, 5]))  # 5

    # Example 2
    print(sol.shadowPairs([6, 7, 8, 9]))  # 3
