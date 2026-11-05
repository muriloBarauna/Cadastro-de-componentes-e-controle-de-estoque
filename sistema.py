# Importa todas as funções do módulo interface
from controledeestoque.lib.interface import *

# Importa todas as funções do módulo arquivo
from controledeestoque.lib.arquivo import *

# Importa a função sleep para criar pausas na execução
from time import sleep

# Define o nome do arquivo que armazenará os dados do estoque
arq = 'cursoemvideo.txt'

# Verifica se o arquivo já existe
if arquivoExistente(arq):
    # Caso exista, apresenta uma mensagem de confirmação
    print('Arquivo encontrado com sucesso!')
else:
    # Caso não exista, informa o usuário
    print('Arquivo não encontrado!')

    # Cria um novo arquivo para armazenar os dados
    criarArquivo(arq)

# Cria um laço de repetição para manter o menu funcionando
while True:

    # Exibe o menu com as opções disponíveis
    # A função menu retorna o número da opção escolhida
    resposta = menu(['ESTOQUE', 'CADASTRAR', 'SAIR DO SISTEMA'])

    # Verifica se o usuário escolheu a opção 1
    if resposta == 1:

        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)

    # Verifica se o usuário escolheu a opção 2
    elif resposta == 2:

        # Exibe o cabeçalho da tela de cadastro
        cabeçalho('NOVO CADASTRO')

        # Solicita o ID do produto e converte a entrada para inteiro
        id = int(input('ID: '))

        # Solicita o nome do produto e armazena como texto
        nome = str(input('Nome: '))

        # Solicita o valor do produto e converte para número decimal
        valor = float(input('Valor: '))

        # Solicita a quantidade disponível e converte para inteiro
        quantidade = int(input('Quantidade: '))

        # Envia os dados informados para a função cadastrar
        # Os dados serão armazenados no arquivo indicado
        cadastrar(arq, id, nome, valor, quantidade)

    # Verifica se o usuário escolheu a opção 3
    elif resposta == 3:

        # Exibe uma mensagem de despedida
        cabeçalho('Saindo do sistema, até breve')

        # Interrompe o laço while e encerra o programa
        break

    # Executa caso o usuário escolha uma opção inválida
    else:

        # Exibe uma mensagem de erro em vermelho
        print('\033[31mERRO! Digite uma opção válida\033[m')

        # Aguarda 4 segundos antes de retornar ao menu
        sleep(4)
