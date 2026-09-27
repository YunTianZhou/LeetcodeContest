"""
4065. Rearrange Array by Removing Distinct Values - Easy


You are given an integer array nums.

You start with an empty array ans. Repeat the following operation until nums is empty:

 - Identify all distinct values currently present in nums.

 - Remove one occurrence of every distinct value currently in nums, and append those values to ans in ascending order.

Return the array ans.



Example 1:

Input: nums = [3,1,3,2,1,3]

Output: [1,2,3,1,3,3]

Explanation:

Operation    Appended to ans    nums after       ans after
1            1, 2, 3            [3, 1, 3]        [1, 2, 3]
2            1, 3               [3]              [1, 2, 3, 1, 3]
3            3                  []               [1, 2, 3, 1, 3, 3]

nums is now empty, so the answer is [1, 2, 3, 1, 3, 3].


Example 2:

Input: nums = [7,7,4,4,4]

Output: [4,7,4,7,4]

Explanation:

Operation    Appended to ans    nums after    ans after
1            4, 7               [7, 4, 4]     [4, 7]
2            4, 7               [4]           [4, 7, 4, 7]
3            4                  []            [4, 7, 4, 7, 4]

nums is now empty, so the answer is [4, 7, 4, 7, 4].



Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = {}

        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1

        ans = []

        while cnt:
            for x in sorted(list(cnt.keys())):
                ans.append(x)
                cnt[x] -= 1

                if cnt[x] == 0:
                    del cnt[x]

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.rearrangeArray([3, 1, 3, 2, 1, 3]))  # [1, 2, 3, 1, 3, 3]

    # Example 2
    print(sol.rearrangeArray([7, 7, 4, 4, 4]))  # [4, 7, 4, 7, 4]
