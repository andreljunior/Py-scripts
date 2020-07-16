

nome = str(input('Qual é seu nome?'))
if nome == 'Andre':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Que belo nome feminino!')
else:
    print('Que nome sem graça')

print('Tenha um bom dia!')

