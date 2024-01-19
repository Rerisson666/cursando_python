# .Format pra apresentação de resultados de forma simples

n = int(input('Digite um número: '))
a = n - 1
b = n + 1
print('Analisando o valor {}, seu anecesor é {} e o sucessor é {}'.format(n, a, b))

# Calculos Aritiméticos básicos

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O doblo de {} vale {}'.format(n, ))
print('O triplo de {} vale {}. \nA raiz dquadrada de {} é igual a {}.'.format(n*3, d, n, r))

# Simplificando  Calculas Aritiméticos básicos

n = int(input('Digite um número: '))
print('O doblo de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz dquadrada de {} é igual a {}.'.format(n, (n*3), n, pow(n,(1/2))))

# Lista de Resultados - Modelo simples de demonstrativo de Resultado

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2  # Observação : Respeitem a ordem de precedência dos operadores aritiméticos
print('A média entre {} e {} é igual'.format(n1, n2, média))

# Criando um conversor de medidas

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde à {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
