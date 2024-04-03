class Solution:
    def reverseList(self, head):
        curr = head
        next = head.next
        temp = None
        while next:
            curr.next = temp
            temp = curr
            curr = next
            next = curr.next
        curr.next = temp
        temp = curr
        return temp
