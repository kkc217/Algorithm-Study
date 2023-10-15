import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        dict_str = collections.Counter(s)
        odd = False
        # 하나의 알파벳만 주어지면 그 개수가 모두 answer
        # 짝수는 모두 포함시키기
        # 홀수가 존재하면 하나만 더하기
        for value in dict_str.values():
            answer += value // 2 * 2

            if value % 2 == 1:
                odd = True
        if odd:
            answer += 1

        return answer
