"""
4035. Maximum Valid Split Positions I - Medium


You are given an integer array nums.

You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.

A split position i of arr is valid if:

 - 0 <= i < m - 1, and

 - gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).

An array of length 1 has no valid split positions.

The score of arr is the number of valid split positions in it.

Return the maximum possible score of arr.

Here, gcd(a) denotes the greatest common divisor of all elements in the array a.



Example 1:

Input: nums = [10,30,15,10]

Output: 2

Explanation:

One optimal solution is to remove nums[2] = 15. Then arr = [10, 30, 10].

The split positions are:

Split Position i  gcd(arr[0..i])  gcd(arr[i + 1..m - 1])
0                 10              10
1                 10              10

All split positions are valid. Thus, the answer is 2.


Example 2:

Input: nums = [2,10,14]

Output: 1

Explanation:

One optimal solution is to not remove any element. Then arr = [2, 10, 14].

The split positions are:

Split Position i  gcd(arr[0..i])  gcd(arr[i + 1..m - 1])
0                 2               2
1                 2               14

Only the split position at index 0 is valid. Thus, the answer is 1.


Example 3:

Input: nums = [2,4]

Output: 0

Explanation:

The only remaining array that has a split position is arr = [2, 4].

The split positions are:

Split Position i  gcd(arr[0..i])  gcd(arr[i + 1..m - 1])
0                 2               4

There are no valid split positions. Thus, the answer is 0.



Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 10^9
"""

from math import gcd


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        def get_score(nums: list[int]) -> int:
            n = len(nums)

            suf = [0] * n
            cur = 0
            for i in range(n - 1, -1, -1):
                cur = gcd(cur, nums[i])
                suf[i] = cur
            
            ans = cur = 0
            for i in range(n - 1):
                cur = gcd(cur, nums[i])
                if cur == suf[i + 1]:
                    ans += 1
            
            return ans

        ans = get_score(nums)
        for i in range(len(nums)):
            ans = max(ans, get_score(nums[: i] + nums[i + 1:]))
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxValidSplits([10, 30, 15, 10]))  # 2

    # Example 2
    print(sol.maxValidSplits([2, 10, 14]))  # 1

    # Example 3
    print(sol.maxValidSplits([2, 4]))  # 0
