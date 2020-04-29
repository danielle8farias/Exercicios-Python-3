#!/usr/bin/env python3.8

'''
Usuário informa um valor em Reais e programa retorna a conversão desse em dólares.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que converte o Real em Dolar
def dollar(real):
    #atribuindo a variável o resultado da operação
    dolar = real/3.89 #em 03/06/2019
    return dolar

#programa principal
#chamada da função cabeçalho
cabecalho('CONVERSOR REAL EM DOLAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável real
    real = float(input('Valor em Reais: R$'))
    #atribuindo a variável o retorno da função
    valor_dolar = dollar(real)
    #função print retorna uma string formatada na tela
    #:.2f limita o número de duas casas decimais
    print(f'Com R${real:.2f} você pode comprar US${valor_dolar:.2f}')
    #função print vazia não retorna nada; pula uma linha
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
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()