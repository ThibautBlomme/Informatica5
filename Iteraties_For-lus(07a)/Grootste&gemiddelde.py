vraag = int(input('Geef het aantal getallen: '))
maximum = int(input('Geef een getal: '))
som = maximum

for _ in range(1, vraag):
    getal = int(input('Geef een getal: '))
    maximum = max(getal, maximum)
    som += getal

gemiddelde = round((som / vraag), 2)

print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(maximum, gemiddelde))