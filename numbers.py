#!/usr/bin/env python3

English_names = ['Thousand', 'Million', 'Billion', 'Trillion',
                 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion',
                 'Octillion', 'Nonillion', 'Decillion', 'Undecillion',
                 'Duodecillion', 'Tredecillion', 'Quattuordecillion',
                 'Quindecillion', 'Sexdecillion', 'Septendecillion',
                 'Octodecillion', 'Novemdecillion', 'Vigintillion']

n = 1
suffix = ''

for c in range (65):

    n = n * 10
    if (c + 1) % 3 == 0:
        suffix = English_names[c//3]
        English_name = f'One {suffix}'
    if (c + 2) % 3 == 0:
        English_name = f'One Hundred {suffix}'
    if (c + 3) % 3 == 0:
        English_name = f'Ten {suffix}'
    print ('{:>100,} {}'.format(n, English_name))
