#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)/2
        for i in range(0,len(nums)-1):
            if (nums[i] == nums[(len(nums)-1)-i]) and (i != (len(nums)-1)-i):
                return True
