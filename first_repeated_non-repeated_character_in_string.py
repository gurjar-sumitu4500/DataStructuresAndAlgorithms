class Solution:
    def firstRepChar(self, s):
        hashmap = {}
        for i in s:
            if i in hashmap:
                return i
            else:
                hashmap[i] = 1
        return -1   
    
    def nonrepeatingCharacter(self,s):
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in s:
            if hashmap[j] == 1:
                return j
        return '$'
