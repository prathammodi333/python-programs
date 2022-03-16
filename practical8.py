# Name : PRATHAM MODI
# ID : 20CE056
# Aim :  Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop and  traversal method.
# GITHUB LINK : https://github.com/prathammodi333/python-programs
class Stack:
    __dataList = []

    def push(self, data):
        self.__dataList.append(data)

    def pop(self):
        if len(self.__dataList) > 0:  
            return self.__dataList.pop()  
        else:
            return "No elements left for popping operation!" 

    def get_stackSize(self):
        return len(self.__dataList)

    def printStack(self):
        print(self.__dataList)

    def has_next(self):
        return bool(len(self.__dataList))

    def next(self):
        return self.pop()

    def peek(self):
        if len(self.__dataList) > 0:  
            return self.__dataList[-1]  
        else:
            return "No Elements are there in stack."  

    def printPeek(self):
        print(self.peek())

    def printPop(self):
        print(self.pop())


if __name__ == "__main__":
    stack = Stack() 
    stack.printStack()
    stack.push(10)
    stack.printStack()
    stack.push(20)
    stack.push(30)
    print(stack.peek())
    stack.push(40)
    stack.push(50)
    stack.printStack()