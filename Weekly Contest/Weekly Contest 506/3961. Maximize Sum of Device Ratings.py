"""
3961. Maximize Sum of Device Ratings - Medium


You are given a 2D integer array units of size m x n where units[i][j] represents the capacity of the jth unit in the ith device. Each device contains exactly n units.

The rating of a device is the minimum capacity among all its units.

You may perform the following operation any number of times (including zero):

 - Choose a device i that has not been used as a source before.

 - Remove exactly one unit from device i and add it to any different device.

 - Then mark device i as used, so it cannot be chosen again as a source.

Return the maximum possible sum of the ratings of all devices after any number of such operations.

Note:

 - Devices can receive units from multiple devices, regardless of whether they have been selected.

 - The rating of an empty device is 0.



Example 1:

Input: units = [[1,3],[2,2]]

Output: 4

Explanation:

 - Select device i = 0 and transfer units[0][0] = 1 to device i = 1.

 - After the transfer, the ratings are:
    - Device 0 = [3]: rating[0] = 3
    - Device 1 = [2, 2, 1]: rating[1] = 1

 - Thus, the sum of ratings is 3 + 1 = 4.


Example 2:

Input: units = [[1,2,3],[4,5,6]]

Output: 6

Explanation:

 - Select device i = 1 and transfer units[1][0] = 4 to device i = 0.

 - After the transfer, the ratings are:
    - Device 0 = [1, 2, 3, 4]: rating[0] = 1
    - Device 1 = [5, 6]: rating[1] = 5

 - Thus, the sum of ratings is 1 + 5 = 6.


Example 3:

Input: units = [[5,5,5],[1,1,1]]

Output: 6

Explanation:

 - No transfers increase the sum of ratings. Thus, the sum of ratings is 5 + 1 = 6.



Constraints:

1 <= m == units.length <= 10^5
1 <= n == units[i].length <= 10^5
m * n <= 2 * 10^5
1 <= units[i][j] <= 10^5
"""

from math import inf


class Solution:
    def maxRatings(self, units: list[list[int]]) -> int:
        if len(units[0]) == 1:
            return sum(x[0] for x in units)

        sm = 0
        mn1 = mn2 = inf
        for g in units:
            top1 = top2 = inf
            for x in g:
                if x < top1:
                    top2 = top1
                    top1 = x
                elif x < top2:
                    top2 = x
            
            sm += top2
            mn1 = min(mn1, top1)
            mn2 = min(mn2, top2)
            
        return sm - mn2 + mn1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxRatings([[1, 3], [2, 2]]))  # 4

    # Example 2
    print(sol.maxRatings([[1, 2, 3], [4, 5, 6]]))  # 6

    # Example 3
    print(sol.maxRatings([[5, 5, 5], [1, 1, 1]]))  # 6
