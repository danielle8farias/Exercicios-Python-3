########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o 1º termo de uma PA e sua razão. O programa retorna os 10 primeiros termos dessa PA.
########

A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 1

An = A1
while i < 11:
    print(f'{An}', end=' -> ')
    #fórmula da Progressão aritmética
    An = A1 + i*r
    #i = i + 1
    i += 1
print('FIM')
