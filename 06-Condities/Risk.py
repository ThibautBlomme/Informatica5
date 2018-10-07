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
#bepaling b
if a1 != a and a1 != x:
    e = a1
elif a2 != a and a2 != x:
    e = a2
elif a3 != a and a3 != x:
    e = a3
b = int(e)

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
