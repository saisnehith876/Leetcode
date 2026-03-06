class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        ##edge case - if str starts with 0 return false
        if s[0] =='0' :return False

        for i in range (len(s)-1):
            if s[i] == '0' and s[i+1]=='1':
                return False

        return True


            