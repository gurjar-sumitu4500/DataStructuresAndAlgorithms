class Solution:
    def maxLen(self, n, arr):
        hashmap = {}
        sum = 0
        count = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                count = max(i+1, count)
            if sum in hashmap:
                count = max(i - hashmap[sum], count)
            else:
                hashmap[sum] = i
        return count
