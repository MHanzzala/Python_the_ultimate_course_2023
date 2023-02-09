
lines = ["line 1", "line 2", "line 3"]

with open('writeThisNow.txt', 'w') as f:

    f.writelines('\n'.join(lines))

#append the line
lines = ['\n', "This the line_one", "This is line_2","And this is line_3"]

with open('writeThisNow.txt', 'a') as f:
    f.writelines('\n'.join(lines))

#again using the 'w' that means it gonna rewrite all the lines
lines = ['\n', "blah blah blah", "helloG"]

with open('writeThisNow.txt', 'w') as f:
    f.writelines('\n'.join(lines))