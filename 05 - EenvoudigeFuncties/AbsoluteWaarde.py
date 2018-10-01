x = float(input('Geef een waarde voor x: '))
y = float(input('Geef een waarde voor y: '))

print(str('{:.4f}'.format(abs(x) - abs(y))) + ' \N{LESS-THAN OR EQUAL TO} ' + str('{:.4f}'.format(abs((x) - (y)))))