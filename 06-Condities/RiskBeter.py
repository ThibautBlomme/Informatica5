a_1 = int(input('Geef het aantal ogen van de eerste dobbelsteen van de aanvaller: '))
a_2 = int(input('Geef het aantal ogen van de tweede dobblesteen van de aanvaller: '))
a_3 = int(input('Geef het aantal ogen van de derde dobbelsteen van de aanvaller: '))
v_1 = int(input('Geef het aantal ogen van de eerste dobbelsteen van de verdediger: '))
v_2= int(input('Geef het aantal ogen van de tweede dobbelsteen van de verdediger: '))

#dobbelsteen in volgorde zetten
s_v_1 = max(v_1, v_2)
s_v_2 = min(v_1, v_2)

s_a_1 = max(a_1, a_2, a_3)
s_a_3 = min(a_1, a_2, a_3)
s_a_2 = (a_1 + a_2 + a_3) - s_a_1 - s_a_3

# dobbelstenen vergelijken

message = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

if s_v_1 >= s_a_1 and s_v_2 >= s_a_2:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
elif s_a_1 > s_v_1 and s_a_2 > s_v_2:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')

print(message)