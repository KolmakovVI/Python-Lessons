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

# set a path for input file with subtitles
inp_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\Change_this_FILE.vtt"
# set a PATh to output file
out_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\test.vtt"
with open(inp_file_path, 'r') as inf, open(out_file_path, 'w', encoding="utf-8") as ouf:  # create a construction for open files
    for line in inf:
        ouf.write(line)
