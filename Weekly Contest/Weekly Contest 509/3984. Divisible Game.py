"""
3984. Divisible Game - Medium


You are given an integer array nums of length n.

Alice and Bob are playing a game. Alice chooses:

- An integer k such that k > 1.

- Two integers l and r such that 0 <= l <= r < n.

Initially, both Alice's and Bob's scores are 0.

For each index i in the range [l, r] (inclusive):

 - If nums[i] is divisible by k, Alice's score increases by nums[i].

 - Otherwise, Bob's score increases by nums[i].

The score difference is Alice's score minus Bob's score.

Alice wants to maximize the score difference. If there are multiple values of k that achieve the maximum score difference, she chooses the smallest such k.

Return the product of the maximum score difference and the chosen value of k. Since the result can be large, return it modulo 10^9 + 7.



Example 1:

Input: nums = [1,4,6,8]

Output: 36

Explanation:

 - Alice can choose k = 2, l = 1, and r = 3.

 - All values in nums[1..3] are divisible by 2, so Alice's score is 4 + 6 + 8 = 18, while Bob's score is 0.

 - The score difference is 18, which is the maximum possible. Among all values of k that achieve this score difference, the smallest is 2.

 - Therefore, the answer is 18 * 2 = 36.


Example 2:

Input: nums = [2,1,2]

Output: 6

Explanation:

 - Alice can choose k = 2, l = 0, and r = 2.

 - The values nums[0] and nums[2] are divisible by 2, so Alice's score is 2 + 2 = 4. The value nums[1] is not divisible by 2, so Bob's score is 1.

 - The score difference is 4 - 1 = 3, which is the maximum possible. Among all values of k that achieve this score difference, the smallest is 2.

 - Therefore, the answer is 3 * 2 = 6.


Example 3:

Input: nums = [1]

Output: 1000000005

Explanation:

 - Alice must choose some k > 1. The smallest possible choice is k = 2.

 - Since nums[0] is not divisible by 2, Alice's score is 0, while Bob's score is 1.

 - The score difference is -1, which is the maximum possible.

 - Therefore, the answer is -1 * 2 = -2. Modulo 109 + 7, this equals 1000000005.



Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^6
"""

from collections import defaultdict
from itertools import accumulate
from math import inf


m = 10 ** 6

factors = [[] for _ in range(m + 1)]
for i in range(2, m + 1):
    if not factors[i]:
        for j in range(i, m + 1, i):
            factors[j].append(i)


class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        mod = 10 ** 9 + 7

        groups = defaultdict(list)
        for i, x in enumerate(nums):
            for f in factors[x]:
                groups[f].append(i)

        ps = list(accumulate(nums, initial=0))

        mx = (-min(nums), -2)
        ans = mx[0] * 2
        for k, g in groups.items():
            cur_mx = -inf
            sm = 0
            prev = -1
            for i in g:
                s = ps[i] - ps[prev + 1]
                sm = nums[i] + max(0, sm - s)
                cur_mx = max(cur_mx, sm)
                prev = i
            
            key = (cur_mx, -k)
            if key > mx:
                mx = key
                ans = cur_mx * k
        
        return ans % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.divisibleGame([1, 4, 6, 8]))  # 36

    # Example 2
    print(sol.divisibleGame([2, 1, 2]))  # 6

    # Example 3
    print(sol.divisibleGame([1]))  # 1000000005
