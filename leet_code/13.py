# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        retVal = 0
        index = len(s) - 1
        while index >= 0:
            temp = 0
            if index > 0:
                temp = self.getChar(s[index - 1] + s[index])

            if temp > 0:
                retVal += temp
                index -= 2
            else:
                retVal += self.getChar(s[index])
                index -= 1

        return retVal

    def getChar(self, num):
        # print(num)
        # if num == 'MMM': return 3000
        # if num == 'MM': return 2000
        if num == 'M': return 1000
        if num == 'CM': return 900
        # if num == 'DCCC': return 800
        # if num == 'DCC': return 700
        # if num == 'DC': return 600
        if num == 'D': return 500
        if num == 'CD': return 400
        # if num == 'CCC': return 300
        # if num == 'CC': return 200
        if num == 'C': return 100
        if num == 'XC': return 90
        # if num == 'LXXX': return 80
        # if num == 'LXX': return 70
        # if num == 'LX': return 60
        if num == 'L': return 50
        if num == 'XL': return 40
        # if num == 'XXX': return 30
        # if num == 'XX': return 20
        if num == 'X': return 10
        if num == 'IX': return 9
        # if num == 'VIII': return 8
        # if num == 'VII': return 7
        # if num == 'VI': return 6
        if num == 'V': return 5
        if num == 'IV': return 4
        # if num == 'III': return 3
        # if num == 'II': return 2
        if num == 'I': return 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman('III'))
    print(s.intToRoman('IV'))
    print(s.intToRoman('IX'))
    print(s.intToRoman('LVIII'))
    print(s.intToRoman('MCMXCIV'))
    print(s.intToRoman('MMMCMXCIX'))
