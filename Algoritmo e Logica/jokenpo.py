import random
items = ('pedra', 'papel', 'tesoura')
computador = random.randint(0,2)
jogador = int(input('digite um numero'))
print ('o computador escolheu {}'.format(items[computador]))
print ('o jogador escolheu {}'.format(items[jogador]))
if computador == 0:
    if jogador ==0:
        print('empate')
    elif jogador == 1:
        print ('perdeu')
    elif jogador == 2:
        print('venceu')

    
if computador == 1:
    if jogador ==0:
        print('ganhou')
    elif jogador == 1:
        print ('empate')
    elif jogador == 2:
        print('perdeu')
if computador == 2:
    if jogador ==0:
        print('perdeu')
    elif jogador == 1:
        print ('ganhou')
    elif jogador == 2:
        print('empate')
