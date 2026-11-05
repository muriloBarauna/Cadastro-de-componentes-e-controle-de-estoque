# Importa a função truediv do módulo operator
from operator import truediv

# Cria uma função para solicitar e validar a entrada de números inteiros
# O parâmetro msg recebe a mensagem que será exibida ao usuário
def leiaInt(msg):

    # Cria um laço de repetição para continuar solicitando até receber um valor válido
    while True:
        try:
            # Solicita uma informação ao usuário e converte para número inteiro
            n = (int(input(msg)))

        # Trata erros quando o usuário digita algo que não pode ser convertido em inteiro
        except (ValueError, TypeError):
            # Exibe uma mensagem de erro na cor vermelha
            print('\n\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

            # Retorna ao início do while para solicitar novamente
            continue

        # Trata a interrupção da entrada pelo teclado (Ctrl + C)
        except (KeyboardInterrupt):
            # Informa que o usuário decidiu não digitar o número
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')

            # Retorna o valor 0 para evitar que o programa seja interrompido
            return 0

        # Executa quando nenhum erro acontece
        else:
            # Retorna o número inteiro informado pelo usuário
            return n


# Cria uma função responsável por gerar uma linha de caracteres
# O parâmetro tam define o tamanho da linha, sendo 52 o valor padrão
def linha(tam=52):

    # Multiplica o caractere '-' pela quantidade definida em tam
    # Retorna uma sequência de traços
    return '-' * tam


# Cria uma função para exibir cabeçalhos no sistema
# O parâmetro txt recebe o texto que será exibido
def cabeçalho(txt):

    # Exibe uma linha de separação
    print(linha())

    # Centraliza o texto recebido dentro de um espaço de 52 caracteres
    print(txt.center(52))

    # Exibe outra linha de separação
    print(linha())


# Cria a função responsável por exibir o menu de opções
# O parâmetro lista recebe uma lista com as opções disponíveis
def menu(lista):

    # Exibe o cabeçalho com o título MENU PRINCIPAL
    cabeçalho('MENU PRINCIPAL')

    # Inicializa o contador em 1 para numerar as opções
    c = 1

    # Percorre todos os elementos existentes na lista
    for item in lista:

        # Exibe o número da opção na cor roxa e o nome na cor azul
        print(f'\033[35m{c}\033[m - \033[34m{item}\033[m')

        # Incrementa o contador em 1 a cada repetição
        c += 1

    # Exibe uma linha para finalizar visualmente o menu
    print(linha())

    # Solicita ao usuário que escolha uma opção
    # Utiliza leiaInt para garantir que a entrada seja um número inteiro
    opc = leiaInt('Sua opção: ')

    # Retorna o número da opção escolhida pelo usuário
    return opc
