'''
Problem URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         n = len(tokens)
#         for i in range(n):
#             # All the different operations
#             if tokens[i] == "+":
#                 ans = int(stack.pop()) + int(stack.pop())
#                 stack.append(ans)
#             elif tokens[i] == "-":
#                 ans = -int(stack.pop()) + int(stack.pop())
#                 stack.append(ans)
#             # Special case for division as questions wants us to round off the number near to zero, so when we compute a positive answer, we round off to the lowest nearest int, but it will be opposite for negative numbers as we are rounding off close to 0
#             elif tokens[i] == "/":
#                 cur = int(stack.pop())
#                 div = stack.pop()
#                 ans = int(div) // cur
#                 if div%cur != 0 and ans < 0:
#                     ans+=1
#                 stack.append(ans)
#             elif tokens[i] == "*":
#                 cur = int(stack.pop())
#                 ans = int(stack.pop()) * cur
#                 stack.append(ans)
#             else:
#                 stack.append(int(tokens[i]))
        
#         return stack[-1]








# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         # use a stack: first in, last out
#         stack = []

#         def calc(a, b, operator:str) -> int:
#             if operator == "+":
#                 return a + b
#             elif operator == "-":
#                 return a - b
#             elif operator == "*":
#                 return a * b
#             elif operator == "/":
#                 return int(a / b)
#             else:
#                 assert(f"unknown operator: {operator}")

#         for t in tokens:
#             if t in ["+", "-", "*", "/"]:
#                 stack[-2] = calc(stack[-2], stack[-1], t)
#                 stack.pop()
#             else:
#                 stack.append(int(t))
        
#         if len(stack) == 1:
#             return int(stack[0])

#         return final_res







# class Solution:
#     def resolves(self, a, b, Operator):
#         if Operator == '+':
#             return a + b
#         elif Operator == '-':
#             return a - b
#         elif Operator == '*':
#             return a * b
#         return int(a / b)

#     def evalRPN(self, tokens):
#         stack = []
#         for token in tokens:
#             if len(token) == 1 and ord(token) < 48:
#                 integer2 = stack.pop()
#                 integer1 = stack.pop()
#                 operator = token
#                 resolved_ans = self.resolves(integer1, integer2, operator)
#                 stack.append(resolved_ans)
#             else:
#                 stack.append(int(token))
#         return stack.pop()







class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l / r))
                case _:
                    stack.append(int(t))
            
        return stack[0]