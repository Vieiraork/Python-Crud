import ControlUser

ctl = ControlUser.ControlUser()

ctl.opcoes()

op = int(input('Digite a opção desejada: '))
while 4 > op < 0:
    op = int(input('Digite a opção desejada: '))

if op == 1:
    nick = str(input('Digite seu nick: '))
    senha = str(input('Digite sua senha: '))

    ctl.registrar(nick, senha)

elif op == 2:
    nick = str(input('Digite seu nick: '))
    senha = str(input('Digite sua senha: '))

    ctl.alterar(nick, senha)

elif op == 3:
    nick = str(input('Digite seu nick: '))
    senha = str(input('Digite sua senha: '))

    ctl.apagar(nick, senha)

elif op == 4:
    ctl.listar()

else:
    print('Opção incorreta, por favor verifique novamente.')
