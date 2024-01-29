preço = float(input('Qual o preço do produto? R$'))
desconto = float(input('Qual o desconto do produto? %'))
novo = preço - (preço * desconto / 100)
print('O produto que custava R${:.2f}, na promoção vai custar R${:.2f}'.format(preço, novo))