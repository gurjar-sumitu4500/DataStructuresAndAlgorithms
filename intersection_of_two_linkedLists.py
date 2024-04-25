class Solution:
    def findIntersection(self, head1, head2):
        p1 = head2
        p2 = head1
        hashmap = {}
        intersection = LinkedList()
        while p1:
            if p1.data not in hashmap:
                hashmap[p1.data] = 0
            p1 = p1.next
        while p2:
            if p2.data in hashmap:
                intersection.push(p2.data)
            p2 = p2.next
        return intersection.head