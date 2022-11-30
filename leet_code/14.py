# 14. longest-common-prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if 0 == length:
            return ""

        retVal = strs[0]
        if 1 == length:
            return retVal

        for i in range(length - 1):
            temp = ''
            item = strs[i + 1]
            for j in range(min(len(retVal), len(item))):
                if retVal[j] == item[j]:
                    temp += retVal[j]
                else:
                    break
            retVal = temp

        return retVal


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
