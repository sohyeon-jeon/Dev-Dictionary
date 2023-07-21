from typing import List
from itertools import permutations

# 투 포인터 이용


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값은 건너뜁니다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    # 중복된 값은 건너뜁니다.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return answer


# 예상대로 타임아웃~
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_list = []
        for p in permutations(nums, 3):
            if sum(p) == 0:
                sum_list.append(sorted(list(p)))
        unique_list = [list(t) for t in {tuple(row) for row in sum_list}]
        return unique_list


# [[-1,-1,2],[-1,0,1]]
solution = Solution()
solution.threeSum([-1, 0, 1, 2, -1, -4])
