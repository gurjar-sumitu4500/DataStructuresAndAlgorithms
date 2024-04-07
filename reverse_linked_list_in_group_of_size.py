class Solution:
    def reverseList(self, head, k):
        if head == None: 
          return None
        current = head 
        next = None
        prev = None
        count = 0
  
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
            count += 1
  
        if next is not None: 
            head.next = self.reverseList(next, k) 
  
        return prev 