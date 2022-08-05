import os

#Dados do aluno
aluno = 'Antonio José Jacinto Cintra - RU: 3420397\n'
print(aluno)

while True:
    print('Escolha uma opção abaixo\n')

    #------Digitação forçada ( Escolha de opções)
    novo_ou_sair = input("0-Limpar tela  1-Inserir dados  2-Sair do programa\t")

    #------Teste de informacao digitada e lançamento de exceções personalizadas
    try:
        #------Quantidade de caracteres Permite-se apenas 1 caracter-----#

        #----Se nada for digitado
        if len(novo_ou_sair) <1:
            raise ValueError('Não é aceito sem digitar nada')
        #---- Se mais de 1 caractere for digitado
        elif len(novo_ou_sair) >1:
            raise ValueError('Só é aceito 1 caractere')

        #----tipo do valor digitado ( permite-se apenas inteiro)
        elif novo_ou_sair.isnumeric() == False:
            raise ValueError("Só é aceito numeros")

        #-----Valor digitado
        #---Se o valor digitado é '0' , Limpa o terminal e recomeça o laço
        elif int(novo_ou_sair) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Limpado terminal\n")
            continue
        #---Se o valor digitado é '2' , Limpa o terminal e finaliza o laço
        elif int(novo_ou_sair) == 2 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Você escolheu sair!\nSaindo do programa")
            break
        #Limitação absoluta de valores a aos digitos '0,1,2'
        elif int(novo_ou_sair) != 0 and int(novo_ou_sair) != 1 and int(novo_ou_sair) != 2:
            raise ValueError('Você deve digitar uma das opções disponíveis')

    #------ Limpa o terminal e mostra Exceções personalizadas, reinicia laço
    except ValueError as erro:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(aluno)
        print(f'Ouve um problema: {erro}\nVamos tentar novamente ?')
        continue

    #------Digitação forçada ( Nome do aluno)
    aluno_nome =  input("\nNome do aluno: ")

    #------Teste de informacao digitada e lançamento de exceções personalizadas
    try:

        #Quantidade de caracteres ( Minimo permitido : 3)
        if len(aluno_nome) < 3:
            raise ValueError('Por favor digite 3 ou mais caracteres no nome do aluno!')
        #Tipo digitado ( Permitido apenas letras )
        elif any(chr.isdigit() for chr in aluno_nome):
            raise ValueError('Por favor digite apenas letras no nome do aluno!')

    #------ Limpa o terminal e mostra Exceções personalizadas, reinicia laço
    except ValueError as erro:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(aluno)
        print(f'Nome inválido: {erro}\nVamos tentar novamente ?')
        continue

    #------Digitação forçada ( Nota do aluno)
    nota_aluno =  input(f"Digite a nota Final de '{aluno_nome}': ")

    #------Teste de informacao digitada e lançamento de exceções personalizadas
    try:

        #------Quantidade de caracteres (Permite entre 1 e 5 caracteres)-----#

        #-----Se nada for digitado
        if len(nota_aluno) <1:
            raise ValueError(f"Você não digitou a nota ")

        #----- Se mais de 5 caracteres for digitado
        elif len(nota_aluno) >= 5:
            raise ValueError("Digite uma nota mais curta.")

        #---Tipo digitado ( Inteiro ou float )
        elif not isinstance(float(nota_aluno), (int, float)):
            raise ValueError("Digite um numero real no intervalo entre 0 e 10")

        #--- Limites de nota minima: 0 (Notas negativas não é permitido)
        elif  float(nota_aluno) <0:
            raise ValueError(f'Você digitou uma nota inferior a 0: {nota_aluno}')

        #--- Limites de nota maxima: 10 ou 10.0
        elif  float(nota_aluno) >10:
            raise ValueError(f'Você digitou uma nota superior a 10:  {nota_aluno}')

    #------ Limpa o terminal e mostra Exceções personalizadas, reinicia laço
    except ValueError as erro:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(aluno)
        print(f'Nota Inválida: {erro} para: {aluno_nome}\n\nVamos tentar novamente ?\n')
        continue

    #Convertendo a nota em numero flutuante
    nota_aluno = float(nota_aluno)

    #------Atribuição de conceitos
    conceito = ''

    #--Conceito "E" De 0 a 2.9
    if nota_aluno >= 0 and nota_aluno <= 2.9:
        conceito = 'E'
    #--Conceito "d" De 3 a 4.9
    elif nota_aluno >= 3 and nota_aluno <= 4.9:
        conceito = 'D'
    #--Conceito "c" De 5 a 6.9
    elif nota_aluno >= 5 and nota_aluno <= 6.9:
        conceito = 'C'
    #--Conceito "b" De 7 a 8.9
    elif nota_aluno >= 7 and nota_aluno <= 8.9:
        conceito = 'B'
    #--Conceito "a" De 9 a 10
    elif nota_aluno >= 9 and nota_aluno <= 10:
        conceito = 'A'

    #Mostra nome, nota, e conceito adquirido pelo aluno
    print(f'O aluno {aluno_nome} tirou a nota {nota_aluno} e se enquadra no conteito {conceito}\n')

#Saindo do programa
exit()
