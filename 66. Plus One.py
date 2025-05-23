from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = -1
        try:
            while digits[k] == 9:
                digits[k] = 0
                k -= 1
        except IndexError:
            digits = [1] + digits
            return digits
        digits[k] += 1
        return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for num in range(len(digits)-1 ,-1, -1):
            if digits[num] < 9:
                digits[num] += 1
                return digits
            else:
                digits[num] = 0
        digits.insert(0, 1)
        return digits