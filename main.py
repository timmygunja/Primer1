from sympy import *

k, T, C, L = symbols('k C T L')

C_ost = 20000
Am_lst = []
C_ost_lst = []

for i in range(6):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 20000, T: 6, L: 0})
    Am_lst.append(round(Am.subs({C: 20000, T: 6, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))

print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

print()
print()

Aj = 0
C_ost = 20000
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(6):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 20000, T: 6, k: 2})
    Am_lst_2.append(round(Am.subs({C: 20000, T: 6, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

print()
print()

import pandas as pd
Y = range(1, 7)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)

from matplotlib import pyplot as plt
plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
plt.legend()
plt.show()

vals = Am_lst
labels = list(range(1, 7))
explode = (0.1,) * 6
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode,
       wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)
ax.axis("equal")
plt.show()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])

plt.bar(tfame['Y'], tfame['Am_lst'])
plt.show()

plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.show()
