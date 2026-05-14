"""
链表介绍：
    概述：
        它属于数据结构之 线性结构中的一种，每个节点都只可能有1个前驱和1个后继节点
    作用：
        用于优化顺序表的弊端（如果没有足够的连续内存空间，会导致扩容失败
        链表扩容是，有地儿就行，连不连续无所谓
    组成：
        由 节点组成，其中节点由元素域（数值域）和链接域
    分类：
        根据节点类型不同，链表主要分为：
        单项链表：节点由1个数值域和1个地址域组成，卡岸边节点的地址域 存储的是后续节点
        单项循环链表：
        双向循环链表：
        双向循环链表

自定义迪马模拟链表，思路分析：
    1.自定义SingleNode类，表示节点类
        属性：
            item    数值域（元素域）
            next    地址域（链接域）
    2.自定义SingleLinkedList类，表示：链表
        属性：
            head 表示头节点，执行第一个节点
        行为：
            isEmpty（）判断链表是否为空
            length（）获取链表长度
            travel（）遍历链表
            add()链表头部添加元素
            append()链表尾部添加元素
            insert（）指定位置添加元素
            remove（）删除节点
            search（）查找结点是否存在

"""

#1.自定义SingleNode类
class SingleNode:
    def __init__(self, item):
        self.item=item
        self.next=None

class SingleLinkedList:
    def __init__(self,node=None):
        self.head=node  #链表的头节点，指向第一个节点

    #   isEmpty（）判断链表是否为空
    def is_empty(self):
        #思路：判断头节点是否为None，如果为None，则链表为空
        #写法1
        # if self.head is None:
        #     return True
        # else:
        #     return False
        #2.写法2：三元表达式
        return True if self.head is None else False
        #写法3：
        # return self.head is None

    #   length（）获取链表长度
    def length(self):
        #1.创建游标（表示当前节点）默认从头节点开始
        cur=self.head
        #2.定义计数器
        count=0
        #3.开始遍历，只要当前节点不为空，就一直循环
        while cur is not None:
            count+=1
            cur=cur.next
        #循环结束，列表长度已经获取了，返回即可
        return count

    #   travel（）遍历链表
    def travel(self):
        #1.创建游标，默认从头节点开始
        cur=self.head
        while cur is not None:
            print(cur.item)
            cur=cur.next

    #   add()链表头部添加元素
    def add(self,item):
        # 封装新节点
        new_node = SingleNode(item)
        # 2.判断列表如果为空，直接设置当前节点为头节点
        if self.is_empty():
            self.head = new_node
        else:
            #到这里说明链表不为空，
            # 1.将新节点的地址域指向旧节点头
            new_node.next=self.head
            self.head = new_node

    #   append()链表尾部添加元素
    def append(self,item):
        # 封装新节点
        new_node = SingleNode(item)
        # 2.判断列表如果为空，直接设置当前节点为头节点
        if self.is_empty():
            self.head = new_node
        else:
            # 走到这里说明列表不为空，需要找到尾节点
            # 创建游标（表示当前节点），默认从头结点开始
            cur = self.head
            # 开始遍历，只要当前节点不为空，就一直循环
            while cur.next is not None:
                cur = cur.next
            # 到这里说明cur就是最后一个节点，设置他的地址域指向新节点即可
            cur.next = new_node

    #   insert（）指定位置添加元素
    def insert(self,pos,item):
        #1.判断索引是否越界，如果<=0往前加
        if pos<=0:
            self.add(item)
        elif pos>=self.length():
            self.append(item)
        else:
            #走到这里，说明索引合法，，即中间的值，
            #创建游标（表示当前节点），默认从头结点开始
            cur=self.head
            #定义变量，记录当前节点的位置
            count=0
            #开始遍历，只要当前节点的位置<pos，就一直循环
            while count<pos-1:
                #
                cur=cur.next
                count+=1
            #走到这里说明，cur就是插入节点前的那个节点，先封装内容为新节点
            new_node=SingleNode(item)
            new_node.next=cur.next
            cur.next=new_node



    #   remove（）删除节点
    def remove(self,item):
        #1.创建游标，表示当前节点，默认从头结点开始
        cur=self.head
        #2.定义变量，记录要删除节点的前驱节点
        pre=None
        #3.循环遍历，只要当前节点不为空，就一直循环
        while cur is not None:
            #4.判断当前节点是否是要删除的节点
            if cur.item == item:
                #5.判断要删除的节点是否是头节点
                if cur==self.head:
                    #6.直接设置头节点为当前节点的下个节点
                    self.head=cur.next
                else:
                    #7.到这里说明要删除的节点不是头节点，直接设置前驱节点的地址域指向当前节点的下一个
                    pre.next=cur.next
                    cur.next=None
                return
            else:
                #8。走到这里说明当前节点不是要删除的节点，游标后移
                pre=cur
                cur=cur.next

    #   search（）查找结点是否存在
    def search(self,item):
        #1.定义游标(表示当前节点，默认从头开始）
        cur=self.head
        while cur is not None:
            if cur.item == item:
                #找到了
                return True
            #没找到接着找
            cur=cur.next
        #都找完没找到，
        return False









if __name__ == '__main__':

    #测试节点类
    node1=SingleNode(10)
    print(f'元素域',node1.item)
    print(f'链接域',node1.next)
    print('node1的类型：',type(node1))

    #测试链表类
    my_linked_list=SingleLinkedList()
    print(f'头节点为：{my_linked_list.head}')    #None
    my_linked_list1=SingleLinkedList(node1)
    print(f'头节点为：{my_linked_list1.head}')

    print(f'头节点的元素域：{my_linked_list1.head.item}')   #10
    print(f'头结点的地址域：{my_linked_list1.head.next}')   #None
    print('*'*20)


    #4.完整测试
    node1=SingleNode('乔峰')
    #2.将节点作为头节点，创建链表
    my_linked_list2=SingleLinkedList(node1)
    #3.打印头节点
    print(f'头节点为：{my_linked_list2.head}')
    print(f'头节点的数值域为：{my_linked_list2.head.item}')
    print('*'*20)

    #4.测试链表是否为空
    print(my_linked_list2.is_empty())


    #测试添加
    my_linked_list2.add('111')
    my_linked_list2.add('333')

    # 测试链表尾添加
    my_linked_list2.append('222')

    #测试插入链表
    my_linked_list2.insert(2,'555')

    #测试删除
    my_linked_list2.remove('555')

    #测试获取列表长度
    print(my_linked_list2.length())
    print('*'*20)



    #测试遍历链表

    my_linked_list2.travel()
    print('*'*20)





