class Solution:
    def findMid(self, head):
        sp = fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        return sp.data
