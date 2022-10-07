# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists

#class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:

nums = [3,2,4]
target = 6

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):
            match = target - number

            if match in nums[index+1:]:
                correct_match_index = nums[index+1:].index(match)

                return correct_match_index + index+1, index

# def twoSum(nums,target)
#     for number in nums:
#         match = target - number
#
# def find_match(nums, target, match):
#     if match in nums:
#         if nums.index(match) != nums.index(number):
#             return nums.index(match), nums.index(number)
#             find_match(nums, target, match)
#         else:
#             return find_match(nums, target, match)
#


#        return first, second
