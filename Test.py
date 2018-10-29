bod = float(input('startprijs: '))
doorgedraaid = float(input('doorgedraaid onder: '))

akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

# zolang (er geen bod is) EN (er nog iets van de prijs kan gedaan worden)
while (not akkoord) and (bod >= doorgedraaid + 0.01):
    # doe iets vd prijs
    bod -= 0.01

    # is er nu iemand
    akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

if akkoord:
    print('verkocht aan {:.2f}'.format(bod))
else:
    print('doorgedraaid')