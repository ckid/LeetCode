
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def addTwoNumbers( l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        datareturn = ListNode(0)
        curNodeReturn = datareturn
        curNode  = l1
        c = 0

        if (l1 and l2) is None:
            return l1 or l2
        while curNode is not None:
            var,c = Solution.nodeAdd(l1,l2,c)
            curNodeReturn.next = ListNode(val)
            curNodeReturn = curNodeReturn.next
            curNode = curNode.next
            l1 = l1.next
            l2 = l2.next
            #如果l1为空 则将l2连接到curNodeReturn
            if l1 is None:
                if c ==1:
                curNodeReturn.next = l2
                break

            if l2 is None:
                curNodeReturn.next = l1
                break
        return datareturn.next

    @staticmethod
    def nodeAdd(n1, n2, c):
        if n1 and n2 is None:
            node = n1 or n2
            if !None and


        var = n1.var + v2.val + c
        if var >9:
            return var -10, 1
        else:
            return var , 0


if __name__ == "__main__":
    l1 = ListNode(5)
    l1.next=ListNode(8)

    l2 = ListNode(0)

    a = Solution.addTwoNumbers(l1, l2)
    print(a)




