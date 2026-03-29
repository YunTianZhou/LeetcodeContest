"""
3883. Count Non Decreasing Arrays With Given Digit Sums - Hard


You are given an integer array digitSum of length n.

An array arr of length n is considered valid if:

 - 0 <= arr[i] <= 5000

 - it is non-decreasing.

 - the sum of the digits of arr[i] equals digitSum[i].

Return an integer denoting the number of distinct valid arrays. Since the answer may be large, return it modulo 10^9 + 7.

An array is said to be non-decreasing if each element is greater than or equal to the previous element, if it exists.



Example 1:

Input: digitSum = [25,1]

Output: 6

Explanation:

Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997.

The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000.

Thus, the valid arrays are [799, 1000], [889, 1000], [898, 1000], [979, 1000], [988, 1000], and [997, 1000].

Hence, the answer is 6.


Example 2:

Input: digitSum = [1]

Output: 4

Explanation:

The valid arrays are [1], [10], [100], and [1000].

Thus, the answer is 4.


Example 3:

Input: digitSum = [2,49,23]

Output: 0

Explanation:

There is no integer in the range [0, 5000] whose sum of digits is 49. Thus, the answer is 0.



Constraints:

1 <= digitSum.length <= 1000
0 <= digitSum[i] <= 50
"""


m = 5000
k = 31

sum_nums = [[] for _ in range(k + 1)]
for x in range(m + 1):
    sm = sum(map(int, str(x)))
    sum_nums[sm].append(x)

class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        mod = 10 ** 9 + 7

        dp = [0] * (m + 1)
        dp[0] = 1

        prev = 0
        for curr in digitSum:
            if curr > k:
                return 0
            
            p = sum_nums[prev]
            lp = len(p)
            sm = j = 0
            for x in sum_nums[curr]:
                while j < lp and x >= p[j]:
                    sm = (sm + dp[p[j]]) % mod
                    j += 1
                dp[x] = sm

            prev = curr
        
        return sum(dp[x] for x in sum_nums[prev]) % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countArrays([25, 1]))  # 6

    # Example 2
    print(sol.countArrays([1]))  # 4

    # Example 3
    print(sol.countArrays([2, 49, 23]))  # 0
