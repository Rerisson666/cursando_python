## Exercício 01 ##
#Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção inteira é {}'.format(num, math.trunc (num)))

## opção sem necessidade de importar nada, apenas usando o método já incluso no python

num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))

## Exercício 02 ##
#Crie um programa que calcule o comprimento do cateto oposto e o cateto adjacente de um triângulo e mostre o comprimento
#Sem o uso da importação da biblioteca Math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Com uso da importação da biblioteca Math
import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

## Exercício 03 ##
#Crie um programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e tangente desse ângulo
from math import sin, cos, tan
ângulo = float('Digite o ângulo que você deseja: ')
seno = sin(math.radians(ângulo))
print ('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(math.radians(ângulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))

## Exercício 04 ##
#Crie um programa que some o comprimento e mostre a hipotenusa de um triângulo

## Exercício 05 ##
#Crie um sorteador de valores aleatórios
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundoo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

## Exercício 06 ##
#Crie um sorteador de ordem aleatória dos valores
from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quanto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)

## Exercício 07 ##
#Crie um tocador MP3 dentro do Python
import pygame
pygame.init()
pygame.mixer.music.load('test.mp3')
pygame.mixer.music.play
pygame.event.wait()


