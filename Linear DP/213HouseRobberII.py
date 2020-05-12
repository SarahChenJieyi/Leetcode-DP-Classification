class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        pre_max = 0
        cur_max = nums[0]
        for i in range(1, len(nums)):
            temp = cur_max
            cur_max = max(nums[i] + pre_max, cur_max)
            pre_max = temp
        return max(cur_max, pre_max)


if __name__ == '__main__':
    result = Solution().rob([-2,0,-1])
    print(result)