class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            prev = fast.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
        
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                    prev = prev.next
                
                prev.next = None
                return
