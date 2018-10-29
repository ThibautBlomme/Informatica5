getal = int(input('Geef een getal: '))

variabele = 0

if getal > 1:
    while variabele == 0:
        for i in range(1, getal):
            if getal % i == 0:
                variabele += 1
    if variabele > 1:
        print('{} is geen priemgetal.'.format(getal))
    else:
        print('{} is een priemgetal.'.format(getal))
else:
    print('{} is geen priemgetal.'.format(getal))