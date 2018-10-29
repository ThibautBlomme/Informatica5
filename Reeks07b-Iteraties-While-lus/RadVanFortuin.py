# variabelen
woord = input('Geef het te raden woord: ')
geld = int(input('Geef het gedraaide geldbedrag: '))
letter = input('Geef een letter: ')
letters = ''
bedrag = 0

# loop
while letter in woord and not letter in letters:
    bedrag += geld
    letters += letter
    letter = input('Geef nog een letter: ')

# output
print(bedrag)