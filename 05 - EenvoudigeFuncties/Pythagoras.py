#variabelen
a = float(input('Geef de lengte van de eerste rechthoekszijde: '))
b = float(input('Geef de lengte van de tweede rechthoekszijde: '))
from math import sqrt
c = sqrt(pow(a, 2) + pow(b, 2))

#formule
print(str('In een rechthoekige driekhoek met rechthoekzijden a = ' + str('{:.2f}'.format(a)) + ' en b = ' + str('{:.2f}'.format(b)))  + ' is de schuine zijde ' + str('{:.2f}'.format(c)))