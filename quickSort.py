class Solution:
    def conquer(self, arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1
    
    def sort(self, arr, start, end):
        if start < end:
            pivotIndex = self.conquer(arr, start, end)
            self.sort(arr, start, pivotIndex - 1)
            self.sort(arr, pivotIndex + 1, end)
        
    def quickSort(self, arr):
        self.sort(arr, 0, len(arr) - 1)
        return arr
