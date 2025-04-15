"""
Desafio 5: Objetivo do Passo
Salve o número de etapas que você já executou em uma variável.
Calcule quantos passos faltam para atingir sua meta e exiba essas informações em uma mensagem.
"""

passos = 10000
passos_dados = 3500
passos_faltam = passos-passos_dados

print('Você já deu {}. Faltam {} passos para alcançar seu objetivo!'.format(passos_dados, passos_faltam))