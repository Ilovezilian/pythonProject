# 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        myMap = {}
        for num in nums:
            if myMap.get(num) is None:
                myMap.setdefault(num, 1)
            else:
                myMap.__setitem__(num, myMap.get(num) + 1)

        # print(myMap)

        result = []
        mark = set()
        for key_1 in myMap.keys():
            for key_2 in myMap.keys():
                if mark.__contains__(key_2):
                    continue
                mark.add(key_1)
                if key_1 == key_2 and myMap.get(key_1) == 1:
                    continue
                if myMap.get(-key_1 - key_2) is None:
                    continue
                if key_2 > -key_2 - key_1:
                    continue
                if key_2 == -key_1 - key_2 and myMap.get(key_2) == 1:
                    continue
                if key_2 == key_1 and key_1 == - key_1 - key_2 and key_1 == 0 and myMap.get(key_1) < 3:
                    continue

                result.append([key_1, key_2, -key_1 - key_2])
        # print(mark)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 0]))
    print(s.threeSum([-1, 0, 1, 0]))
