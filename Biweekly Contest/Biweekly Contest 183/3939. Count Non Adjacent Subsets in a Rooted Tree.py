"""
3939. Count Non Adjacent Subsets in a Rooted Tree - Hard


You are given a rooted tree with n nodes labeled from 0 to n - 1, represented by an integer array parent of length n, where:

 - parent[0] = -1 (node 0 is the root).

 - For each 1 <= i < n, parent[i] is the parent of node i (0 <= parent[i] < i).

 - You are also given an integer array nums of length n, where nums[i] is the value of node i, and an integer k.

A non-empty subset of nodes is called valid if:

 - The sum of the values of the selected nodes is divisible by k.

 - No two selected nodes are adjacent in the tree (no node and its direct parent are both included in the subset).

Return the number of valid subsets modulo 10^9 + 7.



Example 1:

Input: parent = [-1,0,1], nums = [1,2,3], k = 3

Output: 1

Explanation:

[graph1](https://assets.leetcode.com/uploads/2025/07/17/image1.png)

The only valid subset is {2}. It contains node 2 with value 3, which is divisible by 3.


Example 2:

Input: parent = [-1,0,0,0], nums = [2,1,2,1], k = 3

Output: 2

Explanation:

[graph2](https://assets.leetcode.com/uploads/2025/07/17/image2.png)

The valid subsets are:

 - {2, 3}: Nodes 2 and 3 are also non-adjacent. Their values sum to 2 + 1 = 3, which is divisible by 3.
 - {1, 2}: Nodes 1 and 2 are both children of node 0 and not directly connected to each other. Their values sum to 1 + 2 = 3, which is divisible by 3.

No other subset satisfies both conditions. Therefore, the answer is 2.



Constraints:

n == parent.length == nums.length
1 <= n <= 1000
parent[0] == -1
For all 1 <= i < n:
0 <= parent[i] < i
1 <= nums[i] <= 10^9
1 <= k <= 100
parent describes a valid rooted tree.
"""


class Solution:
    def countValidSubsets(self, parent: list[int], nums: list[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        def dfs(a):
            f1 = [0] * k
            f2 = [0] * k
            f1[0] = 1
            f2[nums[a] % k] = 1

            for b in tree[a]:
                g1, g2 = dfs(b)
                
                nf1 = [0] * k
                nf2 = [0] * k
                for x in range(k):
                    if f1[x] == 0 and f2[x] == 0:
                        continue
                    for y in range(k):
                        if g1[y] == 0 and g2[y] == 0:
                            continue
                        t = (x + y) % k
                        nf1[t] = (nf1[t] + f1[x] * (g1[y] + g2[y])) % mod
                        nf2[t] = (nf2[t] + f2[x] * g1[y]) % mod
                
                f1, f2 = nf1, nf2
            
            return f1, f2

        f1, f2 = dfs(0)
        return (f1[0] + f2[0] - 1) % mod


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countValidSubsets([-1, 0, 1], [1, 2, 3], 3))  # 1

    # Example 2
    print(sol.countValidSubsets([-1, 0, 0, 0], [2, 1, 2, 1], 3))  # 2
