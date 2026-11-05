from controledeestoque.lib.interface import*
from controledeestoque.lib.arquivo import*
from time import sleep
arq = 'cursoemvideo.txt'

if arquivoExistente(arq):
    print ('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu (['ESTOQUE', 'CADASTRAR', 'SAIR DO SISTEMA'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        id = int(input('ID: '))
        nome = str(input('Nome: '))
        valor = float(input('Valor: '))
        quantidade = int(input('Quantidade: '))
        cadastrar(arq, id, nome, valor, quantidade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema, até breve')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
        sleep (4)