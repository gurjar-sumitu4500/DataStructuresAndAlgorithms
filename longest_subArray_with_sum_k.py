class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        pref_sum = {}
        count = 0
        prev_sum = 0
        for i in range(n):
            prev_sum += arr[i]
            if (prev_sum - k) in pref_sum:
                count = max(i - pref_sum[prev_sum - k], count)
            if prev_sum == k:
                count = max(i + 1, count)
            if prev_sum not in pref_sum:
                pref_sum[prev_sum] = i
        return count
