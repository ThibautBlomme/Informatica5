# variabelen

gewenste_s = int(input('Geef de gewenste snelheid van de raket: '))
s = int(input('Geef de huidige snelheid van de raket: '))
telling = 0

# lus
while s > gewenste_s:
    telling += 1
    s = s * 0.7

print('na {} rembewegingen is de snelheid {:.2f}'.format(telling, s))