import random
import os

#Dados do aluno
aluno = 'Antonio José Jacinto Cintra - RU: 3420397\n'

#Lista de doadores
lista_doadores =[]

#Função para cadastrar o doador
def cadastrar_doador(nome='',valor=''):
    #------Teste de informacao digitada e lançamento de exceções personalizadas
    try:
        #------Quantidade de caracteres -----#

        #----Se nada for digitado ( Nome )
        if len(nome) <1:
            raise ValueError('Erro ao inserir: Você não digitou o nome\nComece novamente\n')

        #---- Se mais de 1 e menos que 3 caracteres for digitado (Nome)
        elif len(nome) >1 and len(nome) <3:
            raise ValueError('Erro ao inserir: Insira 3 ou mais caracteres no nome do doador\nComece Novamente\n')

        #----Se nada for digitado (Valor)
        elif len(valor) <1 :
            raise ValueError('Erro ao inserir: Você não digitou o valor doado\nComece Novamente\n')

        #----tipo do valor digitado (Nome) - Não permite numeros
        elif any(chr.isdigit() for chr in nome):
            raise ValueError('Erro ao inserir: Digite apenas letras no nome do doador!\nComece Novamente\n')

        #----tipo do valor digitado (valor) - Não permite letras
        elif isinstance(int(valor), int) ==False:
            raise ValueError("Erro ao inserir: O valor doado deve possuir apenas numeros e pontos (0.00)\nComece Novamente\n")

    #------ Retorna exceções em dicionários
    except ValueError as erro:
        return {"Erro":erro}

    #Permite acesso a variavel no modo global
    global lista_doadores

    #Divide o valor doado por 10 , tendo como resultado quantidade de inserção
    qntd_insercoes = float(valor)//10

    #Contador de inserções
    insercao_atual = 0

    #Executa laço de inserção
    while int(insercao_atual) < qntd_insercoes:
        #------Teste inserção e lançamento de exceções personalizadas
        try:
            #Adicionando nome a lista
            lista_doadores.append(nome)
        except:
            return {"Erro":"Erro ao inserir: Não foi possivel gravar na lista de doadores\nComece Novamente\n"}
        #subtrai 1 , de insercao_atual
        insercao_atual +=1
    #Retorna sucesso
    return {"Sucesso":"O doador {} doou R$ {} e seu nome foi inserido {} vezes na lista\n\n".format(nome,valor,int(qntd_insercoes))}

