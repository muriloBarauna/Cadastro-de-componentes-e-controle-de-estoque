from operator import truediv
def leiaInt (msg):
    while True:
        try:
            n = (int(input(msg)))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse número.\n[m')
            return 0
        else:
            return n

def linha(tam = 52) :
    return '-' * tam

def cabeçalho (txt):
    print(linha())
    print(txt.center(52))
    print(linha())

def menu (lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print (f'\033[35m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print (linha())
    opc = leiaInt ('Sua opção: ')
    return opc


