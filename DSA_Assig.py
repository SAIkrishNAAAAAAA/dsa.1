#1.Delete the elements in a linked list whose sum is equal to zero:

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    sum_dict = {0: dummy}

    while head:
        prefix_sum += head.value
        if prefix_sum in sum_dict:
            node_to_remove = sum_dict[prefix_sum].next
            temp_sum = prefix_sum
            while node_to_remove != head:
                temp_sum += node_to_remove.value
                del sum_dict[temp_sum]
                node_to_remove = node_to_remove.next
            sum_dict[prefix_sum].next = head.next
        else:
            sum_dict[prefix_sum] = head
        head = head.next

    return dummy.next

# 2.Reverse a linked list in groups of given size:

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list_in_groups(head, k):
    current = head
    next_node = None
    prev = None
    count = 0

    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    if next_node:
        head.next = reverse_linked_list_in_groups(next_node, k)

    return prev

#3.Merge a linked list into another linked list at alternate positions:

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_linked_lists_alternate(head1, head2):
    current1 = head1
    current2 = head2

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    return head1


#4.In an array, count pairs with the given sum:

def count_pairs_with_sum(arr, target_sum):
    count = 0
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)

    return count

# 5.Find duplicates in an array:

def find_duplicates(arr):
    duplicates = []
    seen = set()

    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)

    return duplicates



#6.Find the Kth largest and Kth smallest number in an array:

def find_kth_largest_smallest(arr, k):
    sorted_arr = sorted(arr)
    kth_largest = sorted_arr[-k]
    kth_smallest = sorted_arr[k - 1]
    return kth_largest, kth_smallest



#7.Move all the negative elements to one side of the array:

def move_negatives_to_one_side(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        else:
            left += 1
            right -= 1

    return arr
arr = [1,2,3,4,5,6,7,8,9,10]


#8.Reverse a string using a stack data structure:

def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)

    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return (reversed_string)


#9.Evaluate a postfix expression using a stack:

def evaluate_postfix_expression(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for char in expression:
        if char not in operators:
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    return (stack.pop())


#10.Implement a queue using the stack data structure:

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None

    def is_empty(self):
        return not self.stack1 and not self.stack2

queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.is_empty())  
print(queue.dequeue())  
print(queue.is_empty())  