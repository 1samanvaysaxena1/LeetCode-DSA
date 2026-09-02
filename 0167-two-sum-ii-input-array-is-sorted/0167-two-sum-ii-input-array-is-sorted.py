class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list1 = []
        left = 0
        right = len(numbers) - 1
        while True:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum == target:
                list1.append(left + 1)
                list1.append(right + 1)
                return list1
            
        