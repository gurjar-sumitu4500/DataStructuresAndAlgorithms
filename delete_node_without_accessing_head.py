def deleteNode(self,del_node):
        data = del_node.next.data
        ref = del_node.next.next
        del_node.next.next = None
        del_node.next = ref
        del_node.data = data