#Opçao inicial para mostrar menu
menu = 'mostrar'
#Variavel para armazenar erros
erro = None
resultados = ''
#Interação em laço com o usuario
while True:

    #Verifica se é primeira execucao
    if menu =='mostrar' or menu=='voltar':
        #Verifica se é uma tentativa de voltar ao menu principal
        if menu == 'voltar':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(aluno)
        #Verifica se há exceções para mostrar
        if erro !=None:
            print(erro)
            erro =None
        print(aluno)
        #Exibe o menu principal
        menu= input("Escolha uma das opções abaixo:\n1-Cadastrar doador\t2-Listar\t3-Sortear\t4-Sair  ")

    #Testando opção digitada para verificar se é possivel continuar
    try:
        #Quantidade de caracteres
        if len(menu) <1:
            raise ValueError('Problema ao escolher opção: Você não digitou sua opção')
        if len(menu) >1:
            raise ValueError('Problema ao escolher opção: Digite 1 opção válida')
        #Tipo digitado
        elif menu.isnumeric() ==False:
            #Se não for inteiro ou float, gera exceção
            raise ValueError("Problema ao escolher opção: Só é permitido numero inteiro de 1 a 4")

        #Valor digitado - Opção 1-Cadastro
        elif int(menu) == 1:
            #Limpar terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            #Mostra informações do aluno
            print(aluno)
            #Mostrando opção escolhida
            print("\nVocê escolheu a opção '1-Cadastrar doador'")
            print("Digite 'voltar' para ir ao menu principal")

            #Solicita nome do doador
            doador = input("\nNome do doador: ")
            #Verifica se foi feita tentativa de voltar
            if doador =='voltar':
                menu='voltar'
                erro=None
                continue

            #Solicita valor da doação
            valor = input(f'Digite o valor doado por {doador} (2 ultimos digitos do RU) - R$ ')
            #Verifica se foi feita tentativa de voltar
            if valor =='voltar':
                menu='voltar'
                erro=None
                continue

            #Executa função e retorna condição do cadastro em um dicionario
            resultado = cadastrar_doador(doador,valor)
            #Verifica se as chaves Erro ou Sucesso existem no Dicionario retornado
            if 'Erro' in resultado.keys():
                raise ValueError(resultado['Erro'])
            elif 'Sucesso' in resultado.keys():
                print(resultado['Sucesso'])
                menu='mostrar'
                continue

        #Valor digitado - Opção 2- Listar doadores
        elif int(menu) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            #Mostra opção escolhida
            print("\nVocê escolheu a opção '2-Listar'")
            #Verifica quantidade de doações cadastradas
            #e exibe um resumo
            if len(lista_doadores) >0 :
                print(f"\nRecebemos {len(lista_doadores)} doações de R$ 10.00")
                print(f"O valor total das doações é R$ {float(len(lista_doadores)*10)}")
                print("Segue abaixo todos os doadores e valores\n")
                print("\n\tLista de doações")
            else:
                #Personaliza Exceção
                raise ValueError('Você escolheu a opção 2-Listar\nNão recebemos nem uma doação até agora')


            #Dicionario que receberá nomes e valores das doaçoes
            doacoes ={}

            #Percorre a lista com nomes a fim de reduzir as repetiçoes
            for doador in sorted(lista_doadores):
                #Verifica se o nome doador ja está no dicionario
                if not doador in doacoes:
                    #Se não estiver no dicionario, Adiciona chave com o valor 10
                    doacoes[doador] = 10
                else:
                    #Se ja existir no dict, atualiza o valor
                    #acrescentando 10 a cada repetição
                    doacoes[doador] = doacoes.get(doador) + 10

            #Percorre doações feitas em seguida, mostra o nome e o valor doado.
            for nome, valor in doacoes.items():
                print(f'{nome} doou R$ {float(valor)}\n')
            #Modifica variavel menu para exibir o menu com possiveis com erros
            menu ='mostrar'
            #Reinicia o laço
            continue
        #Valor digitado - Opção 3-Sortear doadores
        elif int(menu) == 3:
            #Limpa dados anteriores no terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            #Mostra Opção de menu escolhida
            print("\n\tVocê escolheu a opção 3-Sortear")

            #Verifica se há alguma doação
            if len(lista_doadores) >0 :
                print(f"\nRecebemos {len(lista_doadores)} doações de R$ 10.00\nO valor total das doações é R$ {float(len(lista_doadores)*10)}\nSegue abaixo todos os doadores e valores\n")
            else:
                #Gera uma exceção personalizada
                raise ValueError('\nNão recebemos nem uma doação até agora, por isso não haverá sorteio')

            #Dicionario que receberá nomes e valores das doaçoes
            doacoes ={}

            #Percorre a lista com nomes a fim de reduzir as repetiçoes
            for doador in lista_doadores:
                #Verifica se o nome doador ja está no dict
                if not doador in doacoes:
                    #Se não estiver no dicionario, Adiciona chave com o valor 10
                    doacoes[doador] = 10
                else:
                    #Se ja existir no dict, atualiza o valor
                    #acrescentando 10 a cada repetição
                    doacoes[doador] = doacoes.get(doador) + 10

            #Embaralhar lista
            random.shuffle(lista_doadores)

            #Imprime sorteio
            print(f"O doador sorteado foi : {random.choice(lista_doadores)}")

            #Informa que a lista está embaralhada
            print(f"A lista foi embaralhada conforme dados mostram abaixo\n")

            #Percorre doações feitas em seguida, mostra o nome e o valor doado.
            for nome, valor in doacoes.items():
                print(f'{nome} doou R${float(valor)}')
            #Modifica opção de menu para exibir possiveis erros
            menu='mostrar'
            continue
        #Valor digitado - Opção 4-Finalizar programa
        elif int(menu) == 4:
            #Limpa dados anteriores no terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Finalizando programa")
            #Finaliza o laço
            break
        #Valor digitado - Opção não corresponde a nenhuma disponível
        else:
            #Gera Exceção personalizada
            raise ValueError("Problema ao escolher opção: Opção inesistente")

    #Lançamento de exceção
    except ValueError as err:
        #Limpa terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        #Altera o modo de menu para exibir exceções
        menu ='mostrar'
        #Adiciona a variavel erro
        erro = err
        #Reinicia o laço com as exceções
        continue

print("Programa finalizado")
exit()
