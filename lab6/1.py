import math
import time
import os
import string
# # 1
# list = {1, 2, 3, 4, 5}
# mult = math.prod(list)
# print(mult)

# # 2
# a = "DsJJsallSOFaad"
# b = sum(map(str.isupper, a))
# c = sum(map(str.islower, a))
# print(b, c)

# # 3
# a = "xxDfDxx"
# b = a[::-1]
# if a == b:
#     print("palindrome")
# else:
#     print("not")

# # 4
# num1 = int(input())
# num2 = int(input()) 
# time.sleep(b / 1000)
# res = math.sqrt(a)
# print(f"Square root of {num1} after {num2} milliseconds is {res}")

# # 5
# a = (True, True, True)
# print(all(a))

# # Directories and Files

# # 1
# p = "C:\\Users\\danie\\Desktop\\python"
# directories = [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]
# print("Directories:", directories)
# files = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
# print("Files:", files)
# all_items = os.listdir(p)
# print("All items:", all_items)

# # 2
# p = "C:\\Users\\danie\\Desktop\\python"
# if os.path.exists(p):
#     print(f"Path '{p}' exists.")
#     if os.access(p, os.R_OK):
#         print("Readable: Yes")
#     else:
#         print("Readable: No")

#     if os.access(p, os.W_OK):
#         print("Writable: Yes")
#     else:
#         print("Writable: No")

#     if os.access(p, os.X_OK):
#         print("Executable: Yes")
#     else:
#         print("Executable: No")
# else:
#     print(f"Path '{p}' does not exist.")

# # 3
# p = "C:\\Users\\danie\\Desktop\\python"
# if os.path.exists(p):
#     print(f"Path '{p}' exists.")

#     directory = os.path.dirname(p)
#     print(f"Directory: {directory}")

#     filename = os.path.basename(p)
#     print(f"Filename: {filename}")

# else:
#     print(f"Path '{p}' does not exist.")

# # 4
# p = "text.txt"
# with open(p, "r") as file:
#     a = sum(1 for line in file)
# print(f"Number of lines in '{p}': {a}")

# # 5
# a = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# p = "text.txt"
# with open(p, "w") as file:
#     for i in a:
#         file.write(i + "\n")

# # 6

# for i in string.ascii_uppercase:
#     file_name = f"{i}.txt"
#     with open(file_name, "w") as file:
#         file.write(f"This is file {file_name}\n")


# for i in string.ascii_uppercase:
#     file_name = f"{i}.txt"
#     os.remove(file_name)

# # 7
# a = "source.txt"
# b = "destination.txt"
# with open(a, "r") as a, open(b, "w") as b:
#     b.write(a.read())

# #8
# p = "text.txt"
# if os.path.exists(p):
#     print(f"File '{p}' exists.")
#     if os.access(p, os.W_OK):
#         os.remove(p)
#         print("file removed")
#     else:
#         print("file is not accessible")
# else:
#     print("file does not exist")