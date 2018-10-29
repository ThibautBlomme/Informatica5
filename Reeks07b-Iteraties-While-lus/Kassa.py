invoer = float(input('Bedrag product:'))
bedrag = invoer

while invoer != 0:
    bedrag += invoer
    invoer = float(input('Bedrag product:'))

print('De totale prijs is € ' + str(bedrag))