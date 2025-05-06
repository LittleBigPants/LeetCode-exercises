class Solution(object):
    def isPalindrome(self, x):
        string = str(x)
        i = 0
        for f in range(len(string), i, -1):
            if string[f-1] != string[i]:
                return False
            i+= 1

        return True