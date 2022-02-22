import time  # import timeLib for sleep func

import googletrans  # import for translation

translator = googletrans.Translator()  # set VAR for func
numb_line = 0  # set number of line in file

# set a path for input file with subtitles
inp_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\en-InHyuk Lee-Intermediate-0-1-edit.vtt"
# set a PATh to output file
out_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\Этот файл переделать!!!.txt"
with open(inp_file_path, 'r') as inf, open(out_file_path, 'w') as ouf:  # create a cotstruction for open files
    inf_all = inf.readlines()  # set all lines to list
    for line in inf_all:  # нужно найти способ, чтобы можно было прыгнуть сразу через одну строку в цикле, если я уже две строки соединил и перевел.
        print(str(numb_line))
        if numb_line < 2:
            ouf.write(line)
            numb_line += 1
        else:
            # if first element of line is word OR bracket -- we must translate this line
            if line[0].isalpha() or line[0] == '(':
                time.sleep(0.3)  # set sleep time for request limit of goog translator
                new_line = translator.translate(line, src='english',
                                                dest='russian')  # create a new line with the translated text
                ouf.write(line)  # write original english line to new file
                ouf.write(new_line.text + '\n')  # write translated line to new file
                '''
                output:
                ---------------------
                original
                оригинальный
                text
                текст
                '''
            else:  # if line don't have word or bracket
                ouf.write(line)  # just write this line to new file
            numb_line += 1  # increase number of line
