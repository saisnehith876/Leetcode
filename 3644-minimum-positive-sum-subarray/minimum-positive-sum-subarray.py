class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        n = len(nums)
        ans = float('inf')

        for i in range(n):                      # start of the chunk
            s = 0
            for j in range(i, min(n, i + r)):   # end of the chunk, at most r long
                s += nums[j]                    # running sum, no re-adding
                length = j - i + 1
                if length >= l and s > 0:       # long enough and positive
                    ans = min(ans, s)

        return -1 if ans == float('inf') else ans