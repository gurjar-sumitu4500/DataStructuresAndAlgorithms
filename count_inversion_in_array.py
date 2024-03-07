def countInversions(self, arr,n):
        inversions = 0
        tempArr = []
        for i in range(n):
            tempArr.append(arr[i])
            tempArr.sort()
            last_index = len(tempArr) - tempArr[::-1].index(arr[i]) - 1
            inversions += len(tempArr) - last_index - 1        
        return inversions
