import os
import unicodedata


def gera_email(nome='', sobrenome='', ru=''):

    # Testando os dados para verificar se cumpre os requisitos nescessários
    try:
        # Quantidade de caracteres
        if len(nome) < 1:
            raise ValueError('Você não digitou o nome')
        elif len(nome) >= 1 and len(nome) < 3:
            raise ValueError('Insira 3 ou mais caracteres no nome')
        elif len(sobrenome) < 1:
            raise ValueError('Você não digitou o sobrenome')
        elif len(sobrenome) >= 1 and len(sobrenome) < 3:
            raise ValueError('Insira 2 ou mais caracteres no no sobrenome')
        # Tipo digitado
        elif isinstance(int(ru), int) == False:
            raise ValueError("Só é aceito numeros no RU")
        elif any(chr.isdigit() for chr in nome):
            raise ValueError('Digite apenas letras no nome!')
        elif any(chr.isdigit() for chr in sobrenome):
            # Se tiver numeros gera exceção
            raise ValueError('Digite apenas letras no sobrenome!')
    except ValueError as erro:
        # Retorna dicionario com o erro
        return {"Erro": erro}

    # remoçao de acentos do nome e sobrenome para gerar email
    try:
        # tornando Unicode
        email_nome = unicode(nome, 'utf-8')
        email_sobrenome = unicode(sobrenome, 'utf-8')
    except NameError:
        pass
    # Mudando de Utf8 para ascii
    email_nome = unicodedata.normalize('NFD', nome.replace(" ", ""))\
        .encode('ascii', 'ignore')\
        .decode("utf-8")
    email_sobrenome = unicodedata.normalize('NFD', sobrenome.replace(" ", ""))\
        .encode('ascii', 'ignore')\
        .decode("utf-8")
    # Retorna dados do aluno ( nome, sobrenome, email)

    return {"Sucesso": f"O Sr {nome} {sobrenome} seu email é : {email_nome[0].lower()}{email_sobrenome.lower()}{ru[-2::]}@algoritmos.com.br"}


while True:
    print('Antonio José Jacinto Cintra - RU: 3420397\n')

    # Solicitando dados do aluno
    aluno_nome = input('Nome do aluno: ')
    aluno_sobrenome = input('Sobrenome do aluno: ')
    aluno_ru = input('RU do aluno: ')
    # Executando função e armazenando resultado em variavel
    resultado = gera_email(aluno_nome, aluno_sobrenome, aluno_ru)
    # Verificando e exibindo exceções
    if 'Erro' in resultado.keys():
        print('Ouve um problema: {}\n Vamos tentar novamente ?'.format(
            resultado['Erro']))
        continue
    # Verificando resultado e exibindo dados em caso de sucesso
    elif 'Sucesso' in resultado.keys():
        print(resultado['Sucesso'])
        # Finalizando o laço
        break
