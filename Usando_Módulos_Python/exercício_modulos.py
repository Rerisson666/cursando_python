#Exercício 01
#Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção inteira é {}'.format(num, math.trunc (num)))

## opção sem necessidade de importar nada, apenas usando o método já incluso no python

num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))