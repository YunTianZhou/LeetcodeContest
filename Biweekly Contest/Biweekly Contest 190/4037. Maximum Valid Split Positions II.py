"""
4037. Maximum Valid Split Positions II - Hard


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

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from itertools import accumulate
from math import gcd


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        
        pref = list(accumulate(nums, gcd, initial=0))
        suf = list(accumulate(nums[::-1], gcd, initial=0))[::-1]
        
        ans = sum(pref[i] == suf[i] for i in range(n))
        for i in range(n):
            if pref[i + 1] == pref[i]:
                continue
            g = gcd(pref[i], suf[i + 1])

            cur = 0
            for l in range(n):
                if l != i:
                    cur = gcd(cur, nums[l])
                if cur == g:
                    break

            cur = 0
            for r in range(n - 1, l - 1, -1):
                if r != i:
                    cur = gcd(cur, nums[r])
                if cur == g:
                    break

            ans = max(ans, r - l - (l < i < r))
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxValidSplits([10, 30, 15, 10]))  # 2

    # Example 2
    print(sol.maxValidSplits([2, 10, 14]))  # 1

    # Example 3
    print(sol.maxValidSplits([2, 4]))  # 0
