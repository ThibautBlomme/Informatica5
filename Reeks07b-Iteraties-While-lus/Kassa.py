invoer = float(input('Bedrag product:'))
bedrag = 0

while invoer != 0:
    bedrag += invoer
    invoer = float(input('Bedrag product:'))

print('De totale prijs is € {:.2f}'.format(bedrag))