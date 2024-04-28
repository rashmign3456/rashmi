class node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None
n = int(input())
nums = list(map(int,input().split()))

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data,end = " ")
    inorder(root.right)

def insert(root,ele):
    if root == None:
        new = node(ele)
        return new

    if root.data < ele :
        root.right = insert(root.right,ele)
    else:
        root.left = insert(root.left,ele)
    return root

root = None
for ele in nums:
    root = insert(root,ele)
inorder(root)
