
frase = 'Curso em Video Python'

frase[9] #pega o decimo caracter
frase[9:13] #vai de 9 a 12
frase[9:21:2] #vai de 9 a 20 de 2 em 2
frase[:5] #começa de zero
frase[15:] #vai do 15 ate o caracter final
frase[9::3] #do nove ate o final de 3 em 3

print(frase[9::3])

print(len(frase))

frase.count('o',0,13) #contagem de caracteres o nas posicoes 0 a 13
frase.find('deo') #se o retorno for -1, significa que nao foi encontrado
'Curso' in frase #gera true ou false
frase.replace('Python','Android')
frase.upper() #passa tudo para maiusculo -> print(frase.upper())
frase.lower() #mesmo de upper mas para minusculo
frase.capitalize() #passa tudo para minusculo e a primeira letra para maiusculo
frase.title() #analisa quantas palavras a string tem e faz o Capitalize palavra por palavra

frase1 = '   Aprenda Python  '
frase1.strip() #elimina os espacos em branco desnecessarios
frase1.rstrip() #trata apenas o lado direito da string
frase1.lstrip() #trata apenas os espacos da esquerda

frase.split() #transforma cada palavra em uma nova lista -> gera uma lista com todas as palavras da frase
print(frase.split())

dividido = frase.split()
'-'.join(dividido) #junta as palavras utilizando o separador indicado
print(dividido[2][3])
print('-'.join(dividido))

#escrever um texto de multiplas linhas com mais facilidade
print("""O mês de maio foi de muita volatilidade nos mercados. Embora o crescimento
global mantenha uma trajetória firme, observou-se um aumento da incerteza acerca
da resiliência da recuperação econômica global. A confiança dos investidores foi
testada com eventos políticos na Itália, Espanha e Inglaterra, com a elevação do risco
de guerra comercial, e com incertezas nas negociações dos EUA com Coreia do
Norte e Irã sobre desarmamento nuclear.""")