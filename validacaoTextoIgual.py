
senha = ''
user = ''

for count in range (0, 5):

    user1email = input('Digite seu email: ')
    user1senha = input('Digite sua senha: ')
    senhaconfirmacao1 = input('Digite sua senha: ')

    while user1senha != senhaconfirmacao1:
        print('Verifique a senha inserida')
        senhaconfirmacao1 = input( 'Digite novamente a senha de confirmação: ')
    else: 
        print('Usuário cadastrado ')
