# variabelen
kaart = int(input('Geef de waarde van je kaart: '))
som_kaarten = kaart

# loop
while som_kaarten < 21 and kaart != 0:
    kaart = int(input('Geef de waarde van je volgende kaart: '))
    som_kaarten += kaart

# condities
if som_kaarten < 21:
    print('Voorzichtig gespeeld ({})'.format(som_kaarten))
elif som_kaarten == 21:
    print('Gewonnen!')
else:
    print('Verbrand ({})'.format(som_kaarten))