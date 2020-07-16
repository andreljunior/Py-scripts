#codigo ANSI \033[m

#\033[0;31;41m
#\033[4;33;44m
#\033[01;35;43m
#\033[30;42m
#\033[7;30;41m

print('\033[7;33;44mOlá, Mundo!\033[m')
a = 3
b = 5

print('Os valores são \033[1;35;44m{}\033[m e \033[7;33;44m{}\033[m'.format(a, b))

nome = 'Andre'
print('Ola! Prazer em te conhecer {}{}{}!'.format('\033[4;34m',nome,'\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'verde':'\033[32m'}

nome1 = 'Manoella'
print('Ola! Prazer em te conhecer {}{}{}!'.format(cores['verde'],nome1,cores['limpa']))