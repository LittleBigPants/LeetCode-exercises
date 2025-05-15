class Solution:
    #(!array.length || array.pop() !== dicc[char])
    def isValid(self, s: str) -> bool:
        array= []
        dicc= {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            print("array :", array)
            print(c)
            if c not in dicc:
             array.append(c)
            elif not array or array.pop() != dicc[c]:
             return False
            else:
                array.pop()
        return len(array) == 0

solution = Solution()

print(solution.isValid("{}"))