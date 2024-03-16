class Solution: 
    def subArrayExists(self,arr,n, s):
        prefix_sum = {}
        prevSum = 0
        for i in range(n):
            prevSum += arr[i]
            if prevSum == s:
                return [0, i]
            if (prevSum - s) in prefix_sum:
                return [prefix_sum[prevSum - s] + 1, i]
            prefix_sum[prevSum] = i
        return []
