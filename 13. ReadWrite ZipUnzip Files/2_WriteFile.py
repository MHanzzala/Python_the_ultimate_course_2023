
lines = ["line 1", "line 2", "line 3"]

with open('writeThisNow.txt', 'w') as f:

    f.writelines('\n'.join(lines))


lines = ['\n', "new line 1", "new line 2"]

with open('writeThisNow.txt', 'w') as f:
    f.writelines('\n'.join(lines))
