'''from itertools import *

k=0
for x in product('ЕКОФ', repeat = 5):
    s = ''.join(x)
    k+=1
    if s.count('Ф') == 1 and s.count('Е') == 0:
        print(k,s)'''


from itertools import product

k = 0
for x in product('беркелий', repeat = 4):
    if x[0] != 'й' and 'и' :
        k += 1

print(k)





