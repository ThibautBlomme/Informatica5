l = float(input('Geef de gelijke lengte van beide personen in meter: '))
p1 = str(input('Geef de naam van de eerste persoon: '))
g1 = float(input('Geef het gewicht van de eerste persoon: '))
p2 = str(input('Geef de naam van de tweede persoon: '))
g2 = float(input('Geef het gewicht van de tweede persoon: '))

#bepaling grootste BMI-waarde

if g1 > g2:
    hoogste_bmi = p1 + ' heeft het hoogste BMI '
elif g1 < g2:
    hoogste_bmi = p2 + ' heeft het hoogste BMI '
else:
    hoogste_bmi = p2 + ' heeft het hoogste BMI '

#berekening BMI

if g1 > g2:
    bmi = int('{} / ({}**2)'.format(g1, l))
elif g1 < g2:
    bmi = int('{} / ({}**2)'.format(g2, l))
else:
    bmi = int('{} / ({}**2)'.format(g1, l))

#bepaling gezondheid

if bmi >= 30:
    gezondheid = 'is obees.'
elif bmi >= 25:
    gezondheid = 'heeft overgewicht.'
elif bmi >= 18.5:
    gezondheid = 'heeft een gezond gewicht.'
else:
    gezondheid = ' heeft ondergewicht.'

if g1 == g2:
    print('hoogste_bmi + bmi + (round(bmi, 2)) + gezondheid')
#eindzin
print('hoogste_bmi + bmi + (round(bmi, 2)) + gezondheid')