import math
class Solution:
    def findRank(self, S):
        count = [0] * 257
        lenOfStr = len(S)
        mul = math.factorial(lenOfStr)
        rank = 1

        for i in range(lenOfStr):
            count[ord(S[i])] += 1
            
        for i in range(1, len(count)):
            count[i] += count[i - 1]
            
        for i in range(lenOfStr):
            mul = mul // (lenOfStr - i)
            rank += count[ord(S[i]) - 1] * mul
            
            for j in range(ord(S[i]), len(count)):
                count[j] -= 1
                
        return rank
