# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        retVal = ''.__add__(self.getChar(1000, num)).__add__(self.getChar(100, num)).__add__(
            self.getChar(10, num)).__add__(self.getChar(1, num))
        # print("retval = ", retVal)
        return retVal

    def getChar(self, mod, num):
        num = num % (mod * 10) - num % mod
        # print(num)
        if 0 == num: return ''
        if 1 == num: return 'I'
        if 2 == num: return 'II'
        if 3 == num: return 'III'
        if 4 == num: return 'IV'
        if 5 == num: return 'V'
        if 6 == num: return 'VI'
        if 7 == num: return 'VII'
        if 8 == num: return 'VIII'
        if 9 == num: return 'IX'
        if 10 == num: return 'X'
        if 20 == num: return 'XX'
        if 30 == num: return 'XXX'
        if 40 == num: return 'XL'
        if 50 == num: return 'L'
        if 60 == num: return 'LX'
        if 70 == num: return 'LXX'
        if 80 == num: return 'LXXX'
        if 90 == num: return 'XC'
        if 100 == num: return 'C'
        if 200 == num: return 'CC'
        if 300 == num: return 'CCC'
        if 400 == num: return 'CD'
        if 500 == num: return 'D'
        if 600 == num: return 'DC'
        if 700 == num: return 'DCC'
        if 800 == num: return 'DCCC'
        if 900 == num: return 'CM'
        if 1000 == num: return 'M'
        if 2000 == num: return 'MM'
        if 3000 == num: return 'MMM'


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1))
    print(s.intToRoman(3))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
    print(s.intToRoman(3999))
