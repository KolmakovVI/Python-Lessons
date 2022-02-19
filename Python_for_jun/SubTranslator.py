import time

import googletrans

translator = googletrans.Translator()
numb_line = 0 # another little 

inp_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\en-InHyuk Lee-Intermediate-0-1-edit.vtt"
out_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\Этот файл переделать!!!.txt"
with open(inp_file_path, 'r') as inf, open(out_file_path, 'w') as ouf:
    inf_all = inf.readlines()
    for line in inf_all: # нужно найти способ, чтобы можно было прыгнуть сразу через одну строку в цикле, если я уже две строки соединил и перевел.

        print(str(numb_line))
        if numb_line < 2:
            ouf.write(line)
            numb_line += 1
        else:

            if line[0].isalpha() or line[0] == '(':
                time.sleep(0.3)
                new_line = translator.translate(line, src='english', dest='russian')
                ouf.write(line)
                ouf.write(new_line.text + '\n')
            else:
                ouf.write(line)
            numb_line += 1
