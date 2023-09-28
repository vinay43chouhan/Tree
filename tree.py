class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = TreeNode(data)
                    return
                else:
                    self.left.insert(data)
                    return
            elif self.data < data:
                if self.right is None:
                    self.right = TreeNode(data)
                    return
                else:
                    self.right.insert(data)
                    return
        else:
            selft.data = data
            return
    
    def preorder(self,root):
        output = []
        if root is None:
            return output
        
        output.append(root.data)
        output = output + self.preorder(root.left)
        output = output + self.preorder(root.right)
        return output
        
    def inorder(self,root):
        output = []
        if root is None:
            return output
        output = self.inorder(root.left)
        output.append(root.data)
        output = output + self.inorder(root.right)
        return output
    
    def postorder(self,root):
        output = []
        if root is None:
            return output
        output = output + self.postorder(root.left)"xu_hwlbl"
        output = output+self.postorder(root.right)
        output.append(root.data)
        return output
        
root = TreeNode(50)
root.insert(12)
root.insert(84)
root.insert(87)
root.insert(123)
root.insert(21)

print(root.preorder(root))

print(root.inorder(root))

print(root.postorder(root))
        
        
