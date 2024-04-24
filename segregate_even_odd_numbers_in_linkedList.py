class Solution:
    def segregateList(self, head):
        evenHead = None
        oddHead = None
        evenP = None
        oddP = None
        pointer = head
        while pointer:
            if pointer.data % 2 == 0:
                if evenHead:
                    evenP.next = pointer
                    evenP = evenP.next
                else:
                    evenHead = pointer
                    evenP = evenHead
            else:
                if oddHead:
                    oddP.next = pointer
                    oddP = oddP.next
                else:
                    oddHead = pointer
                    oddP = oddHead
            pointer = pointer.next
        oddP.next = None
        evenP.next = oddHead
        return evenHead