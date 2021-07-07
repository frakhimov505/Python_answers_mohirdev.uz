# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:15:52 2021

@author: User
"""

# ismlar=['Mirzo','Farrux','Ubay','Dima','Farhod']
# i=0
# for ism in ismlar:
#     print('Salom ',ism)
#     i=i+1
# print('sikl '+ str(i) + '  marta takrorlandi')

# toq_sonlar=list(range(11,100,2))
# for tsk in toq_sonlar:
#     print(f"{tsk} ning kubi {tsk**3} ga teng")

# suhbat=[]
# for s in range(5):
#     suhbat.append(input(f'{s+1}-suhbat qilmoqchi bo\'lgan odamingizni kiriting'))
# print('siz ',suhbat,' lar bilan suhbat qilmoqchisiz')

n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)