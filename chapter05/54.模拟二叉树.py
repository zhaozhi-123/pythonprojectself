"""
树结构解释：
    概述：
        它属于数据结构的一种，属于非线性结构（N个前驱，N个后续）
    特点：
        1.有且只能有1个根节点.
        2.每个节点都司以有1个父节点及任意个产货点，根节点除外(没有父节点)
        3.没有子节点的节点，称之为：叶子分点。
    常用分类：
        无序树：
        有序树：
        二叉树：
            完全二叉树：最后一层不满，其它都是满的.
            满_叉网：都是满的。
            非完全叉树：中间有断的.
            平衡_叉树：任意节点的两个子树的高度差不超过1

            我们用的最多的就是：二叉树
            存储：
                顺序存储：既要存储数据，又要存储劳点的关系。
                链式存储：采用节点（item,lchild,rchild)的方式，形成链表来存储
"""

#定义Node类，表示二叉树的节点
class Node(object):
    def __init__(self,item):
        self.item=item      #元素域
        self.lchild=None    #左子结点
        self.rchild=None    #右子结点

#定义BinaryTree类，表示二叉树
class BinaryTree:
    def __init__(self,node=None):
        self.root=node          #根结点

    #定义add函数，添加结点
    def add(self,item):
        #把item封装成节点
        new_node = Node(item)
        #判断根结点是否为空，若为空，则把该节点作为根结点
        if self.root is None:
            self.root = new_node
            return      #核心
        #创建队列，添加根结点到队列中
        queue = []
        queue.append(self.root)
        #通过while True循环,找到空缺的节点位置
        while True:
            #获取队列中的第一个元素
            node = queue.pop(0)
            #判断该节点的左右子树是否为空
            if node.lchild is None:
                #把新节点设置为该节点的左子树
                node.lchild = new_node
                return
            else:
                #把当前节点的左子树加入队列
                queue.append(node.lchild)

            #判断该节点的右子树是否为空
            if node.rchild is None:
                node.rchild = new_node
                return
            else:
                queue.append(node.rchild)


    #广度优先遍历：一层一层向外扩散
    def breadth_travel(self):
        #判断根节点是否为空。
        if self.root is None:
            return
        #创建队列，添加 根节点到队列中
        queue = []
        queue.append(self.root)
        #循环打印内容，只要队列不为空，就一直遍历
        while len( queue)!=0:
            #获取队列中的第一个元素
            node = queue.pop(0)
            #打印元素
            print(node.item,end=' ')
            #判断该节点的左子树是否为空
            if node.lchild is not None:
                #把左子树加入队列
                queue.append(node.lchild)
            #判断该节点的右子树是否为空
            if node.rchild is not None:
                queue.append(node.rchild)


    #深度优先遍历：一条路走到黑
    # 先序：根结点-》左子树-》右子树

    # 定义preorder函数，深度优先遍历之先序遍历
    def preorder_travel(self,root):
        #判断根节点是否为空，若不为空，则打印
        if root is not None:
            #打印根节点的元素域
            print(root.item,end=' ')
            #递归遍历左子树
            self.preorder_travel(root.lchild)
            #递归遍历右子树
            self.preorder_travel(root.rchild)

    #中序：左子树-》根结点-》右子树

    # 定义inorder函数，深度优先遍历之中序遍历
    def inorder_travel(self,root):
         if root is not None:
            #递归遍历左子树
            self.inorder_travel(root.lchild)
            #打印根节点的元素域
            print(root.item,end=' ')
            #递归遍历右子树
            self.inorder_travel(root.rchild)

        #后序：左子树-》右子树-》根结点
    # 定义postorder函数，深度优先遍历之后序遍历
    def postorder_travel(self,root):
        if root is not None:
            #递归遍历左子树
            self.postorder_travel(root.lchild)
            #递归遍历右子树
            self.postorder_travel(root.rchild)
            #打印根节点的元素域
            print(root.item,end=' ')

    # 测试代码
    def dm01_tree(self):
        #创建节点
        node1 = Node('A')
        # 打印节点的元素域，左子树，右子树
        print(node1.item)   #A
        print(node1.lchild) #None
        print(node1.rchild) #None
        # 测试二叉树
        # bt=BinaryTree()   #空的
        # print(bt.root)    #None
        bt = BinaryTree(node1)
        print(bt.root)  # 根节点（的地址）
        print(bt.root.item)  # 根节点的元素域（A）

    #测试：广度优先遍历
    def method_bfs(self):
        bt = BinaryTree()
        # 添加元素
        bt.add('A')
        bt.add('B')
        bt.add('C')
        bt.add('D')
        bt.add('E')
        bt.add('F')
        bt.add('G')
        bt.add('H')
        bt.add('I')
        bt.add('J')

        # 广度优先遍历
        bt.breadth_travel()


    def method_dfs(self):
        # 创建二叉树对象
        bt = BinaryTree()
        bt.add(0)
        bt.add(1)
        bt.add(2)
        bt.add(3)
        bt.add(4)
        bt.add(5)
        bt.add(6)
        bt.add(7)
        bt.add(8)
        bt.add(9)
        # 深度优先遍历
        print('先序（根左右）：', end='')
        bt.preorder_travel(bt.root)

        print('中序（左根右）：', end='')
        bt.inorder_travel(bt.root)

        print('后序（左右根）：', end='')
        bt.postorder_travel(bt.root)

    if __name__ == '__main__':
        print(666)
