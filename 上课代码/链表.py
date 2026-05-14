# # # class SingleNode:
# # #     def __init__(self,item):
# # #         self.item=item
# # #         self.next=None
# # #
# # # class SingleLinkedList:
# # #     def __init__(self,node=None):
# # #         self.head=node
# # #
# # #     def is_empty(self):
# # #         # 链表是否为空
# # #         self.head is None
# # #
# # #     def length(self):
# # #         # 链表长度
# # #         pass
# # #
# # #     def travel(self):
# # #         # 遍历整个链表
# # #         # 1.设置游标
# # #         cur = self.head
# # #         # 2.只要当前节点不为空,就一直循环
# # #         while cur is not None:
# # #             # 3.打印当前节点的数值域
# # #             print(f"数值域:{cur.item}")
# # #             # 4.修改当前节点,动起来
# # #             cur = cur.next
# # #
# # #     def add(self, item):
# # #         # 链表头部添加元素
# # #         # 1.创建一个新的节点
# # #         new_node = SingleNode(item)
# # #         # 2.设置新节点的地址域指向头节点变量
# # #         new_node.next = self.head
# # #         # 3.设置头结点指向新节点
# # #         self.head = new_node
# # #
# # #     def append(self, item):
# # #         # 链表尾部添加元素
# # #         pass
# # #
# # #     def insert(self, pos, item):
# # #         # 指定位置添加元素
# # #         pass
# # #
# # #     def remove(self, item):
# # #         # 删除节点
# # #         cur=self.head
# # #         pre=None
# # #         while cur is not None:
# # #             if cur.item==item:
# # #                 if cur==self.head:
# # #                     self.head=cur.next
# # #                 else:
# # #                     pre.next=cur.next
# # #                 return
# # #             else:
# # #                 pre=cur
# # #                 cur=cur.next
# # #
# # #     def search(self, item):
# # #         # 查找节点是否存在
# # #         pass
# # #
# # #
# # #
# # # if __name__ == '__main__':
# # #
# # #     node1=SingleNode(10)
# # #     # node1=SingleNode(20)
# # #     # node1=SingleNode(30)
# # #     # node1=SingleNode(40)
# # #     print(node1.item)
# # #     print(node1.next)
# # #     print('*'*12)
# # #
# # #     my_linked_list=SingleLinkedList(node1)
# # #     print(my_linked_list.head)
# # #     print(my_linked_list.head.item)
# # #     print(my_linked_list.head.next)
# # #
# # #     print('*'*12)
# # #
# # #     my_linked_list.add(20)
# # #     my_linked_list.add(20)
# # #     my_linked_list.add(20)
# # #     my_linked_list.add(20)
# # #     my_linked_list.append(30)
# # #     my_linked_list.travel()
# # #
# # #
# # #
# #
# # def bb_sort(lst):
# #     n=len(lst)
# #     for i in range(n-1):
# #         for j in range(n-1-i):
# #             if lst[j]>lst[j+1]:
# #                 lst[j],lst[j+1]=lst[j+1],lst[j]
# #
# # if __name__ == '__main__':
# #     ls1=[5,3,4,7,2]
# #     bb_sort(ls1)
# #     print(ls1)
#
# # def binary_search_recursion(my_list,target):
# #     n=len(my_list)
# #     if n==0:
# #         return False
# #     mid=n//2
# #     if my_list[mid]==target:
# #         return True
# #     elif target<my_list[mid]:
# #         return binary_search_recursion(my_list[:mid],target)
# #     else:
# #         return binary_search_recursion(my_list[mid+1:],target)
# #
# # if __name__ == '__main__':
# #     my_list=[1,2,3,4,5,6,7,8,9,10,22,34,656,]
# #     print(binary_search_recursion(my_list,10))
# #     print(binary_search_recursion(my_list,21))
#
#
#
# def binary_search(my_list,target):
#     start=0
#     end=len(my_list)-1
#
#     while start<=end:
#         mid=(start+end)//2
#         if my_list[mid]==target:
#             return True
#
#         elif target<my_list[mid]:
#             end=mid-1
#         else:
#             start=mid+1
#     return False
#
# if __name__ == '__main__':
#     my_list=[1,2,3,4,5,6]
#     print(binary_search(my_list,3))
#     print(binary_search(my_list,7))


my_list=[1,2,3,4,5,6]

l=my_list[:1:-1]
print(l)
import pandas as pd
my_list=pd.DataFrame
my_list.iloc