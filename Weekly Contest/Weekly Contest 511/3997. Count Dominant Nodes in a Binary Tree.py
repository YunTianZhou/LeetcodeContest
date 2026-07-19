"""
3997. Count Dominant Nodes in a Binary Tree - Medium


You are given the root of a complete binary tree.

A node x is called dominant if its value is equal to the maximum value among all nodes in the subtree rooted at x.

Return the number of dominant nodes in the tree.



Example 1:

[graph1](https://assets.leetcode.com/uploads/2026/06/13/tnew.png)

Input: root = [5,3,8,2,4,7,1]

Output: 5

Explanation:

 - The leaf nodes with values 2, 4, 7, and 1 are dominant.

 - The node with value 8 is dominant because its value is the maximum value in its subtree [8, 7, 1].

 - Thus, the answer is 5.


Example 2:

[graph2](https://assets.leetcode.com/uploads/2026/06/15/t9.png)

Input: root = [1,2,3,1,2]

Output: 4

Explanation:

 - The leaf nodes with values 1, 2, and 3 are dominant.

 - The node with value 2 whose subtree is [2, 1, 2] is dominant because its value is the maximum value in its subtree.

 - Thus, the answer is 4.



Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^9
The tree is guaranteed to be a complete binary tree.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values: list[int]):
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            node.left = TreeNode(values[i])
            queue.append(node.left)
            i += 1
        if i < len(values):
            node.right = TreeNode(values[i])
            queue.append(node.right)
            i += 1

    return root


class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans = 0
        
        def dfs(root):
            if root is None:
                return 0
            
            mx = max(dfs(root.left), dfs(root.right), root.val)
            
            if root.val == mx:
                nonlocal ans
                ans += 1
            
            return mx
        
        dfs(root)
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.countDominantNodes(build_tree_from_list([5, 3, 8, 2, 4, 7, 1])))  # 5

    # Example 2
    print(sol.countDominantNodes(build_tree_from_list([1, 2, 3, 1, 2])))  # 4
