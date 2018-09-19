class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        """
          This should only be a node object or None
        """
        if value is None or type(value) is Node:
            self._left = value
            return
        raise Exception("The left node must be of type Node or None.")

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        """ This should only be a node object or None  """
        if value is None or type(value) is Node:
            self._right = value
            return
        raise Exception("The right node must be of type Node or None.")


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def add_node(self, new_node):
        if self.root is None:
            self.root = new_node
            return
        self.check_node(self.root, new_node)

    def check_node(self, existing_node, new_node):
        if new_node.value < existing_node.value:
            if existing_node.left is None:
                existing_node.left = new_node
                return
            else:
                return self.check_node(existing_node.left, new_node)
        else:
            if existing_node.right is None:
                existing_node.right = new_node
                return
            else:
                return self.check_node(existing_node.right, new_node)
