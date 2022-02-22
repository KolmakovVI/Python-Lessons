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
lines_to_trans = ["What are some contributing factors\n", "say hello\n"]
#full_string = " ".join(lines_to_trans).replace('\n', '')
full_string = " ".join(lines_to_trans)
print(type(full_string))
print(full_string)