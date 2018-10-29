# variabelen
getal_1, getal_2, getal_3 = 1, 1, 1

n = int(input('Getalnummer: '))

# loop
for _ in range(0, n - 2):
    getal_3 = getal_1 + getal_2
    getal_1, getal_2 = getal_2, getal_3

print(getal_3)