'''
Problem URL: https://leetcode.com/problems/multiply-strings/description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # n1 = 0
        # for i in num1:
        #     n1 = n1*10 + (ord(i) - 48)

        # n2 = 0
        # for j in num2:
        #     n2 = n2*10 + (ord(j) - 48)   
        
        # return str(n1*n2)




        # d=num1+"*"+num2
        # d=str(eval(d))
        # return d






        # n1 = [char for char in str(num1)]
        # n2 = [char for char in str(num2)]
        # N1 = 0
        # N2=0
        # p=1
        # val = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        # for ch in n1[::-1]:
        #     N1+= val[ch]*p
        #     p*=10
        # p=1
        # for ch in n2[::-1]:
        #     N2+= val[ch]*p
        #     p*=10
        # return str(N1*N2)






        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                p1 = i + j
                p2 = i + j + 1
                
                total = mul + result[p2]
                
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert to string, skipping leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str