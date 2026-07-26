"""
4001. Aggregate Two Time Series - Medium


You are given two 2D integer arrays series1 and series2.

Each element in both series is of the form [timestamp, value], where:

 - timestamp is an integer representing the time.

 - value is an integer representing the value at that timestamp.

Each array is sorted in strictly increasing order of timestamp.

For any timestamp not present in a series, its value is taken from the next available timestamp in the same series if one exists. Otherwise, its value is considered 0.

The aggregated series is formed by summing the corresponding values from both series at every timestamp that appears in either series.

Return the aggregated series as a 2D integer array of [timestamp, summedValue] pairs, sorted in strictly increasing order of timestamp.



Example 1:

Input: series1 = [[1,3],[4,1]], series2 = [[2,2],[5,2]]

Output: [[1,5],[2,3],[4,3],[5,2]]

Explanation:

Timestamp  series1  series2  summedValue
1          3        2        5
2          1        2        3
4          1        2        3
5          0        2        2

Thus, the aggregated series is [[1, 5], [2, 3], [4, 3], [5, 2]].


Example 2:

Input: series1 = [[1,5],[3,1]], series2 = [[2,2]]

Output: [[1,7],[2,3],[3,1]]

Explanation:

Timestamp  series1  series2  summedValue
1          5        2        7
2          1        2        3
3          1        0        1

Thus, the aggregated series is [[1, 7], [2, 3], [3, 1]].


Example 3:

Input: series1 = [[1,5]], series2 = [[1000000000,2]]

Output: [[1,7],[1000000000,2]]

Explanation:

At timestamp 1, the next available value in series2 is 2 at timestamp 1000000000. At timestamp 1000000000, there is no later timestamp in series1, so its value is 0. Only timestamps that appear in at least one of the two series are included.



Constraints:

1 <= series1.length, series2.length <= 10^5
series1[i].length == series2[i].length == 2
1 <= series1[i][0], series2[i][0] <= 10^9
1 <= series1[i][1], series2[i][1] <= 10^9
Each series is sorted in strictly increasing order of timestamp.
"""

from math import inf


class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        n, m = len(series1), len(series2)
        series1.append([inf, 0])
        series2.append([inf, 0])
        
        i = j = 0
        ans = []
        while i < n or j < m:
            t1, x = series1[i]
            t2, y = series2[j]
            
            if t1 <= t2:
                i += 1
            if t1 >= t2:
                j += 1
                
            ans.append([min(t1, t2), x + y])
            
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.aggregateTimeSeries([[1, 3], [4, 1]], [[2, 2], [5, 2]]))  # [[1, 5], [2, 3], [4, 3], [5, 2]]

    # Example 2
    print(sol.aggregateTimeSeries([[1, 5], [3, 1]], [[2, 2]]))  # [[1, 7], [2, 3], [3, 1]]

    # Example 3
    print(sol.aggregateTimeSeries([[1, 5]], [[1000000000, 2]]))  # [[1, 7], [1000000000, 2]]
