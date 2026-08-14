class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        right_product = 1
        left_product_list = []
        right_product_list = []
        final_list = []
        for i in range(len(nums)):
            left_product_list.append(left_product)
            left_product *= nums[i]
        for i in range(len(nums) - 1,-1,-1):
            right_product_list.append(right_product)
            right_product *= nums[i]
        right_product_list.reverse()
        for left,right in zip(left_product_list,right_product_list):
            final_list.append(left * right)
        return final_list
        
