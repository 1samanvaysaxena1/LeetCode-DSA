class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for index,num in enumerate(nums):
            if target - num in dict1:
                num2 = target - num
                return [dict1[num2],index]
            dict1.setdefault(num,index)
        