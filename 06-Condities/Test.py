x = int(input('Geef een geheel getal: '))

if x % 2 == 0 or x % 3 == 0:
    print(x,'is een veelvoud van 2 of 3')
elif x % 6 == 0:
    print(x, 'is een veelvoud van 6')
else:
    print(x, 'is geen veelvoud van 2 of 3')