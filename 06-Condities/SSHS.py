# 119-153 = 1	  154-177 = 2	178-209 = 3	  210-249 = 4	≥ 250 = 5

# variabelen
snelheid = int(input('Geef de windsnelheid van de orkaan in km/h: '))

# code

if snelheid >= 250:
    print('categorie 5')
elif snelheid >= 210:
    print('categorie 4')
elif snelheid >= 178:
    print('categorie 3')
elif snelheid >= 154:
    print('categorie 2')
elif snelheid >= 119:
    print('categorie 1')
else:
    print('geen orkaan')