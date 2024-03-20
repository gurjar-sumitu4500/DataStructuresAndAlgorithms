from collections import defaultdict
class Solution:
    def countDistinct(self, A, N, K):
        hashmap = defaultdict(lambda: 0)
        result = []
        count = 0
        for i in range(K):
            if hashmap[A[i]] == 0:
                count += 1
            hashmap[A[i]] += 1
        result.append(count)
        
        for j in range(K, N):
            if hashmap[A[j-K]] == 1:
                count -= 1
            hashmap[A[j-K]] -= 1
            
            if hashmap[A[j]] == 0:
                count += 1
            hashmap[A[j]] += 1
            result.append(count)
        return result
