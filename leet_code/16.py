# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = target - nums[0] - nums[1] - nums[2]
        len_nums = len(nums) - 1
        for i in range(len_nums - 1):
            res = self.f(nums, i + 1, len_nums, target - nums[i])
            if abs(res) < abs(result):
                result = res
            # print("nums[i] = ", nums[i], "res = ", res, "  result = ", result)
        return target - result

    def f(self, nums, l, r, target):
        result = target - (nums[l] + nums[r])
        while l < r:
            res = target - nums[l] - nums[r]
            if abs(res) < abs(result):
                result = res
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        # print("target = ", target, "  result = ", result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([-1, 0, 1, 0], 3))
