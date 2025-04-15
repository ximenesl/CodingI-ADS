"""
Desafio 2: Contenção de Mercado
Você foi ao mercado e comprou alguns itens.
Crie variáveis para armazenar os preços de 3 produtos diferentes.
Calcule o valor total gasto e exiba esse valor.
"""

produto1 = 13
produto2 = 12
produto3 = 14.50
preco_total = produto1 + produto2 + produto3
#preco_total = sum([produto1, produto2, produto3])

print('O preço total é R${}'.format(preco_total))

"""
#Pesquisas e Testes
produtos = {
    "Arroz": 12.50,
    "Feijão": 8.99,
    "Macarrão": 5.75
}

compras = ["Feijão", "Arroz"]

total = sum(produtos[produto] for produto in compras)

print('Você comprou:R${}'.format(total))
"""
