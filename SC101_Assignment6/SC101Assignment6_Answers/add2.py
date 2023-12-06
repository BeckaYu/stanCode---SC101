"""
File: add2.py
Name: Rebecca
------------------------
This program adds two numbers represented by two linked lists, where each node contains a single digit.
The digits are stored in reverse order, and each of their non-empty linked lists does not contain any leading zeros,
except for the number 0 itself. After calculating the sum, the result is returned as a linked list.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: ListNode representing the first number
    :param l2: ListNode representing the second number
    :return: ListNode representing the sum of the two numbers
    -------------------------------------------
    This function converts the linked lists to integers, adds them together,
    and converts the sum back into a linked list.
    """
    cur1 = l1
    cur2 = l2
    lst1 = []
    lst2 = []

    # Turn the linked list into a list
    while cur1 is not None:
        lst1.append(cur1.val)
        cur1 = cur1.next
    total1 = 0
    digit1 = 0

    while cur2 is not None:
        lst2.append(cur2.val)
        cur2 = cur2.next
    total2 = 0
    digit2 = 0

    # Turn the list into integers
    for i in range(len(lst1)):
        total1 += lst1[i] * 10**i
        digit1 += 1

    for i in range(len(lst2)):
        total2 += lst2[i] * 10**i
        digit2 += 1

    total = total1 + total2

    # Turn the integers into list
    lst_ans = []
    if total >= 10: # Deal with integers more than two digits
        lst_ans = find_answers(total, []) # Use recursion to convert the digit
    else:
        lst_ans.append(total)

    # Turn the list back to linked list
    ans = None
    end = None
    for digit in lst_ans:
        new_node = ListNode(digit, None)
        if ans is None:
            ans = new_node
            end = new_node
        else:
            end.next = new_node
            end = end.next
    return ans


def find_answers(total, lst_ans):
    """
    :param total: Integer to be decomposed
    :param lst_ans: List to store the decomposed digits
    :return: List of digits
    -------------------------------------------
    This function recursively decomposes an integer into its digits.
    """
    if total < 1:
        return lst_ans
    else:
        lst_ans.append(total%10)
        total = total//10
        return find_answers(total, lst_ans)
####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)

def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
