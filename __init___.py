# Define uma função para ler e validar números inteiros
# O parâmetro msg recebe a mensagem que será exibida ao usuário
def leiaInt(msg):

    # Inicia um laço de repetição infinito
    while True:
        try:
            # Solicita um dado ao usuário e converte para número inteiro
            n = (int(input(msg)))

        # Captura erros caso o usuário digite um valor que não seja inteiro
        except (ValueError, TypeError):

            # Exibe uma mensagem de erro na cor vermelha
            print('\n\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

            # Retorna ao início do laço para solicitar um novo valor
            continue

        # Captura o erro caso o usuário interrompa a digitação (Ctrl + C)
        except (KeyboardInterrupt):

            # Informa que o usuário preferiu não digitar o número
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')

            # Retorna o valor zero para evitar a interrupção do programa
            return 0

        # Executa quando não ocorre nenhum erro
        else:

            # Retorna o número inteiro informado pelo usuário
            return n


# Define uma função para criar uma linha de separação
# O parâmetro tam define o tamanho da linha
# Caso nenhum valor seja informado, utiliza o padrão de 52 caracteres
def linha(tam=52):

    # Multiplica o caractere '-' pela quantidade definida em tam
    # Retorna a linha de separação
    return '-' * tam


# Define uma função para criar cabeçalhos no programa
# O parâmetro txt recebe o texto que será exibido no cabeçalho
def cabeçalho(txt):

    # Exibe uma linha de separação antes do título
    print(linha())

    # Centraliza o texto recebido em um espaço de 52 caracteres
    print(txt.center(52))

    # Exibe outra linha de separação após o título
    print(linha())


# Define uma função responsável por exibir o menu de opções
# O parâmetro lista recebe as opções que serão apresentadas ao usuário
def menu(lista):

    # Chama a função cabeçalho para exibir o título do menu
    cabeçalho('MENU PRINCIPAL')

    # Inicializa a variável c com o valor 1
    # Essa variável será utilizada para numerar as opções do menu
    c = 1

    # Percorre todos os elementos existentes dentro da lista
    for item in lista:

        # Exibe o número da opção na cor roxa
        # Exibe o nome da opção na cor azul
        print(f'\033[35m{c}\033[m - \033[34m{item}\033[m')

        # Incrementa o contador em 1 a cada repetição
        c += 1

    # Exibe uma linha de separação após as opções
    print(linha())

    # Solicita ao usuário que escolha uma das opções disponíveis
    # Utiliza a função leiaInt para garantir que a entrada seja um número inteiro
    opc = leiaInt('Sua opção: ')

    # Retorna o número da opção escolhida pelo usuário
    return opc
