class Solution:
    def unionAndIntersection(self,arr1,arr2):
        set1 = set(arr1)
        set2 = set(arr2)
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return union, intersection
    
    def unionAndIntersection(self,arr1,arr2):
        n = len(arr1)
        m = len(arr2)
        i = j = 0
        union = []
        intersection = []
        while i < n and j < m:
            if(arr1[i] == arr2[j]):
                union.append(arr1[i])
                intersection.append(arr1[i])
                i += 1
                j += 1
            elif(arr1[i] < arr2[j]):
                union.append(arr1[i])
                i += 1
            else:
                union.append(arr2[j])
                j += 1
        while i < n:
            union.append(arr1[i])
            i += 1
        while j < m:
            union.append(arr2[j])
            j += 1
        return union, intersection            
