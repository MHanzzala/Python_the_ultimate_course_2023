
l = ['a', 'b', 'c', ' ', ' ']

filteredList = list(filter(lambda x: x!=' ', l))
print(filteredList )

appendList = list(map(lambda x: x+"d", l))
print(appendList)

