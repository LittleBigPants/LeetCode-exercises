import array as arr
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for word in range(len(words)):
            if x in words[word]:
                result.append(word)
                    
        return result


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i , word in enumerate(words) if x in word]

    
# Example usage:
solution = Solution()
words = ["hello", "world", "python", "code"]
x = "o"
result = solution.findWordsContaining(words, x)
print(result)  # Output: [0, 1, 3]