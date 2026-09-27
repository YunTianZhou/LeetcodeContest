"""
4062. Transform Array Using Pair Operations - Medium


You are given two integer arrays source and target.

In one operation, you may choose two distinct indices i and j in source, along with any integer delta. Then update source as follows:

source[i] = source[i] + source[j] - delta
source[j] = delta

Return true if it is possible to make source equal to target after performing the operation any (including zero) number of times. Otherwise, return false.



Example 1:

Input: source = [1,2,3], target = [0,2,4]

Output: true

Explanation:

Choose indices i = 0 and j = 2, and set delta = 4.

Before operation, source[0] = 1 and source[2] = 3.

After the operation,

source[0] = 1 + 3 - 4 = 0
source[2] = 4

Hence, source becomes [0, 2, 4], which is equal to target.

Therefore, the answer is true.


Example 2:

Input: source = [-5,-5], target = [-15,5]

Output: true

Explanation:

Choose indices i = 1 and j = 0, and set delta = -15.

Before operation, source[1] = -5 and source[0] = -5.

After the operation,

source[1] = -5 + (-5) - (-15) = 5
source[0] = -15

Hence, source becomes [-15, 5], which is equal to target.

Therefore, the answer is true.


Example 3:

Input: source = [1,2,1], target = [0,2,5]

Output: false

Explanation:

It can be shown that no matter what operations are performed, source can never be made equal to target. Therefore, the answer is false.



Constraints:

2 <= source.length == target.length <= 10^5
-10^9 <= source[i], target[i] <= 10^9
"""


class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        return sum(source) == sum(target)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.canTransform([1, 2, 3], [0, 2, 4]))  # True

    # Example 2
    print(sol.canTransform([-5, -5], [-15, 5]))  # True

    # Example 3
    print(sol.canTransform([1, 2, 1], [0, 2, 5]))  # False
