
# The task is to create a palindrome checker whilst
## implementing a list/stack algorithm.
## CODE BY STEPHANIE FERMIL | BCS22

numbers = ["0","1","2","3","4","5","6","7","8","9"]
i = 1

## defining the list for numbers, in case numbers are placed
## in input, it will check here.

## stack code

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)

        if self.top is None:
            self.top = new_node
            self.top.next = None

        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return

        elif self.top.next is None:
            data = self.top.data
            self.top = None
            return data
        else:
            temp = self.top
            data = temp
            self.top = temp.next
            temp = None
            return data

    def reverse_checker(self): ## reverses self.data and returns the reversed list.
        if self.top is not None:
            reverseList = []
            temp = self.top
            while temp:
                reverseList.append(temp.data)
                temp = temp.next
            return reverseList
        else:
            print("Stack is empty.")

def palcheck(palindrome): ## takes the argument 'palindrome' and turns it into a list
    resp = palindrome.lower() ## and runs it under the function Stack().
    this_list = list(palindrome) 
    reverse = Stack()

    for x in resp:
        if x.isalpha() or x in numbers:
            reverse.push(x) ## this will loop through the palindrome and push data to the stack.

    revlist = reverse.reverse_checker()
    finalpal = "".join(this_list)
    reversepal = "".join(revlist)
    if finalpal == reversepal:
        print(f"\"{finalpal}\" is a palindrome!")
    else:
        print(f"\"{finalpal}\" and \"{reversepal}\" do not match and is not a palindrome.")

## actual main program. will loop for all eternity.


while i == 1:
    print("Welcome to the Palindrome Checker.")
    pal = input("Enter a word, sentence, or a phrase!\n")
    palcheck(pal)
    print("\n")

## Reflection/things I've learned: I believe stacks are VERY tricky to
## use and implement. But as long as you remember 'last in, first out',
## I think its also very fun. I'm very curious of other ways to use it
## and might use it for other personal coding projects in the future.

## On the other hand, what I enjoy the most is looping and printing
## through lists, I think that its very fulfilling to see contents 
## of the list come one by one together into a full idea, I think
## this is one of my favorites about lists.
        
    