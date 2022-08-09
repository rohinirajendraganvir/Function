def generateRange(min, max, step):
    list = []
    while min <= max :
        list.append(min)
        min+=step
    return list
print(generateRange(2, 10, 2))