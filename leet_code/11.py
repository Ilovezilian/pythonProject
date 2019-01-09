# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
class Solution:
    # // standard
    def maxArea(self, height):
        right = len(height) - 1
        left = 0
        retVal = 0
        while left < right:
            # print(height[left], "--", height[right])
            retVal = max(retVal, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # print(retVal)
        return retVal

    # // my
    def maxArea_my(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        upMap = {}
        i = 0
        maxVal = 0
        # asc items
        for h in height:
            if h > maxVal:
                maxVal = h
                upMap.__setitem__(i, maxVal)
            i += 1

        downMap = {}
        # down items
        i = 0
        maxVal = 0
        length = len(height)
        for h in reversed(height):
            if h > maxVal:
                maxVal = h
                downMap.__setitem__(length - i - 1, maxVal)
            i += 1

        # print(upMap, "--", downMap)
        retVal = 0
        for upKey in upMap.keys():
            for downKey in downMap.keys():
                retVal = max(retVal, (downKey - upKey) * min(upMap[upKey], downMap[downKey]))

        # print(retVal)
        return retVal


if __name__ == '__main__':
    s = Solution()
    s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
