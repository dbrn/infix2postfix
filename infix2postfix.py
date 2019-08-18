# Stack data-structure class. All the methods represent the possible operations that you can perform on a stack
# As for peek and pop, I coded an error management system to avoid raising exceptions during runtime
class Stack:
    def __init__(self, iterator = []):
        self.__stack = iterator
        self.__value = None

    def push(self, obj):
        self.__stack.append(obj)

    def pop(self):
        try:
            self.__value = self.__stack.pop(-1)
            return self.__value
        except IndexError:
            return None

    def peek(self):
        try:
            return self.__stack[-1]
        except IndexError:
            return None

# dictionary to give priorities to the supported mathematical operations
precedenze = {"+":1, "-":1, "*":2, "/":2, "^":3}
# all the elements of the expression have to be inserted with a space, 
# in that way my script will be able to create a list out of them
espressione = input().split()
#All the possible operators in a string
operatori = "()-*/+^"
# I create a stack object
stack = Stack()
for i in range(len(espressione)):
# Ignore spaces, print operands to the console and push to the stack open parenthesis
    if espressione[i] == " ":
        continue
    if espressione[i] not in operatori:
        print(espressione[i], end=" ")
    elif espressione[i] == "(":
        stack.push(espressione[i])
# if it's an operator or a closed parenthesis...
    else:
# print to the console all the operators inside the parenthesis
        if espressione[i] == ")":
            while stack.peek() is not None and stack.peek() != "(":
                print(stack.pop(), end = " ")
            stack.pop()
            continue
# if the operator has a lower precedence print the higher precedence operators from the stack
        else:
            while stack.peek() is not None and stack.peek() != "(":
                if precedenze[espressione[i]] <= precedenze[stack.peek()]:
                    print(stack.pop(), end=" ")
                else:
                    stack.push(espressione[i])
                    break
            else:
                stack.push(espressione[i])
# print all the remaining operators from the stack, emptying it
# do not print parenthesis
while stack.peek() is not None:
    operatore = stack.pop()
    if operatore == "(" or operatore == ")":
        continue
    else:
        print(operatore, end=" ")
