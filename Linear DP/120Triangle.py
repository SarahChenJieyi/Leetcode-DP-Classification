class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        # modify on the original list 
        # each element represents the minimum path sum end with current element
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                last_min = sys.maxsize
                if j == 0:
                    last_min = triangle[i-1][j]
                elif j == i:
                    last_min = triangle[i-1][j-1]
                else:
                    last_min = min(triangle[i-1][j], triangle[i-1][j-1])
                triangle[i][j] = last_min + triangle[i][j]
        
        return min(triangle[-1])
