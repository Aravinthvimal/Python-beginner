s = input()

fahad = []

for i in s.split():
    i = i[0].upper() + i[1:]
    fahad.append(i)

print(" ".join(fahad))


