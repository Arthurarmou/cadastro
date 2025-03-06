import datetime
import time
import json
def lernumero(): #ver se contém apenas números
    while True:
        escolha = input("insira o número:").strip()
        try:
            numero = int(escolha)
            return numero
        except ValueError:
            print("você não inseriu um número")
def lernome(): #ver se apenas possui letras no valor, sem números e caractéres especiais
    while True:
        nome = input("insira seu nome:").strip()
        if nome == "":
            print("seu nome não pode ser vazio, digite novamente abaixo:")
            continue
        for char in nome:
            if not (("A" <= char <="Z") or ("a" <= char <= "z") or (char == "ç") or ("ã" <= char <="õ") or ("á"<=char <="ú") or (char == " ") or ("â"<= char <= "û")):
                print("está errado!, digite um nome que não contenha símbolo ou número!")
                break
        else:
            return nome
def lugar(): #ver se o lugar da pessoa contém apenas letras
    while True:
        nomelugar = input("insira o lugar que você quer ir:").strip()

        if nomelugar == "":
            print("seu lugar não pode ser vazio, digite novamente abaixo:")
            continue
        for char in nomelugar:
            if not (("A" <= char <= "Z") or ("a" <= char <= "z") or (char == "ç") or ("ã" <= char <= "õ") or (
                    "á" <= char <= "ú") or (char == " ") or ("â" <= char <= "û")):
                print("está errado!, digite um lugar que não tenha símbolo ou número!")
                break
        else:
            return nomelugar
def pousada(): #escolher a pousada que a pessoa irá ficar
    pousada = input("insira uma de nossas pousadas: costa mar e costa areia:").upper()
    while pousada != "COSTA AREIA" and pousada != "COSTA MAR":
        print("ops não temos essa pousada insira uma de nossas pousadas, certifique-se que todas as letras estão iguais!")
        pousada = input("insira a pousada:").upper()
    if pousada == "COSTA AREIA":
        return costaareia()
    elif pousada == "COSTA MAR":
        return costamar()
def costaareia(): #se a pessoa escolher costa areia irá chamar essa função onde contém o saldo os dias que ela ficará
    print("insira seu saldo abaixo para a transação:")
    saldo = lernumero()
    while saldo <= 0:
        print("ops, não insira um saldo negativo ou um saldo de 0!")
        saldo = lernumero()
    print("insira a quantidade de dias que quer passar em nossa pousada abaixo, cada diária é 150 reais :")
    dias = lernumero()
    while dias <=0:
        print("insira sua quantidade de dias de forma positiva!")
        dias = lernumero()
    valor = 150 * dias
    while valor > saldo:
        print("seu saldo é insuficiente! Insira um saldo maior do que será retirado de sua conta!")
        saldo = lernumero()
    novosaldo = saldo - valor
    return novosaldo, dias
def costamar(): #se a pessoa escolher costa mar irá chamar essa função onde contém o saldo os dias que ela ficará
    print("insira seu saldo abaixo para a transação:")
    saldo = lernumero()
    while saldo <= 0:
        print("ops não insira um saldo negativo ou um saldo de 0!")
        saldo = lernumero()
    print("insira a quantidade de dias que quer passar em nossa pousada abaixo, cada diária é 200 reais :")
    dias = lernumero()
    valor = 200 * dias
    while valor > saldo:
        print("seu saldo é insuficiente! Insira um saldo maior do que será retirado de sua conta!")
        saldo = lernumero()
    novosaldo = saldo - valor
    return novosaldo, dias
def imprimir_reserva(reserva): #mostar o seu cadastro atual
    print(f"seu cadastro é:{reserva}")
def imprimir_todas_reservas(lista): #mostar todos os cadastros do banco de dados
    for reserva in lista:
        print("===================")
        imprimir_reserva(reserva)
def data(dias): #mostar a data de check in e check out e adiciona-la no dicionário

    hora = datetime.date.today()
    datackin = hora + datetime.timedelta(days=4)
    datackout = datackin + datetime.timedelta(days=dias)

    dicionario["data do check-in"] = datackin.strftime('%d/%m/%Y')
    print("sua data de check-in é:", dicionario["data do check-in"])
    dicionario["data do check-out"] = datackout.strftime('%d/%m/%Y')
    print("sua data de check-out é:", dicionario["data do check-out"])
    return datackin,datackout

def ler_arquivo(): #carregar o banco de dados para um uso futuro
        with open("cadastro.json","r") as lercadastro:
            lista = json.load(lercadastro)
        return lista
def remover(lista): #remover o seu cadastro atual através do banco de dados
    lista.pop(0)
    print("seu cadastro foi excluído!")

def editar(dicionario): #editar algum item do dicionário
    print(dicionario)
    while True:
        nome = input("insira o valor que você quer editar:")
        if nome not in dicionario:
            print("o valor que você está inserindo não está na lista!")
            continue
        elif nome == "data do check-out" or nome == "data do check-in" or nome == "saldo":
            print("o valor digitado é imutável!")
            continue
        nome_editar = True
        while nome_editar:
            nome_editar = input("insira o nome que você quer substituir:")
            try:
                int(nome_editar)
                print("o nome deve conter apenas letras!")
                continue
            except:
                break
        while nome_editar == dicionario[nome] :
            print("o nome é igual, insira outro nome!")
            nome_editar = input("insira o nome que você quer substituir:")
        dicionario[nome] = nome_editar.capitalize()
        return dicionario


