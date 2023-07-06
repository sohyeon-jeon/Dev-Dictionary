'''
https://leetcode.com/problems/container-with-most-water/
'''
from typing import List

# 시간초과
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        area=0
        for i in range(len(height)):
            for j in range(len(height)):
                if i!=j:
                    w=abs(j-i)
                    h=min(height[i],height[j])
                    area=max(area,w*h)
        return area

# 이중 투포인터 사용
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left=0
        right=len(height)-1
        while (right-left)>0:
            max_area=max(max_area,(right-left)*min(height[left],height[right]))

            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
        return max_area
        
                    
solution=Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

'''
브루트포스( O(N2)에서 이중 투포인터 사용(O(n))으로 바꿨다.
left,right 변수를 이용해서 상황 비교해가면서 위치 이동하는 방법!
이진탐색과 비슷한 방법이다. 기초 알고리즘 상기시키자!!!!!
'''
