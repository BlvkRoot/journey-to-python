# Understanding strings commonly used methods
nome_curso = '  Edição de vídeo  '
print(nome_curso.capitalize()) # Convert first letter to uppercase
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip()) # Remove spaces from string
print(nome_curso.lstrip()) # Remove left spaces from string
print(nome_curso.rstrip()) # Remove right space from string
print(nome_curso.find('ção')) # Return string position
print(nome_curso.replace('Video', 'Música'))
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))


# Challenge

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.capitalize()}')


