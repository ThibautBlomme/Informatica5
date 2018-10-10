#variabelen
tijd = float(input('Geef het aantal minuten na het openen van de proefbuis: '))

#berekening aantal overblijvende toeschouwers

overlevenden = int(50000 * pow(0.5, tijd))

print(round(overlevenden, 0))