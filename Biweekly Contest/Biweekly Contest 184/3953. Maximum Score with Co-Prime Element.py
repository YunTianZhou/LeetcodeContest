"""
3953. Maximum Score with Co-Prime Element - Hard


You are given an integer array nums of length n and an integer maxVal.

You may change any element in nums to any positive integer less than or equal to maxVal. Each such change costs 1.

Two integers are co-prime if their greatest common divisor (GCD) is 1.

After all modifications, you must choose an index i such that, nums[i] is co-prime with every other element nums[j].

Let:

 - selectedValue be the final value of nums[i] after modifications.

 - modificationCost be the total number of elements changed.

The score is defined as score = selectedValue - modificationCost.

Return the maximum possible score.



Example 1:

Input: nums = [3,4,6], maxVal = 5

Output: 4

Explanation:

Change nums[2] from 6 to 5, which costs 1. Choose nums[2] = 5, since it is co-prime with 3 and 4.

 - selectedValue = 5

 - modificationCost = 1

 - The score is 5 - 1 = 4


Example 2:

Input: nums = [1,2,3], maxVal = 4

Output: 3

Explanation:

No modifications are required. Choose nums[2] = 3, since it is co-prime with 1 and 2.

 - selectedValue = 3

 - modificationCost = 0

 - The score is 3 - 0 = 3


Example 3:

Input: nums = [2,2], maxVal = 1

Output: 1

Explanation:

Change nums[0] from 2 to 1, which costs 1. Choose nums[1] = 2, since it is co-prime with 1.

 - selectedValue = 2

 - modificationCost = 1

 - The score is 2 - 1 = 1



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= maxVal <= 10^5
"""

from collections import defaultdict


m = 10 ** 5

divisors = [[] for _ in range(m + 1)]
for i in range(2, m + 1):
    for j in range(i, m + 1, i):
        divisors[j].append(i)

rad = [1] * (m + 2)
prime_factors = [0] * (m + 2)
for i in range(2, m):
    if prime_factors[i] == 0:
        for j in range(i, m + 1, i):
            rad[j] *= i
            prime_factors[j] += 1


class Solution:
    def maxScore(self, nums: list[int], maxVal: int) -> int:
        cnt = defaultdict(int)
        for x in nums:
            for d in divisors[x]:
                cnt[d] += 1
        
        def get(x):
            ans = 0
            for d in divisors[rad[x]]:
                sign = 1 if prime_factors[d] % 2 else -1
                ans += sign * cnt[d]
            return ans

        ans = 0

        for x in range(maxVal, 0, -1):
            if x <= ans:
                break
            ans = max(ans, x - max(1, get(x)))
        
        for x in nums:
            if x > ans:
                ans = max(ans, x - max(1, get(x)) + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxScore([3, 4, 6], 5))  # 4

    # Example 2
    print(sol.maxScore([1, 2, 3], 4))  # 3

    # Example 3
    print(sol.maxScore([2, 2], 1))  # 1
