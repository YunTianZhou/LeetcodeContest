"""
3605. Minimum Stability Factor of Array - Hard


You are given an integer array nums and an integer maxC.

A subarray is called stable if the highest common factor (HCF) of all its elements is greater than or equal to 2.

The stability factor of an array is defined as the length of its longest stable subarray.

You may modify at most maxC elements of the array to any integer.

Return the minimum possible stability factor of the array after at most maxC modifications. If no stable subarray remains, return 0.

Note:

A subarray is a contiguous sequence of elements within an array.
The highest common factor (HCF) of an array is the largest integer that evenly divides all the array elements.
A subarray of length 1 is stable if its only element is greater than or equal to 2, since HCF([x]) = x.
 


Example 1:

Input: nums = [3,5,10], maxC = 1

Output: 1

Explanation:

The stable subarray [5, 10] has HCF = 5, which has a stability factor of 2.
Since maxC = 1, one optimal strategy is to change nums[1] to 7, resulting in nums = [3, 7, 10].
Now, no subarray of length greater than 1 has HCF >= 2. Thus, the minimum possible stability factor is 1.


Example 2:

Input: nums = [2,6,8], maxC = 2

Output: 1

Explanation:

The subarray [2, 6, 8] has HCF = 2, which has a stability factor of 3.
Since maxC = 2, one optimal strategy is to change nums[1] to 3 and nums[2] to 5, resulting in nums = [2, 3, 5].
Now, no subarray of length greater than 1 has HCF >= 2. Thus, the minimum possible stability factor is 1.


Example 3:

Input: nums = [2,4,9,6], maxC = 1

Output: 2

Explanation:

The stable subarrays are:
[2, 4] with HCF = 2 and stability factor of 2.
[9, 6] with HCF = 3 and stability factor of 2.
Since maxC = 1, the stability factor of 2 cannot be reduced due to two separate stable subarrays. Thus, the minimum possible stability factor is 2.
 


Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= maxC <= n
"""

from typing import List
from math import gcd


class SparseTable:
    def __init__(self, data):
        self.n = len(data)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        k = self.log[self.n] + 1
        self.st = [[0] * k for _ in range(self.n)]
        
        for i in range(self.n):
            self.st[i][0] = data[i]
        
        for j in range(1, k):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = self.combine(self.st[i][j-1], self.st[i + (1 << (j - 1))][j-1])

    def query(self, l, r):
        j = self.log[r - l + 1]
        return self.combine(self.st[l][j], self.st[r - (1 << j) + 1][j])
    
    def combine(self, a, b):
        return gcd(a, b)


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = n
        st = SparseTable(nums)

        while left <= right:
            mid = (left + right) // 2

            k = 0
            prev = 0
            for i in range(mid, n):
                if i - prev + 1 <= mid: continue
                prev = max(prev, i - mid)
                if st.query(prev, i) >= 2:
                    k += 1
                    prev = i + 1
                    if k > maxC:
                        break

            if k <= maxC:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.minStable([3, 5, 10], 1))  # 1

    # Example 2
    print(sol.minStable([2, 6, 8], 2))  # 1

    # Example 3
    print(sol.minStable([2, 4, 9, 6], 1))  # 2
