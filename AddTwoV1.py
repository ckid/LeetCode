class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def nodeAddOne(self, l1):
        """
        将节点的值+1
        :param l1:li不能为空
        :return:
        """
        listData = l1
        l1Pre = l1
        c = 1
        while c == 1:
            if l1 is None:
                l1Pre.next = ListNode(1)
                return listData
            if l1.val < 9:
                l1.val += 1
                return listData
            else:
                if l1.val == 9:
                    l1.val = 0
                    c = 1
                    l1Pre = l1
                    li = li.next


    def add_two(self, l1, l2):
        listReturn= l1
        l1pre = l1
        l2pre = l2
        c = 0
        while l1 and l2:
            tmp_val = l1.val + l2.val + 1
            if tmp_val > 9:
                c = 1
                l1.val = tmp_val -10
            else:
                c = 0
                l1.val = tmp_val

            l1pre = l1
            l2pre = l2
            l1 = l1.next
            l2 = l2.next

        #注意这时候至少有一个链表遍历完
        if c == 0:
            l1pre.next = l1 or l2
        else:
            #c =1 必须处理c
            if (l1 or l2) is None:
                l1pre.next = ListNode(1)
            else:
                l1pre.next = self.nodeAddOne(l1 or l2)
        return listReturn



if __name__ == "__main__":
    l1 = ListNode(9)
    l1.next=ListNode(8)

    l2 = ListNode(1)
    a = Solution()
    b = a.add_two(l1, l2)
    print(b)