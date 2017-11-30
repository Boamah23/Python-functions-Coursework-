def deleteNode(tree, value):
    if(tree == None): #checks if tree is empty
       return tree
    elif(value < tree.value): #checks if the value is less than the value of root
       tree.left = deleteNode(tree.left, value) #recursive function that will delete the value on the left side of the tree
    elif(value > tree.value): #checks if value is greater than value of root
        tree.right = deleteNode(tree.right, value) #recursive function that will delete the value on the right side of the tree
    else:
        if(tree.left == None and tree.right == None): #checks if there is no child
            del(tree) #deletes node
            tree = None
        elif(tree.left == None): #checks if there is only one child
            tree.temp = tree #stores address of current node to be deleted in temporary pointer
            tree = tree.right #moves root to right child
            del tree.temp #deletes the node being pointed to
        elif(tree.right == None):
            tree.temp = tree
            tree = tree.left
            del tree.temp
        else:
            tree.temp = min(tree.right) #if there is two children find minimum value in the right subtree
            tree.value = tree.temp.value
            tree.right = deleteNode(tree.right, tree.temp.value)
