  
class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value

        current_node = self

        def insert_node(node, value):
                
            if value > node.value:
                if node.right is None:
                    node.right = BinarySearchTree(value)
                else:
                    insert_node(node.right, value)

            elif value < node.value:
                if node.left is None:
                    node.left = BinarySearchTree(value)
                else:
                    insert_node(node.left, value)
                
            else: # The values are identical
                print(f"Duplicate: {value}")
        
        insert_node(current_node, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None: 
            return False

        current_node = self

        while current_node is not None:
            if current_node.value == target:
                return True
            elif current_node.value > target:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return False
                

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return
        else:
            current_node = self
            max_val = current_node.value
            while current_node is not None:
                if current_node.value > max_val:
                    max_val = current_node.value
                
                current_node = current_node.right
            
            return max_val

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is None:
            return
        
        def for_each_node(node):
            if node.value is not None:
                cb(node.value)
            
            if node.left is not None:
                for_each_node(node.left)
            
            if node.right is not None:
                for_each_node(node.right)

        for_each_node(self)