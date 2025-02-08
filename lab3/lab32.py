# import random
# import math

# # 1
# def gtoo(g):
#     return 28.3495231 * g

# # 2
# def ftoc(fahrenheit):
#     return (5 / 9) * (fahrenheit - 32)

# # 3
# def solve(numheads, numlegs):
#     for chick in range(numheads + 1):
#         rabb = numheads - chick
#         if 2 * chick + 4 * rabb == numlegs:
#             return (chick, rabb)
#     return None

# # 4
# def filtprime(nums):
#     def isprime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True

#     return [num for num in nums if isprime(num)]

# # 5
# from itertools import permutations
# def printpermutations(s):
#     return [''.join(p) for p in permutations(s)]

# # 6
# def revwords(s):
#     w = s.split()
#     return ' '.join(reversed(w))

# # 7
# def has33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False
# #8
# def spygame(nums):
#     code = [0, 0, 7]
#     i = 0
#     for num in nums:
#         if num == code[i]:
#             i += 1
#             if i == len(code):
#                 return True
#     return False

# # 9
# def volofsph(r):
#     return (4/3) * math.pi * r**3

# #10
# def unielem(lst):
#     uniquelst = []
#     for elem in lst:
#         if elem not in uniquelst:
#             uniquelst.append(elem)
#     return uniquelst

# #11
# def ispalindrome(word):
#     cleanedword = ''.join(e for e in word if e.isalnum()).lower()
#     return cleanedword == cleanedword[::-1]

# # 12
# def histogram(lst):
#     for num in lst:
#         print('*' * num)

# #13
# def guessthenumber():
#     print("Hello! What is your name?")
#     name = input()
#     print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
#     secnum = random.randint(1, 20)
#     guessestaken = 0
    
#     while True:
#         print("Take a guess.")
#         guess = int(input())
#         guessestaken += 1
        
#         if guess < secnum:
#             print("Your guess is too low.")
#         elif guess > secnum:
#             print("Your guess is too high.")
#         else:
#             print(f"Good job, {name}! You guessed my number in {guessestaken} guesses!")
#             break


