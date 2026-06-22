from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count chars in given text and stor them
        # compare them with ballon
        #if b->2 , a->2 l->4 o-3, n-2 output should be 1 because shoertage od o
        count = Counter(text)
        return min(
            count['b'],
            count['a'],
            count['l']//2,
            count['o']//2,
            count['n']
        )
        