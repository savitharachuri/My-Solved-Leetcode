# 15. 3Sum 
# https://leetcode.com/problems/3sum/description/

def three_sum(nums, target):
  nums.sort()
  for i in range(0, len(nums)-2):
    low = i + 1
    right = len(nums) - 1
    while low < right:
      triplet = nums[i] + nums[low] + nums[right]
      if triplet == target:
        return True
      elif triplet < target:
        low += 1
      else:
        right -= 1
  return False
      
    
