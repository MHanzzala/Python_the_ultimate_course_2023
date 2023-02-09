
xcord = []
ycord = []
with open('data.txt', 'r') as file:
    data = file.read()

coordinates = data.split('\n')
for c in coordinates:
    x, y = c.split(',')
    xcord.append(x)
    ycord.append(y)

print("my x are:", xcord)
print("my y are:", ycord)
