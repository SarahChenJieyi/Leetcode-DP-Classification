class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        nums[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i] + nums[i - 3])
        return max(nums)
    # Time: 24ms
    # RAM: 12.8MB

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        pre_max = 0
        cur_max = nums[0]
        for i in range(1, len(nums)):
            temp = cur_max
            cur_max = max(nums[i] + pre_max, cur_max)
            pre_max = temp
        return max(cur_max, pre_max)
    # Time: 24ms
    # RAM: 12.7MB

if __name__ == '__main__':
    result = Solution().rob1([7,1,1,9,1])
    print(result)