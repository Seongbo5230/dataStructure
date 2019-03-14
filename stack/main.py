class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]

    def printStack(self):
        print(self.stack)

class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or stack.pop() != dict[char]:
                    return False
            else:
                return False
        return stack == []

class DailyTemperatures:
    def dailyTemperatures(self, tempList):
        result = [0] * len(tempList)
        # stack contains the index of the tempList
        stack = []

        for index, t in enumerate(tempList):
          while stack and tempList[stack[-1]] < t:
            cur = stack.pop()
            result[cur] = index - cur
          stack.append(index)
          # print("Index: {},   Stack: {}\nResult: {}\n".format(index, stack, result))

        return result

class ReversePolishNotation:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                v1, v2 = stack.pop(), stack.pop()

                if t=='/':
                    v = int(float(v2) / float(v1))
                else:
                    v = eval(v2 + t + v1)

                stack.append(str(v))

            else:
                stack.append(t)

        return int(stack.pop())

def main():
    ######################
    # MinStack Test Case #
    ######################
    # s = MinStack();
    # s.push(-2);
    # # s.printStack()
    # print("Pushed -2... at the top is " + str(s.top()))
    # s.push(0);
    # # s.printStack()
    # print("Pushed 0... at the top is " + str(s.top()))
    # s.push(-3);
    # # s.printStack()
    # print("Pushed -3... at the top is " + str(s.top()))
    # print("Min: " + str(s.getMin())) # should be -3
    # s.pop();
    # # s.printStack()
    # print("Run pop... at the top is " + str(s.top()))
    # print("Min: " + str(s.getMin())) # should be -2

    ##############################
    # ValidParenthesis Test Case #
    ##############################
    # s = ValidParenthesis()
    # print("Testing \"()\": " + str(s.isValid("()")))
    # print("Testing \"()[]{}\": " + str(s.isValid("()[]{}")))
    # print("Testing \"(]\": " + str(s.isValid("(]"))) # should be false
    # print("Testing \"([)]\": " + str(s.isValid("([)]"))) # should be false
    # print("Testing \"{([])}\": " + str(s.isValid("{([])}")))

    ###############################
    # DailyTemperatures Test Case #
    ###############################
    # dTemp = DailyTemperatures()
    # temps = [73, 74, 75, 71, 69, 72, 76, 73]
    # soln = dTemp.dailyTemperatures(temps)
    # print(soln)
    # print("Output should be: [1, 1, 4, 2, 1, 1, 0, 0]")

    #####################################
    # Reverse Polish Notation Test Case #
    #####################################
    obj = ReversePolishNotation()
    token1 = ["2", "1", "+", "3", "*"]
    print(token1)
    print(obj.evalRPN(token1))
    print("\n")

    token2 = ["4", "13", "5", "/", "+"]
    print(token2)
    print(obj.evalRPN(token2))
    print("\n")

    token3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(token3)
    print(obj.evalRPN(token3))
    print("\n")

if __name__ == "__main__":
    main()
