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

-------------------------------------------------------------------------------------------
# in klas

woord = input('woord: ')
bedrag = int(input('bedrag: '))

gewonnen_bedrag = 0
geraden_letters = ''

letter = input('letter: ')

while (letter in woord) and (letter not in geraden_letters):
    gewonnen_bedrag += bedrag
    geraden_letters += letter

    letter = input('letter: ')

print(gewonnen_bedrag)