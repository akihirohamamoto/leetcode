#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def bruteforce(self, nums: List[int], target: int) -> List[int]:
        nums_under_targets = list(range(len(nums)))
        for i in list(itertools.combinations(nums_under_targets, 2)):
            if nums[i[0]] + nums[i[1]] == target: return i
    """
    Accepted
    52/52 cases passed (368 ms)
    Your runtime beats 31.61 % of python3 submissions
    Your memory usage beats 6.91 % of python3 submissions (51.2 MB)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
# @lc code=end

