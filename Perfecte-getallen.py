# variabelen
n = int(input('Geef een getal: '))
som = 0
getallen = ''

#lus
for number in range(1, n):
    if n % number == 0:
        som += number
        getallen += ' ' + str(number)

# perfect of niet EN uitzondering 1
if n == 1:
    print('{} is geen perfect getal'.format(n))

elif som == n:
    print('{} is een perfect getal en de delers zijn{}'.format(n, getallen))

else:
    print('{} is geen perfect getal'.format(n))