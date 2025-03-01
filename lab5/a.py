# import re
# with open("row.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# # 1
# if re.search("^a*b*", content):
#     print("1: yes")
# else:
#     print("1: no")


# # 2
# if re.search("^a*bb|^a*bbb", content):
#     print("2: yes")
# else:
#     print("2: no")

# # 3
# a = re.findall("[a-z]+_[a-z]+", content)
# print(a)

# # 4
# a = re.findall("[A-Z]{1}_[a-z]+", content)
# print(a)

# # 5
# if re.search("a.*b$", content):
#     print("5: yes")
# else:
#     print("5: no")

# # 6 
# a = re.sub("[ .,]", ":", content)
# print(a)

# # 7
# def upp(b):
#     return b.group(0)[1:].upper()
# a = re.sub("_[a-z]", upp, content)
# print(a)


# # 8
# a = re.split("[A-Z]", content)
# print(a)

# # 9
# def func(b):
#     return " "+b.group(0)
# a = re.sub('[A-Z]', func, content)
# print(a)

# # 10
# def k(b):
#     return "_"+b.group(0).lower()
# a = re.sub("[A-Z]", k, content)
# print(a)