#variabelen
a1 = input('Geef het aantal ogen van de eerste dobbelsteen van de aanvaller: ')
a2 = input('Geef het aantal ogen van de tweede dobblesteen van de aanvaller: ')
a3 = input('Geef het aantal ogen van de derde dobbelsteen van de aanvaller: ')
d1 = input('Geef het aantal ogen van de eerste dobbelsteen van de verdediger: ')
d2 = input('Geef het aantal ogen van de tweede dobbelsteen van de verdediger: ')
a = int(max(a1, a2, a3))
x = int(min(a1, a2, a3))
c = int(max(d1, d2))
d = int(min(d1, d2))
y = int(a1) + int(a2) + int(a3)
b = int(y) - int(a) - int(x)

#code
if a > c and b > d:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
elif a > c and b < d:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a < c and b > d:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a < c and b < d:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
elif a == c and b == d:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
elif a == c and b > d:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a == c and b < d:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
elif a > c and b == d:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a < c and b == d:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')