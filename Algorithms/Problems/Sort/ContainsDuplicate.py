"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""
from Algorithms.Core.Sort.QuickSort import quick_sort


def containsDuplicate(nums: list[int]) -> bool:
    length = len(nums)
    quick_sort(0, length - 1, nums)
    for i in range(length - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(containsDuplicate(nums))
