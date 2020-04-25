#!/usr/bin/env python3.8

'''
Usuário digita dois números e programa retorna a soma entre eles.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função para somar dois números
def soma(x,y):
        z = x+y
        return z

#programa principal
cabecalho('soma de dois números')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura o que for digitado
    #float() convertendo string para tipo flutuante
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    # atribui a uma variável o retorno da função soma()
    resultado = soma(num1,num2)
    print(f'{num1} + {num2} = {resultado}')
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
