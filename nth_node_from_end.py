class Solution:
    def getNthFromLast(self, head, n):
        fp = head
        sp = head
        for i in range(n-1):
            if(fp.next == None):
                return -1
            fp = fp.next
        while fp.next:
            fp = fp.next
            sp = sp.next
        return sp.data
