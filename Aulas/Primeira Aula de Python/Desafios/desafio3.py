"""
Desafio 3: Tempo de leitura
Crie uma variável para o nome de um livro.
Crie outra variável para o número de páginas desse livro.
Suponha que você leia 10 páginas por dia. Calcule quantos dias levará para terminar o livro e mostre uma frase com essa previsão.
"""

livro = 'Dom Casmurro'
pagina = 160
paginas_lidas = 10

livro_lido = pagina/paginas_lidas

print('Você leverá {} dias.'.format(livro_lido))
