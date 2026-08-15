class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set()
        longest_sequence = 0
        for num in nums:
            set1.add(num)
        for num in set1:
            if (num - 1) not in set1:
                current_number = num
                current_sequence = 1
                while (current_number + 1) in set1:
                    current_number += 1
                    current_sequence += 1
                longest_sequence = max(longest_sequence, current_sequence)
        return longest_sequence
                    
                       
        
                
                
            
                    

