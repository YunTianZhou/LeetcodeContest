"""
3573. Best Time to Buy and Sell Stock V - Medium


You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:

Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.



Example 1:

Input: prices = [1,7,9,8,2], k = 2

Output: 14

Explanation:

We can make $14 of profit through 2 transactions:
A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.


Example 2:

Input: prices = [12,16,19,19,8,1,19,13,9], k = 3

Output: 36

Explanation:

We can make $36 of profit through 3 transactions:
A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.
 


Constraints:

2 <= prices.length <= 10^3
1 <= prices[i] <= 10^9
1 <= k <= prices.length / 2
"""

from typing import List
from math import inf


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        prev = [[-inf] * (k + 1) for _ in range(3)]
        curr = [[0] * (k + 1) for _ in range(3)]

        for i in range(k + 1):
            prev[0][i] = 0

        for x in prices:
            for state in range(3):
                for left_k in range(k + 1):
                    if state == 0:
                        curr[state][left_k] = max(prev[0][left_k], 
                                                  prev[1][left_k] + x, 
                                                  prev[2][left_k] - x)
                    elif state == 1:
                        curr[state][left_k] = max(prev[1][left_k], 
                                                  prev[0][left_k - 1] - x if left_k > 0 else -inf)
                    else:  # state == 2
                        curr[state][left_k] = max(prev[2][left_k], 
                                                  prev[0][left_k - 1] + x if left_k > 0 else -inf)
            curr, prev = prev, curr

        return prev[0][k]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maximumProfit([1, 7, 9, 8, 2], 2))  # 14

    # Example 2
    print(sol.maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3))  # 36
