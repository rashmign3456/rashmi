class Node:
    def _init_(self,data):
        self.data = data
        self.right =   None
        self.left = None

n=int(input())
num=list(map(int,input().split()))
k=int(input())

def fillInorder(inorder,root):
    if root==None:
        return
    fillInorder(inorder,root.left)
    inorder.append(root.data)
    fillInorder(inorder,root.right)
    
def insertIntoBST(root,ele):
    if root==None:
        new=Node(ele)
        return new
    if root.data<ele:
        root.right=insertIntoBST(root.right,ele)
    else:
        root.left=insertIntoBST(root.left,ele)
    return root

root=None
for ele in num:
    root=insertIntoBST(root,ele)
    
inorder=[]
fillInorder(inorder,root)
print(inorder[k-1])
