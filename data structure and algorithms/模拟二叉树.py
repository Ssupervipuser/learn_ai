"""
概述：
    他数据数据结构的一种，属于非线性结构（n个前驱，n个后继）
特点：
    1.有且只能有一个根节点
    2.每个节点都可以有1个父节点，以及任意一个子节点，根节点除外
    3.没有子节点的节点，称之为叶子节点

常用分类
    无序树：
    有序树
    二叉树
            完全二叉树:最后一层不满，其他都是满的
            满二叉树：都是满的
            非完全二叉树：中间有断的
            平衡二叉树：任意节点的两个子树的高度不超过1

    存储：
        顺序存储：既要存储数据，又要存储节点的关系
        链式存储，采用节点（item,lchild,rchild)的方式，形成列表来存储
"""

#1.定义Node类，表示二叉树的节点
class Node:
    #初始化属性
    def __init__(self, item):
            self.item = item        #元素域，
            self.lchild = None      #左子节点
            self.rchild = None      #右子节点

#2.自定义BinaryTree类，表示二叉树

class BinaryTree:
    def __init__(self,node=None):
        self.root = node    #根节点，类似于

    #2.定义add函数表示添加节点
    def add(self,item):
        #1.把item 封装成节点
        new_node = Node(item)
        #2.判断根节点是否为空，如果为空，设置当前节点为根节点
        if self.root is None:
            self.root = new_node
            return
        #3.创建队列，添加根节点到队列中
        queue=[]
        queue.append(self.root)
        #4.通过while循环找到空缺的节点位置
        while True:
            #5.获取队列的第1个元素
            node=queue.pop(0)
            #6.判断当前节点的左子树是否为空
            if node.lchild is None:
                #6.1把新节点设置为当前节点的左子树，并结束
                node.lchild=new_node
                return
            else:
                #6.2走到这里，说明左子树不为空，把当前节点的左子树，添加到队列中
                queue.append(node.lchild)

            #7.判断当前节点的右子树是否为空
            if node.rchild is None:
                #7.1把当前节点设置为当前节点的右子树，并结束
                node.rchild=new_node
                return
            else:
                #走到这里说明右子树不为空，把当前节点的右子树，添加到队列中
                queue.append(node.rchild)

    #3.定义breadth（）函数，表示过度优先遍历（逐层遍历，
    def breadth(self):
        #1.判断根节点是否为空
        if self.root is None:
            return
        #2.创建队列，添加根节点到队列中
        queue=[]
        queue.append(self.root)
        #3.循环打印内容，只要队列不为空，就一直遍历
        while len(queue)!=0:
            #4.获取队列的第一个元素
            node=queue.pop(0)
            #5.打印该节点的元素域
            print(node.item,end=' ')
            #6.判断当前节点的左子树是否存在，存在就添加到队列中
            if node.lchild is not None:
                queue.append(node.lchild)
            #7.
            if node.rchild is not None:
                queue.append(node.rchild)

    #4.定义preorder（）函数，表示深度优先值先序遍历(跟左右）
    def preorder(self,root):
        #1.判断根节点是否不为空，不为空就打印
        if root is not None:
            #2.打印根节点的元素域
            print(root.item,end=' ')
            #3.递归遍历左子树
            self.preorder(root.lchild)
            self.preorder(root.rchild)


    #5.定义inorder（）函数，表示深度优先之中序遍历（左根右）
    def inorder(self,root):
        # 1.判断根节点是否不为空，不为空就打印
        if root is not None:
            # 2.递归遍历左子树
            self.inorder(root.lchild)
            # 3.打印根节点的元素域
            print(root.item, end=' ')
            #4.
            self.inorder(root.rchild)

    #6.定义postorder（）函数，表示深度优先值后序遍历(左右根）
    def postorder(self,root):
        # 1.判断根节点是否不为空，不为空就打印
        if root is not None:
            # 4.递归遍历左子树
            self.postorder(root.lchild)
            #2.
            self.postorder(root.rchild)
            # 3.打印根节点的元素域
            print(root.item, end=' ')


def dem01():
    # 1.创建节点
    node1 = Node('A')
    # 2.打印节点的元素域，左子树，右子树
    print(node1.item)
    print(node1.lchild)
    print(node1.rchild)
    print('-' * 23)
    # 3.测试二叉树
    bt = BinaryTree()
    print(bt.root)

    bt = BinaryTree(node1)
    print(bt.root)
    print(bt.root.item)


def dem02模拟队列获取元素():
    # 1.创建队列，特点，先进先出
    queue = []
    # 2.模拟往队列中添加元素
    queue.append('A')
    queue.append('B')
    queue.append('C')

    # 3.模拟队列中去除元素
    print(queue.pop(0))  # 删除索引为0的元素，并返回该元素
    print(queue.pop(0))
    print(queue.pop(0))

    # 4.打印队列
    print(queue)


def dem03广度优先遍历():
    # 1.创建二叉树对象
    bt = BinaryTree()
    # 2.添加元素
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
    # 3.广度优先遍历

    bt.breadth()


if __name__ == '__main__':


    # dem01()

    # dem02模拟队列获取元素()

    # dem03广度优先遍历()

    #1.创建二叉树对象
    bt=BinaryTree()
    #2.添加元素
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
    #3.深度优先遍历
    print('深度先序遍历')
    bt.preorder(bt.root)
    print('深度中序遍历')
    bt.inorder(bt.root)
    print('深度后序遍历')
    bt.postorder(bt.root)

