class Solution(object):
    @staticmethod
    def gcdOfStrings(str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        a, b = len(str1), len(str2)
        while b > 0:
            a, b = b, a % b

        return str1[:a]


str1 = "ABCABC"
str2 = "ABC"
print(Solution.gcdOfStrings(str1, str2))