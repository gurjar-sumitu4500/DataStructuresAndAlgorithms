import math
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False

    def _r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, currentNode, value):
        if currentNode == None:
            return False
        if currentNode.value == value:
            return True
        elif value < currentNode.value:
            return self.__r_contains(currentNode.left, value)
        elif value > currentNode.value:
            return self.__r_contains(currentNode.right, value)
        
    def _r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def __r_insert(self, currentNode, value):
        if currentNode == None:
            return Node(value)
        if value < currentNode.value:
            currentNode.left = self.__r_insert(currentNode.left, value)
        if value > currentNode.value:
            currentNode.right = self.__r_insert(currentNode.right, value)
        return currentNode
    
    def min_value(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def _r_delete(self, value):
        self.__r_delete(self.root, value)
    
    def __delete_node(self, currentNode, value):
        if currentNode == None:
            return False
        
        if value < currentNode.value:
            currentNode.left = self.__delete_node(currentNode.left, value)
        elif value > currentNode.value:
            currentNode.right = self.__delete_node(currentNode.right, value)
        else:
            if currentNode.left == None and currentNode.right == None:
                return None
            if currentNode.left == None:
                currentNode = currentNode.right
            if currentNode.right == None:
                currentNode = currentNode.left
            else:
                subTreeMin = self.min_value(currentNode.right)
                currentNode.value = subTreeMin
                currentNode.right = self.__delete_node(currentNode.right, subTreeMin)
        return currentNode
    
    def invert(self):
        if self.root == None:
            return None
        self.invertTree(self.root)
        return self.root
    
    def invertTree(self, node):
        if node == None:
            return None
        else:
            left = node.left
            node.left = self.invertTree(node.right)
            node.right = self.invertTree(left)
            return node
    
    def BFS(self):
        currentNode = self.root
        queue = []
        result = []
        queue.append(currentNode)
        while len(queue) > 0:
            currentNode = queue.pop(0)
            result.append(currentNode.value)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
        return result

# myTree = BinarySearchTree()
# myTree.insert(47)
# myTree.insert(21)
# myTree.insert(76)
# myTree.insert(18)
# myTree.insert(27)
# myTree.insert(52)
# myTree.insert(82)
# print(myTree.BFS())
            