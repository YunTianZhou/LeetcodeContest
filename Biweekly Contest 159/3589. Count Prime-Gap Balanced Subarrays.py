"""
3589. Count Prime-Gap Balanced Subarrays - Medium


You are given an integer array nums and an integer k.

A subarray is called prime-gap balanced if:

It contains at least two prime numbers, and
The difference between the maximum and minimum prime numbers in that subarray is less than or equal to k.
Return the count of prime-gap balanced subarrays in nums.

Note:

A subarray is a contiguous non-empty sequence of elements within an array.
A prime number is a natural number greater than 1 with only two factors, 1 and itself.
 


Example 1:

Input: nums = [1,2,3], k = 1

Output: 2

Explanation:

Prime-gap balanced subarrays are:

[2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
[1,2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
Thus, the answer is 2.


Example 2:

Input: nums = [2,3,5,7], k = 3

Output: 4

Explanation:

Prime-gap balanced subarrays are:

[2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
[2,3,5]: contains three primes (2, 3, and 5), max - min = 5 - 2 = 3 <= k.
[3,5]: contains two primes (3 and 5), max - min = 5 - 3 = 2 <= k.
[5,7]: contains two primes (5 and 7), max - min = 7 - 5 = 2 <= k.
Thus, the answer is 4.

 

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 5 * 10^4
0 <= k <= 5 * 10^4
"""

from typing import List
from collections import deque


m = 10 ** 6
is_prime = [True] * (m + 2)
is_prime[0] = is_prime[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, m + 1, i):
            is_prime[j] = False


class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        inc = deque()
        dec = deque()
        res = j = prev = 0
        prev_prime = -1

        for i, x in enumerate(nums):
            if is_prime[x]:
                while dec and x > nums[dec[-1]]:
                    dec.pop()
                while inc and x <= nums[inc[-1]]:
                    inc.pop()
                inc.append(i)
                dec.append(i)

                while nums[dec[0]] - nums[inc[0]] > k:
                    if j == dec[0]:
                        dec.popleft()
                    if j == inc[0]:
                        inc.popleft()
                    j += 1

                prev = 0 if inc[0] == dec[0] else prev_prime - j + 1
                prev_prime = i
            res += prev

        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.primeSubarray([1, 2, 3], 1))  # 2

    # Example 2
    print(sol.primeSubarray([2, 3, 5, 7], 3))  # 4
