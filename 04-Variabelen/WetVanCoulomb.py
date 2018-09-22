r = float(input('Geef de straal: '))

k = 8.99 * 10 ** 9
Q1 = 2.0 * 10 ** -6
Q2 = 1.0 * 10 ** -6

uitvoer = k
uitvoer *= (Q1 * Q2)
uitvoer /= (r * 10 ** -2) ** 2

print(uitvoer)



