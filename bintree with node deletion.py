class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        self.temp=None
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def locateMin(self, tree):
    while(tree.left != None):
        tree = tree.left
        return tree

def deleteNode(tree, value):
    if(tree == None):
       return tree
    elif(value < tree.value):
       tree.left = deleteNode(tree.left, value)
    elif(value > tree.value):
        tree.right = deleteNode(tree.right, value)
    else:
        if(tree.left == None and tree.right == None):
            del(tree)
            tree = None
        elif(tree.left == None):
            tree.temp = tree
            tree = tree.right
            del tree.temp
        elif(tree.right == None):
            tree.temp = tree
            tree = tree.left
            del tree.temp
        else:
            tree.temp = min(tree.right)
            tree.value = tree.temp.value
            tree.right = deleteNode(tree.right, tree.temp.value)

    return tree
 
t=tree_insert(None,6);
tree_insert(t,10)
tree_insert(t,5)
tree_insert(t,2)
tree_insert(t,3)
tree_insert(t,4)
tree_insert(t,11)
deleteNode(t,5)
in_order(t)
