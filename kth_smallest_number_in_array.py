import sys

class Solution:
    def count_less_than_or_equal(self, nums, mid):
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        return count
    
    def kth_smallest(self, nums,l, r, k):
        min_val = float('inf')
        max_val = float('-inf')
        for num in nums:
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        while min_val < max_val:
            mid = min_val + (max_val - min_val) // 2
            count = self.count_less_than_or_equal(nums, mid)
            if count < k:
                min_val = mid + 1
            else:
                max_val = mid
        return min_val
