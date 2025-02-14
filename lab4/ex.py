# # python json
# import json

# with open('sample-data.json', 'r') as file:
#     data = json.load(file)

# print("Interface Status")
# print("=" * 80)
# print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
# print("-" * 80)

# for interface in data['imdata']:
#     dn = interface['l1PhysIf']['attributes']['dn']
#     speed = interface['l1PhysIf']['attributes']['speed']
#     mtu = interface['l1PhysIf']['attributes']['mtu']
    
#     print("{:<50} {:<20} {:<6} {:<6}".format(dn, "", speed, mtu))

# # python dates
# 1
# from datetime import datetime, timedelta

# cdate = datetime.now()

# ndate = cdate - timedelta(days=5)

# print("current date:", cdate.strftime("%Y-%m-%d"))
# print("date 5 days ago:", ndate.strftime("%Y-%m-%d"))

# 2
# from datetime import datetime, timedelta

# t = datetime.now()

# y = t - timedelta(days=1)
# tom = t + timedelta(days=1)

# print("Yesterday:", y.strftime("%Y-%m-%d"))
# print("Today:", t.strftime("%Y-%m-%d"))
# print("Tomorrow:", tom.strftime("%Y-%m-%d"))

# 3
# from datetime import datetime

# currentdatetime = datetime.now()

# currentdatetimewithoutmicroseconds = currentdatetime.replace(microsecond=0)

# print("Current DateTime:", currentdatetime)
# print("DateTime without microseconds:", currentdatetimewithoutmicroseconds)

# 4
# from datetime import datetime

# d1 = datetime(2025, 2, 10, 12, 0, 0)
# d2 = datetime(2025, 2, 14, 12, 0, 0)

# dif = (d2 - d1).total_seconds()

# print("Difference in seconds:", dif)

# python generator
# 1
# def generatesquares(N):
#     for i in range(N+1):
#         yield i * i

# N = int(input("Enter a number N: "))
# for s in generatesquares(N):
#     print(s)

# 2
# def genevennum(N):
#     for i in range(N+1):
#         if i % 2 == 0:
#             yield i

# N = int(input("Enter a number N: "))
# evenum = list(genevennum(N))
# print(", ".join(map(str, evenum)))

# 3
# def divisibleby3and4(N):
#     for i in range(N+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# N = int(input("Enter a number N: "))
# for num in divisibleby3and4(N):
#     print(num)

# 4
# def squares(a, b):
#     for i in range(a, b+1):
#         yield i * i

# a = int(input("Enter the starting number a: "))
# b = int(input("Enter the ending number b: "))
# for s in squares(a, b):
#     print(s)

# 5
# def countdown(N):
#     while N >= 0:
#         yield N
#         N -= 1
# N = int(input("Enter a number N: "))
# for num in countdown(N):
#     print(num)

# python math
# 1
# import math
# deg = float(input("Input degree: "))
# rad = math.radians(deg)
# print(f"Output radian: {rad:.6f}")

# 2
# h = float(input("Height: "))
# b1 = float(input("Base, first value: "))
# b2 = float(input("Base, second value: "))
# area = 0.5 * (b1 + b2) * h
# print(f"Expected Output: {area}")

# 3
# import math
# sides = int(input("Input number of sides: "))
# sidelength = float(input("Input the length of a side: "))

# areapolygon = (sides * sidelength**2) / (4 * math.tan(math.pi / sides))

# print(f"The area of the polygon is: {areapolygon}")

# 4
# b = float(input("Length of base: "))
# h = float(input("Height of parallelogram: "))

# areaparallelogram = b * h

# print(f"Expected Output: {areaparallelogram}")
