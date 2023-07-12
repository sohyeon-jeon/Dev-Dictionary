'''
https://leetcode.com/problems/largest-values-from-labels/
'''
from typing import List
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        used_count = defaultdict(int)
        total_value = 0

        for val, label in sorted(zip(values, labels), reverse=True):

            if not num_wanted:
                break

            if used_count[label] >= use_limit:
                continue

            used_count[label] += 1

            num_wanted -= 1
            total_value += val

        return total_value
    
solution=Solution()
solution.largestValsFromLabels([5,4,3,2,1],[1,1,2,2,3],3,1)