"""
 Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.
"""
from time import sleep
print("-=-" *13)
print('######TABUADA##### ')
print("-=-" *13)
n = int(input('DIGITE UM NÚMERO: '))
print("-=-" *13)
print('CAUCULANDO O SEU NÚMERO...')
sleep(2)
print("-=-" *13)
for c in range (1,11):
    print(f'{n}  x  {c:2} = {n*c} ')
print("-=-" * 13)
print('Estou estudando muito para lhe oferecer uma experiência melhor!!!')
print("-=-" * 13)

