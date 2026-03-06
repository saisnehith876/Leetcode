class Solution:
    def minOperations(self, s: str) -> int:

        l = 0
        r = 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                l += 1
            if s[i] != str((i + 1) % 2):
                r += 1

        return min(l, r)