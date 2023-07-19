from typing import List
from collections import deque

# 큰 문제를 작은 문제로 나눌 수 있다! dp
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        
        # 0열 채우기
        for r in range(1,m):
            grid[r][0]+=grid[r-1][0]

        # 0행 채우기
        for c in range(1,n):
            grid[0][c]+=grid[0][c-1]
        
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        
        return grid[m-1][n-1]

        
# 시간초과
class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        answer=[]
        q=deque()
        m=len(grid)
        n=len(grid[0])
        q.append([(0,0),grid[0][0]])

        while q:
            point,value=q.popleft()
            if point==(m-1,n-1):
                answer.append((value))
            x,y=point
            r_x,r_y=(x,y+1)
            d_x,d_y=(x+1,y)
            if 0<=r_x<m and 0<=r_y<n:
                q.append([(r_x,r_y),value+grid[r_x][r_y]])
            if 0<=d_x<m and 0<=d_y<n:
                q.append([(d_x,d_y),value+grid[d_x][d_y]])

        return min(answer)

            
       

            
            

        
        

solution=Solution()
solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]])