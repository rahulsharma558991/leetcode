'''
Problem URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if not digits:
        #     return []
        
        # phone_map = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz',
        # }

        # def backtrack(combination, next_digits):
        #     if len(next_digits) == 0:
        #         output.append(combination)
        #     else:
        #         for letter in phone_map[next_digits[0]]:
        #             backtrack(combination + letter, next_digits[1:])

        # output = []
        # backtrack("", digits)
        # return output





        # if not digits:
        #     return []

        # phone_map = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz'
        # }
        # combinations = [""]

        # for digit in digits:
        #     new_combinations = []
        #     for combination in combinations:
        #         for letter in phone_map[digit]:
        #             new_combinations.append(combination + letter)
        #     combinations = new_combinations

        # return combinations






        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, current_combination):
            # Base case: if the combination length matches digits length
            if index == len(digits):
                res.append("".join(current_combination))
                return
            
            # Get letters for the current digit
            letters = phone_map[digits[index]]
            
            for letter in letters:
                # Add the letter and move to the next digit
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                # Backtrack: remove the letter before trying the next one
                current_combination.pop()
        
        backtrack(0, [])
        return res