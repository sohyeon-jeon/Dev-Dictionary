# 132ms / 16.27mb
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def lookup(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        if len(s) <= 1 or s == s[::-1]:
            return s
        ans = ""
        for i in range(len(s) - 1):
            # 홀수 길이와 짝수 길이 팰린드롬을 각각 찾는다.
            ans = max(ans, lookup(s, i, i + 1), lookup(s, i, i + 2), key=len)
        return ans


"""
팰린드롬이 되는 경우 -> 문자 길이가 짝수인 경우와 홀수인 경우
중간점이 되는 부분을 시작으로 점차 늘려나가 큰 회문이 되게 한다.
"""


# 5345 ms / 16.3 MB
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) + 1
        p_s = len(s)

        while p_s > 0:
            for i in range(n - p_s):
                temp = s[i : i + p_s]
                if temp == temp[::-1]:
                    return temp
            p_s -= 1


solution = Solution()
solution.longestPalindrome("babad")
