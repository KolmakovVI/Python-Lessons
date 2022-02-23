import time  # import timeLib for sleep func

import googletrans  # import for translation

translator = googletrans.Translator()  # set VAR for func
numb_line = 0  # set number of line in file
lines_to_trans = []  # create a list for accumulating lines to translate
# set a path for input file with subtitles
inp_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\en-InHyuk Lee-Intermediate-0-1-edit.vtt"
# set a PATh to output file
out_file_path = r"C:\Users\kolma\Desktop\Courses\Иллюстрация\InHyuk Lee Illustration\0 Hello, I'm InHyuk Lee\subtitles\RU-InHyuk Lee-Intermediate-0-1-edit.vtt"
with open(inp_file_path, 'r') as inf, open(out_file_path, 'w',
                                           encoding="utf-8") as ouf:  # create a construction for open files
    inf_all = inf.readlines()  # set all lines to list
    # execute cycle while the number of line don't equal last number of line on input file
    while numb_line <= len(inf_all):
        print(str(numb_line))
        if numb_line < 2:  # skip two first lines for translator
            ouf.write(inf_all[numb_line])  # just write two first lines to new file
            numb_line += 1  # increase number of line
        else:
            # if first element of line is word OR bracket -- we must translate this line
            if inf_all[numb_line][0].isalpha() or inf_all[numb_line][0] == '(':
                lines_to_trans.append(inf_all[numb_line])  # append new line to list for translator
                ouf.write(inf_all[numb_line])  # just write this line to new file

            else:  # if line don't have word or bracket
                for line in lines_to_trans:
                    time.sleep(0.1)  # set sleep time for request limit of goog translator
                    new_line = translator.translate(line, src='english',
                                                    dest='russian')  # create a new line with the translated text
                    ouf.write(new_line.text + '\n')  # write original english line to new file

                # ----------------- change all element of list with lines to string and translate it together
                # if lines_to_trans:
                #     full_string = " ".join(lines_to_trans).replace('\n', '')
                #     time.sleep(0.2)  # set sleep time for request limit of goog translator
                #     new_line = translator.translate(full_string, src='english',
                #                                         dest='russian')  # create a new line with the translated text
                #     ouf.write(new_line.text + '\n')  # write original english line to new file
                # ----------------- this feature don't increase quality of translated text

                lines_to_trans.clear()  # set empty list for searching next fragments subtitles
                ouf.write(inf_all[numb_line])  # just write this line to new file

            numb_line += 1  # increase number of line

