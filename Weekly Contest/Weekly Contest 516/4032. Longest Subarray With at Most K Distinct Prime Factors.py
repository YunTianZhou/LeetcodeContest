"""
4032. Longest Subarray With at Most K Distinct Prime Factors - Medium


You are given an integer array nums consisting of positive integers and an integer k.

The prime factor set of a subarray is the union of the distinct prime factors of all its elements.

Return the length of the longest subarray whose prime factor set contains at most k distinct prime factors. If no such subarray exists, return 0.



Example 1:

Input: nums = [7,6,10,12,11], k = 3

Output: 3

Explanation:

Consider the subarray [6, 10, 12]:

 - The distinct prime factors of 6 are {2, 3}.

 - The distinct prime factors of 10 are {2, 5}.

 - The distinct prime factors of 12 are {2, 3}.

 - The union of these sets is {2, 3, 5}, which contains 3 distinct prime factors.

No longer subarray satisfies the condition. Therefore, the answer is 3.


Example 2:

Input: nums = [4,6,9,18], k = 4

Output: 4

Explanation:

Consider the entire array [4, 6, 9, 18]:

 - The distinct prime factors of 4 are {2}.

 - The distinct prime factors of 6 are {2, 3}.

 - The distinct prime factors of 9 are {3}.

 - The distinct prime factors of 18 are {2, 3}.

 - The union of these sets is {2, 3}, which contains 2 distinct prime factors.

Since 2 <= 4, the entire array is valid. Therefore, the answer is 4.


Example 3:

Input: nums = [6,10,15], k = 2

Output: 1

Explanation:

Every subarray of length at least 2 has prime factor set {2, 3, 5}, which contains 3 distinct prime factors.

Since 3 > 2, only subarrays of length 1 are valid. Therefore, the answer is 1.



Constraints:

1 <= nums.length <= 10^5
2 <= nums[i] <= 10^5
1 <= k <= 10^4
"""

m = 10 ** 5

prime_factors = [[] for _ in range(m + 1)]
for i in range(2, m + 1):
    if prime_factors[i]:
        continue
    for j in range(i, m + 1, i):
        prime_factors[j].append(i)


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        cnt = {}

        ans = j = 0
        for i in range(len(nums)):
            for p in prime_factors[nums[i]]:
                cnt[p] = cnt.get(p, 0) + 1
            
            while len(cnt) > k:
                for p in prime_factors[nums[j]]:
                    cnt[p] -= 1
                    if cnt[p] == 0:
                        del cnt[p]
                j += 1
            
            ans = max(ans, i - j + 1)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longestSubarray([7, 6, 10, 12, 11], 3))  # 3

    # Example 2
    print(sol.longestSubarray([4, 6, 9, 18], 4))  # 4

    # Example 3
    print(sol.longestSubarray([6, 10, 15], 2))  # 1
