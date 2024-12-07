currentArray = ["700", "800", "", "900", "1000", "1100", "", "1200", "1300", "", "1400", "900", "1000", "1100", ""]

max = 0
current = 0


for i in range(len(currentArray)):
    if currentArray[i] == "":
        if current > max:
            max = current
        current = 0
    else:
        current = current + int(currentArray[i])

print(max)