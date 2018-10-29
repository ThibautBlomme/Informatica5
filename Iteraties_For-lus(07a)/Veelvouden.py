# r is groter dan 0 en kleiner dan 100 (en natuurlijk getal = integer)
r = int(input('Geef een getal: '))
som = 0

# loop
for x in range(r, 101, r):
    som += x

#output
print(som)