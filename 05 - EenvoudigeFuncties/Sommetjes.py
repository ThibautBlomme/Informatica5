#invoer
a = float(input('Geef een waarde voor a: '))
b = float(input('Geef een waarde voor b: '))
i = 0

#formule
print(str('{:>6.0f}'.format(a * pow(10,i))) + ' + ' + ('{:<6.0f}'.format(b * pow(10,i))) + ' = ' + str(int(a * pow(10,i) + b * pow(10,i))))
i += 1
print(str('{:>6.0f}'.format(a * pow(10,i))) + ' + ' + ('{:<6.0f}'.format(b * pow(10,i))) + ' = ' + str(int(a * pow(10,i) + b * pow(10,i))))
i += 1
print(str('{:>6.0f}'.format(a * pow(10,i))) + ' + ' + ('{:<6.0f}'.format(b * pow(10,i))) + ' = ' + str(int(a * pow(10,i) + b * pow(10,i))))
i += 1
print(str('{:>6.0f}'.format(a * pow(10,i))) + ' + ' + ('{:<6.0f}'.format(b * pow(10,i))) + ' = ' + str(int(a * pow(10,i) + b * pow(10,i))))
i += 1
print(str('{:>6.0f}'.format(a * pow(10,i))) + ' + ' + ('{:<6.0f}'.format(b * pow(10,i))) + ' = ' + str(int(a * pow(10,i) + b * pow(10,i))))