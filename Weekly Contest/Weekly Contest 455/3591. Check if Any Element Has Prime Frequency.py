"""
3591. Check if Any Element Has Prime Frequency - Easy


You are given an integer array nums.

Return true if the frequency of any element of the array is prime, otherwise, return false.

The frequency of an element x is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

 

Example 1:

Input: nums = [1,2,3,4,5,4]

Output: true

Explanation:

4 has a frequency of two, which is a prime number.


Example 2:

Input: nums = [1,2,3,4,5]

Output: false

Explanation:

All elements have a frequency of one.


Example 3:

Input: nums = [2,2,2,4,4]

Output: true

Explanation:

Both 2 and 4 have a prime frequency.

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List
from collections import Counter


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n: int) -> bool:
            # Since n <= 100, we can use a simple check using small primes
            primes = [2, 3, 5, 7]
            return n > 1 and (n in primes or all(n % p != 0 for p in primes))

        frequency = Counter(nums)
        return any(is_prime(count) for count in frequency.values())


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.checkPrimeFrequency([1, 2, 3, 4, 5, 4]))  # true

    # Example 2
    print(sol.checkPrimeFrequency([1, 2, 3, 4, 5]))  # false

    # Example 3
    print(sol.checkPrimeFrequency([2, 2, 2, 4, 4]))  # true
