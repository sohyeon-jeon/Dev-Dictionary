from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i+j>=len(nums):
                    continue
                else:
                    # 이미 dp에 값이 있으면 그 값이 최소값이므로, dp[i+j]가 0인 것만 이동시킨다! 
                    if dp[i+j]==0:
                        dp[i+j]=dp[i]+1
        return dp[-1]


solution=Solution()
solution.jump([1,2,3])
