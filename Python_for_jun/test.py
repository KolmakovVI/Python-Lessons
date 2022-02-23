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


import translators as ts
import time
# set a path for input file with subtitles
inp_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\en-InHyuk Lee-Intermediate-0-1-edit.vtt"
# set a PATh to output file
out_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\testnewtr.vtt"
tic = 0
with open(inp_file_path, 'r') as inf, open(out_file_path, 'w', encoding="utf-8") as ouf:  # create a construction for open files
    for line in inf:
        if line[0].isalpha() or line[0] == '(':
            # ouf.write(line)
            transl_line = ts.google(line, from_language='en', to_language='ru')
            # ouf.write(t)
            print(transl_line)
            time.sleep(1)
            # tic+=1
