
class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil
class RBTreeNode(object):
    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size = None
#左旋
def LeftRotate(T,x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

#右旋
def RightRotate(T,x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

#红黑树的插入
def RBInsert(T,z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else :
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'red'
    RBInsertFixup(T,z)
    return z.key,'颜色为',z.color

#给红黑树上色
def RBInsertFixup(T,z):
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.righ
            if y.color == 'red':
                y.parent.color = 'black'
                y.color = 'black'
                y.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    LeftRotate(T,z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                RightRotate(T,z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    RightRotate(T,z)
                z.parent.color='black'
                z.parent.parent.color = 'red'
                LeftRotate(T, z.parent.parent)
    T.root.color = 'black'
def RBTransplant(T,u,v):
    if u.parent == T.nil:
        T.root = v;
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent