"""
递归：
    要点：
        1.递归必须要有出口
        2.递归调用次数不能过多
        3.递归必须有规律
    1.分析出口
    2.找规律
"""

# #求阶乘
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
#
# print(factorial(5))

"""
链表：
    每个节点只能有一个前驱和一个后继节点
    优化顺序表的弊端（若无足够的连续的内存空间，会导致扩容失败）
    链表扩容时，有空间就行，无需连续
    
节点：元素域（数值域）和链接域（地址域）组成

    单向链表：一个数值域和一个地址域组成。
    双向链表：可前后双向遍历，每个节点存前驱 + 后继节点地址。
    循环单向链表：最后一个节点指向头节点，形成闭环，无尾指针为空。
    循环双向链表：首尾互指、双向闭环，前驱后继都形成循环。

    行为：
        isEmpty():  判断链表是否为空
        length():   获取链表长度
        travel():   遍历链表
        add(self.item):        链表头部添加元素
        append(self.item):     链表尾部添加元素
        insert(self.pos,item): 指定位置添加元素
        remove(self.item):     删除节点
        search(self.item):     查找节点是否查找 
"""

class SingleNode:
    def __init__(self, item):
        self.item = item    #元素域
        self.next = None    #链接域

class SingleLinkedList:
    def __init__(self,node=None):
        self.head = node

    # is_empty(): 判断链表是否为空
    def is_empty(self):
        #思路1:判断头结点是否为None，若是，则链表为空
        # 写法1：
        # if self.head is None:
        #     return True
        # else:
        #     return False

        #写法2：三元表达式
        # return  True if self.head is None else False

        #写法3：
        return  self.head is None

    # length(): 获取链表长度
    def length(self):
        #创建游标（表示当前节点），默认从头结点开始
        cur=self.head
        #定义计数器
        count=0
        #开始遍历，若不为空，一直循环
        while cur is not None:
            #计数器+1，指向下个结点
            count+=1
            cur=cur.next
        return count

    # travel(): 遍历链表
    def travel(self):
        cur = self.head
        # 开始遍历，若不为空，一直循环
        while cur is not None:
            # 打印当前节点的数值域
            print(f"数值域：{cur.item}")
            #修改当前节点
            cur=cur.next

    # add(self.item): 链表头部添加元素
    def add(self,item):
        #创建新节点
        new_node = SingleNode(item)
        #设置新节点的地址域指向头结点
        new_node.next = self.head
        #设置头结点指向新结点
        self.head = new_node

    # append(self.item): 链表尾部添加元素
    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            #cur为最后一个节点，设置地址域指向新节点
            cur.next = new_node

    # insert(self.pos, item): 指定位置添加元素
    def insert(self,pos,item):
        #头部添加新结点
        if pos<=0:
            self.add(item)
        #尾部添加新结点
        elif pos>=self.length():
            self.append(item)
        #添加新结点
        else:
            #游标
            cur = self.head
            #计数
            count = 0
            #新结点
            new_node=SingleNode(item)

            #找到插入位置前一个结点
            while count < pos-1:
                cur = cur.next
                count += 1
            #完成插入新结点
            new_node.next=cur.next
            cur.next=new_node

    # remove(self.item): 删除节点
    def remove(self,item):
        #游标
        cur = self.head
        #辅助游标（指向前一个结点的游标）
        pre = None

        while cur is not None:
            #判断要删除的结点
            if cur.item == item:
                #判断删除的是否是头结点
                if cur == self.head:
                    #设置头结点为当前结点的下个节点
                    self.head = cur.next
                else:
                    pre.next = cur.next
                    cur.next = None     #删除节点，断开链接
                return
            #没有找到要删除的元素
            else:
                pre = cur
                cur = cur.next

    # search(self.item):
    def search(self,item):
        #游标
        cur = self.head

        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next

        return False

if __name__ == '__main__':
    #测试节点类
    nodel = SingleNode(None)
    print(f"元素域：{nodel.item}")  #10
    print(f"元素域：{nodel.next}")  #None
    print(f"nodel对象：{nodel}")   #地址
    print(f"nodel对象：{type(nodel)}")

    #测试链表类
    my_linked_list = SingleLinkedList()#有默认值可以不传
    print(f"头结点为：{my_linked_list.head}")
    print(f"头结点的元素域为：{my_linked_list.head.item}")   #10
    print(f"头结点的数值域为：{my_linked_list.head.next}")   #None

    #完整测试
    nodel=SingleNode("李三")
    #上述节点做为头结点，创建链表
    my_linked_list=SingleLinkedList(nodel)
    # my_linked_list=SingleLinkedList()

    #打印头结点
    print(f"头结点为:{my_linked_list.head}")
    print(f"头结点的数值域为:{my_linked_list.head.item}")
    print("-"*23)

    #测试链表是否为空
    print(my_linked_list.is_empty())#False
    print('-'*23)

    #测试链表长度
    print(f'链表长度为：{my_linked_list.length()}')
    print('-' * 23)

    #测试遍历链表
    my_linked_list.travel()

    #测试添加元素
    my_linked_list.add(5)

    # 测试(指定位置)添加元素
    my_linked_list.insert(3,'李四')

    #测试删除元素
    my_linked_list.remove('李四')

    # 测试查找元素
    print(my_linked_list.search('张三'))





