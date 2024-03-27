class Solution:
    def detectLoop(self, head):
        slowPointer = head
        fastPointer = head.next
        while(slowPointer != None and fastPointer != None):
            if(slowPointer == fastPointer):
                return True
            else:
                slowPointer = slowPointer.next
                fastPointer = fastPointer.next.next
        return False
