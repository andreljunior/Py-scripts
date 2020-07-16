
#tempo = int(input('Quantos anos tem seu carro?'))
#if tempo <= 3:
 #   print('carro novo')
#else:
 #   print('carro velho')
#print('FIM')

#print('carro novo'if tempo <= 3 else 'carro velho')
#print('FIM')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
#print('Sua média foi {}.'.format(m))
print('Sua média foi {}. Parabéns!'.format(m) if m >= 7 else 'Sua média foi {}. Precisa estudar mais.'.format(m))