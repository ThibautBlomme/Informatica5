#Trek aan hendel + Man van brug duwen => Ja + Ja => 2 doden
#Trek aan hendel : nee + man van brug duwen : ja => 1 dode
#Trek aan hendel : ja + man van brug duwen : nee => 1 dode
#Trek aan hendel : nee + man van brug duwen : nee => 5 doden

#Variabelen
hendel = input('Aan de hendel trekken? ')
brug = input('Man van de brug duwen? ')

if hendel == 'ja' and brug == 'ja':
    doden = ('2')
elif hendel == 'ja' and brug == 'nee':
    doden = ('1')
elif hendel == 'nee' and brug == 'ja':
    doden = ('1')
elif hendel == 'nee' and brug == 'nee':
    doden = ('5')

print(doden)
