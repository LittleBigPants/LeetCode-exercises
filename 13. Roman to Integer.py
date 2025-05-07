class Solution(object):
    def romanToInt(self, string):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        """
        :type string: str
        :rtype: int
        """
        result = 0
        for i in range(len(string)):
            if i > 0:
                if (string[i] in ("V", "X") and string[i - 1] == "I"):
                    result += roman_numerals[string[i]] - 2
                elif (string[i] in ("L", "C") and string[i - 1] == "X"):
                    result += roman_numerals[string[i]] - 20
                elif (string[i] in ("D", "M") and string[i - 1] == "C"):
                    result += roman_numerals[string[i]] - 200
                else:
                    result += roman_numerals[string[i]]
            else:
                result += roman_numerals[string[i]]

        return result