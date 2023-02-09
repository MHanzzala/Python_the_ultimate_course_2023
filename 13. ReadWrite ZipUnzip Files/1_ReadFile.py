
with open('readthis.txt', "r") as f:
    readByte = f.read(8)
    f.seek(0)
    readOneLine = f.readline()
    f.seek(0)
    readAllLines = f.readlines()

print(readByte)
print(readOneLine)
print(readAllLines)
