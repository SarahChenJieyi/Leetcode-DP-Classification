class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp_max = list(nums)
        dp_min = list(nums)
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
        return max(max(dp_max), max(dp_min))


if __name__ == '__main__':
    result = Solution().maxProduct([-2,0,-1])
    print(result)