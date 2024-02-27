'''
COMP.SC.100 Tässä käsitellään inputtia ja muutetaan siitä omia muuttujia
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

insert = input('Enter the amount of the study benefits: ') # Ensin kysytään opintotuen suuruutta
before_raise = float(insert)  # Muutetaan saatu arvo float muuttujaksi
print('If the index raise is 1.17 percent, the study benefit,')
after_raise = before_raise * 1.0117 # Evaluoidaan arvo indeksikorotuksella uuteen muuttujaan
print('after a raise, would be', after_raise ,'euros')
print('and if there was another index raise, the study')
double_raise = after_raise * 1.0117 # Evaluoidaan arvo toisella indeksikorotuksella
print('benefits would be as much as', double_raise, 'euros')