lista = ler_arquivo() #carregar o banco de dados

while True:
    dicionario = {} #dicionário vazio para adicionar o seu cadastro atual]
    #menu para a pessoa não botar a mesma coisa duas vezes
    nome_adicionado = False
    local_adicionado = False
    pousada_adicionada = False
    data_adicionada = False
    fechar_programa = False
    cadastro_adicionado = False
    dias = "" #dias vazio para pegar os dias que a pessoa ficará em nossa pousada

    while not (nome_adicionado and local_adicionado and pousada_adicionada and data_adicionada): #verifica se tudo foi inserido
        print("olá, seja bem vindo ao cadastro de viagem!\n1 - Para escrever seu nome\n2 - para inserir o local\n3- para inserir onde quer ficar\n4- para identificar quando vai ser o check-out e o check-in\nDigite qualquer outro número para sair!\nInsira abaixo a sua escolha!")
        menu = lernumero() #inserir o número de algo que a pessoa queira fazer
        if menu == 1 and not nome_adicionado: #botar o nome
            nome = lernome()
            dicionario["nome"] = nome.capitalize() #adicionar nome ao dicionário
            print("seu nome é:",dicionario["nome"]) #mostar o seu nome
            nome_adicionado = True #para a pessoa não botar o nome duas vezes

        elif menu == 1 and nome_adicionado: #se a pessoa já tiver botado o nome não pode botar de novo
            print("você já botou seu nome!")
            time.sleep(2)

        elif menu == 2 and not local_adicionado: #botar o lugar
            local = lugar()
            dicionario["lugar"] = local.capitalize() #adicionar lugar ao dicionário
            print("seu lugar cadastro é:",dicionario["lugar"]) #mostar o seu lugar
            local_adicionado = True #para a pessoa não botar o lugar duas vezes

        elif menu == 2 and local_adicionado: #se a pessoa já tiver botado o lugar não pode botar de novo
            print("você já botou seu lugar!")
            time.sleep(2)

        elif menu == 3 and not pousada_adicionada: #botar a pousada
            saldo, dias = pousada()
            dicionario["saldo"] = saldo #adicionar saldo ao dicionário
            print("seu saldo é:",dicionario["saldo"]) #mostar o seu saldo
            pousada_adicionada = True #para a pessoa não botar a pousada duas vezes

        elif menu == 3 and pousada_adicionada: #se a pessoa já tiver botado a pousada não pode botar de novo
            print("você já botou sua pousada!")
            time.sleep(2)

        elif menu == 4 and not data_adicionada: #mostrar a data de check-in e check-out
            try:
                data(dias)
                data_adicionada = True #para a pessoa não apertar data de novo
            except:
                print("ops, você ainda não inseriu os dias que quer ficar em nossa pousada!")
                time.sleep(2)
                continue
        elif menu == 4 and data_adicionada: #se a pessoa já tiver visto a data de check-in e check-out não pode mais usar essa parte do menu
            print("já amostramos a sua data de check-in e check-out!")
            time.sleep(2)
        elif menu >=0 or menu <4: #fechar o programa
            fechar_programa = True
        if fechar_programa: #fecha o programa
            print("fechando programa...")
            break
    if fechar_programa: #fecha o programa novamente
        break

    escolha = input("insira sim se quiser remover seu cadastro atual (qualquer outra coisa não excluirá seu cadastro):").lower() #escolha de remover cadastro
    if escolha == "sim" or escolha == "si" or escolha == "s": #se a pessoa quiser remover irá chamar a função removedora
        remover(lista)
    else:
        escolha = input("você deseja editar algo da lista, insira sim!:").lower()#se a pessoa quiser editar algo no seu cadastro atual
        if escolha == "sim": #entra no cadastro atual e bota para modificar algum item
            cadastro_adicionado = True
            editar(dicionario)
            print(f"seu novo cadastro é: {dicionario}")
        lista.append(dicionario) #adicionar o cadastro à lista
        with open("cadastro.json", "w") as cadastro: #adiciona o cadastro ao banco de dados
            lista_json = json.dumps(lista, indent=4)
            cadastro.write(lista_json)
        escolha = input("você deseja ver seu cadastro?,se sim digite ver:").upper() #ver seu cadastro atual
        if escolha == "VER":
            cadastro_adicionado = True
            imprimir_reserva(lista[-1])
        elif escolha == "VER TUDO": #ver todos os bancos de dados
            cadastro_adicionado = True
            imprimir_todas_reservas(lista)
    escolha = input("insira se deseja continuar, caso queira digite sim:").lower().strip() #escolha, caso a pessoa queira inserir mais um cadastro
    if escolha == "sim" or escolha == "si" or escolha == "s": #retorna ao lopping principal (para o menu)
        continue
    else: #caso a pessoa não escolha continuar
        if cadastro_adicionado: #se a pessoa estiver com o cadastro adicionado irá aparecer um mensagem
            print("seu cadastro foi salvo em nosso banco de dados, fechando programa...")
            break
        else: #caso a pessoa n estiver com o cadastro adicionado aparecerá essa mensagem
            print("você não fez nenhum cadastro!")
            break
