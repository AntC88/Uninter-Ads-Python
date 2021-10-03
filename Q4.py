import os
from operator import itemgetter

#Dados do aluno
aluno = 'Antonio José Jacinto Cintra - RU: 3420397\n'

#Lista de produtos
produtos = []

#Função para cadastrar produtos
def cadastra_produto(codigo='',estoque='',minimo=''):
    #Testa e verifica exceções personalizadas
    try:
        #Quantidade de caracteres
        if len(str(codigo)) <1:
            raise ValueError('Você não digitou o código')
        elif len(str(estoque)) <1:
            raise ValueError('Você não digitou o estoque')
        elif len(str(minimo)) <1 :
            raise ValueError('Você não digitou a quantidade minima')

        #Tipo digitado
        elif isinstance(int(codigo),int) ==False:
            #Se não for numero inteiro, gera exceção
            raise ValueError("Só são aceitos numeros inteiros")
        elif isinstance(int(estoque),int) ==False:
            #Se não for numero inteiro, gera exceção
            raise ValueError("Só são aceitos numeros inteiros")
        elif isinstance(int(minimo),int) ==False:
            #Se não for numero inteiro, gera exceção
            raise ValueError("Só são aceitos numeros inteiros")
    #Retorna as exceções
    except ValueError as erro:
        return {"Erro":erro}

    #Acesso a variavel produtos
    global produtos

    try:
        #Tenta adicionar produtos
        produtos.append({"codigo":codigo, "estoque":estoque,"minimo":minimo})
    except:
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Retorna exceção
        return {"Erro":"Não foi possivel inserir esse produto"}

    #Limpa dados anteriores no terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #Retorna sucesso
    return {"Sucesso":"O produto com o código: {} inserido na lista\n\n".format(codigo)}

#Função para listar produtos
def listar_produtos():

    #Permitindo acesso a variavel produtos
    global produtos
    print("Lista de produtos")
    print("Codigo\tEstoque\tMinimo")

    #Ordenar lista por código
    produtos = sorted(produtos, key=itemgetter('codigo'), reverse=False)

    #Percorrendo lista de produtos
    for linha in produtos:
        print('   {}\t   {}\t  {}'.format(linha['codigo'],linha['estoque'],linha['minimo']))


codigo =''
estoque=''
minimo=''

while True:
    print(aluno)
    print("Para finalizar o programa digite '0'")
    #Verifica se há produtos na lista
    if len(produtos)>0:
        #Mostra opção de limpar produtos cadastrados
        print("Para listar os produtos cadastrados digite 'listar'")

    #Verifica cadastro ja iniciado
    if codigo =='' and estoque=='' and minimo =='':
        #informa que é um novo cadastro
        print("Você está inserindo um novo produto")
    else:
        #Informa que está continuando a ultima
        print(f"Você ja iniciou esse cadastro\t Codigo: {codigo} - Estoque: {estoque} - Minimo: {minimo}")
        print("Para iniciar um novo produto do zero, digite 'recomecar'")

    #Verifica se o codigo para o produto atual ja foi digitado antes:
    if codigo =='':
        codigo=input("Digite o código do produto: ")

    ###Verificar opções para o codigo ( finalizar, recomeçar, listar)

    #Verifica se o usuario digitou '0' ( finalizar o programa)
    if codigo =='0':
        print("Você escolheu sair do programa...")
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Finaliza o laço
        break
    #Se digitar 0 ( finaliza o programa)
    if codigo =='recomecar':
        #limpa variaveis
        codigo=''
        estoque=''
        minimo =''
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Reinicia laço sem continuar inserção iniciada
        continue
    #Se digitar Listar
    if codigo =='listar':
        listar_produtos()
        codigo =''
        continue
    else:
        try:
           codigo = int(codigo)
        except:
            codigo=''
            #Limpa dados anteriores no terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite um numero inteiro, 'recomecar', '0' ou 'listar'")
            continue

    #Verifica se o para o produto atual ja foi digitado antes:
    if estoque =='':
        estoque=input("Digite o estoque do produto: ")

    ###Verificar opções para o estoque ( finalizar, recomeçar, listar)

    #Verifica se o usuario digitou '0' ( finalizar o programa)
    if estoque =='0':
        print("Você escolheu sair do programa...")
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Finaliza o laço
        break
    #Se digitar 0 ( finaliza o programa)
    if estoque =='recomecar':
        #limpa variaveis
        codigo=''
        estoque=''
        minimo =''
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Reinicia laço sem continuar inserção iniciada
        continue
    #Se digitar Listar
    if estoque =='listar':
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        estoque=''
        listar_produtos()
        continue
    else:
        try:
           estoque = int(estoque)
        except:
            estoque=''
            #Limpa dados anteriores no terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite um numero inteiro, 'recomecar', '0' ou 'listar'")
            continue
    #Verifica se o para o produto atual ja foi digitado antes:
    if minimo =='':
        minimo=input("Digite o minimo do produto: ")

    ###Verificar opções para o minimo( finalizar, recomeçar, listar)

    #Verifica se o usuario digitou '0' ( finalizar o programa)
    if minimo =='0':
        print("Você escolheu sair do programa...")
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Finaliza o laço
        break
    #Se digitar 0 ( finaliza o programa)
    if minimo =='recomecar':
        #limpa variaveis
        codigo=''
        estoque=''
        minimo =''
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Reinicia laço sem continuar inserção iniciada
        continue
    #Se digitar Listar
    if minimo =='listar':
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        minimo = ''
        listar_produtos()
        continue
    else:
        try:
           minimo = int(minimo)
        except:
            minimo=''
            #Limpa dados anteriores no terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite um numero inteiro, 'recomecar', '0' ou 'listar'")
            continue
    #Executa função para fazer verificação e gravação das informações

    resultado= cadastra_produto(codigo,estoque,minimo)
    if 'Erro' in resultado.keys():
        #Limpa dados anteriores
        os.system('cls' if os.name == 'nt' else 'clear')
        #Mostra possiveis exceções
        print('Ouve um problema: {}\nVamos tentar novamente ?'\
            .format(resultado['Erro']))
        #Reinicia o laço
        continue
    elif 'Sucesso' in resultado.keys():
        #Limpa dados anteriores no terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print(resultado['Sucesso'])
        #Zerando as variaveis
        listar_produtos()
        codigo=''
        estoque=''
        minimo=''


print("programa finalizado")
