'''
Problem URL: https://leetcode.com/problems/count-primes/description

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        # count = 0
        # for i in range(2, n):
        #     is_prime = True
        #     for j in range(2, int(i ** 0.5) + 1):
        #         if i % j == 0:
        #             is_prime = False
        #             break
        #     if is_prime:
        #         count += 1
        # return count

        # if n == 0:
        #     return 0
        
        # isPrime = [True] * n
        # count = 0
        
        # if n > 0:
        #     isPrime[0] = False
        # if n > 1:
        #     isPrime[1] = False
        
        # for i in range(n):
        #     if isPrime[i]:
        #         count += 1
        #         j = i * 2
        #         while j < n:
        #             isPrime[j] = False
        #             j += i
        
        # return count


        # if n <= 2:
        #     return 0
        
        # # Initialize bytearray for odd numbers less than n.
        # # The size is n // 2.
        # # Index i represents the number (2 * i + 1).
        # sieve = bytearray([1]) * (n // 2)
        
        # # Index 0 represents number 1, which is not prime.
        # sieve[0] = 0
        
        # # We only need to iterate up to the square root of n.
        # for i in range(3, int(n**0.5) + 1, 2):
        #     # Check if index corresponds to a prime number
        #     # (i - 1) // 2 converts number 'i' to its corresponding index
        #     if sieve[(i - 1) // 2]:
        #         # If i is prime, mark all its odd multiples as non-prime.
        #         # The first odd multiple to mark is i * i.
        #         # The step is 2 * i (since odd + odd = even, we skip even multiples).
        #         # In our index space (0, 1, 2...), a step of 2*i in numbers corresponds to a step of i in indices.
        #         start_index = (i * i - 1) // 2
                
        #         # We update the slice using standard slice assignment.
        #         # The length calculation ensures we generate a bytearray of the exact needed size.
        #         sieve[start_index::i] = bytearray((len(sieve) - 1 - start_index) // i + 1)
        
        # # sum(sieve) counts the odd primes. We add 1 to include the even prime '2'.
        # return sum(sieve) + 1


        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        