#Blad wint van steen. Steen wint van schaar. Schaar wint van blad. Schaar en Schaar = onbeslist.

#variabelen
p1 = input('Keuze van speler 1: ')
p2 = input('Keuze van speler 2: ')

#code
if p1 == p2:
    print('onbeslist')
elif p1 == 'blad' and p2 == 'steen':
    print('speler 1 wint')
elif p1 == 'steen' and p2 == 'schaar':
    print('speler 1 wint')
elif p1 == 'schaar' and p2 == 'blad':
    print('speler 1 wint')
else:
    print('speler 2 wint')
