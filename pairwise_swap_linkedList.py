def pairwiseSwap(self, head):
        p = head
        while p:
            pdata = p.data
            temp = p.next
            p.data = temp.data
            temp.data = pdata
            p = temp.next
        return head