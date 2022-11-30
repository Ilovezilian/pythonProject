# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        return self.f(0, digits)

    def f(self, i, digits):
        if i == len(digits) - 1:
            return self.getCharList(digits[i])

        f_list = self.f(i + 1, digits)
        char_list = self.getCharList(digits[i])
        result = list()
        for char_item in char_list:
            for f_item in f_list:
                result.append(char_item + f_item)
        return result

    @staticmethod
    def getCharList(num):
        if num == '2': return list('abc')
        if num == '3': return list('def')
        if num == '4': return list('ghi')
        if num == '5': return list('jkl')
        if num == '6': return list('mno')
        if num == '7': return list('pqrs')
        if num == '8': return list('tuv')
        if num == '9': return list('wxyz')
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
