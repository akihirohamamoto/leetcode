# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
import itertools
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_under_targets = list(range(len(nums)))
        for i in list(itertools.combinations(nums_under_targets, 2)):
            if nums[i[0]] + nums[i[1]] == target: return i
    """
    Accepted
    52/52 cases passed (368 ms)
    Your runtime beats 31.61 % of python3 submissions
    Your memory usage beats 6.91 % of python3 submissions (51.2 MB)
    """
       
# @lc code=end
# debug case 1 : [1,2,3]\n4
