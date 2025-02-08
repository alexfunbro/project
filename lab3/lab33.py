# #1
# class String:
#     def __init__(self):
#         self.string = ""

#     def getString(self):
#         self.string = input()

#     def printString(self):
#         print(self.string.upper())

# #2
# class shape:
#     def __init__(self):
#         self.name = "Shape"

#     def area(self):
#         return 0  

# class square(shape):
#     def __init__(self, l):
#         super().__init__()
#         self.l = l
#         self.name = "Square"

#     def area(self):
#         return self.l * self.l

# #3
# class rectangle(shape):
#     def __init__(self, l, w):
#         super().__init__()
#         self.l = l
#         self.w = w
#         self.name = "Rectangle"

#     def area(self):
#         return self.l * self.w
    
# #4
# import math

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Point coordinates: ({self.x}, {self.y})")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#         print(f"Moved to new coordinates: ({self.x}, {self.y})")

#     def dist(self, other_point):
#         d = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
#         return d

# #5
# class Account:
#     def __init__(self, o, b=0):
#         self.o = o
#         self.b = b

#     def deposit(self, a):
#         if a > 0:
#             self.b += a
#             print(f"Deposited: ${a}. New balance: ${self.b}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, a):
#         if a > 0:
#             if a<= self.b:
#                 self.b -= a
#                 print(f"Withdrew: ${a}. New balance: ${self.b}")
#             else:
#                 print("Insufficient funds for withdrawal.")
#         else:
#             print("Withdrawal amount must be positive.")

# #6
# numss = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]
# isprime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
# prime_numss = list(filter(isprime, numss))
# print("Prime numbers:", prime_numss)
