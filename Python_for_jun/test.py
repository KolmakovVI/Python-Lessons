# a, b= (float(input()) for i in range(2))
# c = input()
# #a, b, c = 1.0, 0.0, "/"
# if c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "*":
#     print(a * b)
# elif c == "pow":
#     print(a ** b)
# elif b == 0:
#     print("Деление на 0!")
# elif c == "/":
#     print(a / b)
# elif c == "mod":
#     print(a % b)
# elif c == "div":
#     print(a // b)

l = r'X-TIMESTAMP-MAP=MPEGTS:180000,LOCAL:00:00:00.000'
d = r'X-TIMESTAMP'
print(l == d)
