class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final_list = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while right > left:
                current_sum = nums[left] + nums[right] + nums[i]  
                if current_sum == 0:
                    final_list.append([nums[i], nums[left], nums[right]])
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
        return final_list




