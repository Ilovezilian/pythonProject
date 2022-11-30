# 18. 4Sum
# https://leetcode.com/problems/4sum/

class Solution:
    def letterCombinations(self, digits):
        """ todo
        :type digits: str
        :rtype: List[str]
        """

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.dfs(nums, 3, 0, target)

    def dfs(self, nums, height, left, target):

        res = list()
        for i in range(len(nums) - height)[left:]:
            if 0 == height:
                tmp = self.f(nums, left, len(nums) - 1, target)
                if tmp is not None:
                    res.append([tmp])
            else:
                for item in self.dfs(nums, height - 1, i + 1, target - nums[i]):
                    res.append(item.append(i))
        if len(res) == 0:
            res.append([])
        return res

    def f(self, nums, l, r, target):

        while l <= r:
            mid = int(l + (r - l - (r - l) % 1) / 2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            elif nums[mid] == target:
                return nums[mid]
            else :
                return None


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 1))
