'''
https://leetcode.com/problems/next-permutation/
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            # i 오른쪽에서부터 순회하면서 nums[i]보다 큰 가장 첫 번째 숫자를 찾음
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # i+1부터 끝까지 오름차순으로 정렬 (reverse)
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
                            


            
                

            
            
# [1,3,2]
solution=Solution()
solution.nextPermutation([3,2,1])
