###### Lomuto Partition
def partition(self, arr, start, end, pivot):
        j = start
        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[j], arr[end] = arr[end], arr[j]
        return j
        
        
    def lomutoQuickSort(self, arr, start, end):
        if start < end:
            pivot = arr[end]
            partition = self.partition(arr, start, end, pivot)
            self.lomutoQuickSort(arr, start, partition - 1)
            self.lomutoQuickSort(arr, partition + 1, end)
            return arr
        else:
            return arr


###### Hoare Partition
def hoareQuickSort(self, arr, start, end):
        if start < end:
            pivot = arr[start]
            i = start - 1
            j = end + 1
            while True:
                i += 1
                while arr[i] < pivot:
                    i += 1
                j -= 1
                while arr[j] > pivot:
                    j -=1
                
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
            self.hoareQuickSort(arr, start, j)
            self.hoareQuickSort(arr, j + 1, end)
            return arr
        return arr
