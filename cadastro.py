# cadastro 2:
import datetime
import time
import json
def lernumero():
    while True:
        escolha = input("insira o número:").strip()
        try:
            numero = int(escolha)
            return numero
        except ValueError:
            print("você não inseriu um número")
def lernome():
    nome = input("insira seu nome:")
    while True:
        if nome == "":
            nome = input("seu nome não pode ser vazio, digite novamente:")
            continue
        for char in nome:
            if not (("A" <= char <="Z") or ("a" <= char <= "z") or (char == "ç") or ("ã" <= char <="õ") or ("á"<=char <="ú") or (char == " ") or ("â"<= char <= "û")):
                print("está errado!, digite um nome que não contenha símbolo ou número!")
                nome = input("insira um nome sem números ou símbolos:")
                break
        else:
            return nome
def lugar():
    nome = input("insira o lugar que você quer ir:")
    while True:
        if nome == "":
            nome = input("seu lugar não pode ser vazio, digite novamente:")
            continue
        for char in nome:
            if not (("A" <= char <= "Z") or ("a" <= char <= "z") or (char == "ç") or ("ã" <= char <= "õ") or (
                    "á" <= char <= "ú") or (char == " ") or ("â" <= char <= "û")):
                print("está errado!, digite um lugar que não tenha símbolo ou número!")
                nome = input("insira um lugar sem números ou símbolos:")
                break
        else:
            return nome
def pousada():
    pousada = input("insira uma de nossas pousadas: costa mar e costa areia:").upper()
    while pousada != "COSTA AREIA" and pousada != "COSTA MAR":
        print("ops não temos essa pousada insira uma de nossas pousadas, certifique-se que todas as letras estão iguais!")
        pousada = input("insira a pousada:").upper()
    if pousada == "COSTA AREIA":
        return costaareia()
    elif pousada == "COSTA MAR":
        return costamar()
def costaareia():
    print("insira seu saldo abaixo para a transação:")
    saldo = lernumero()
    while saldo <= 0:
        print("ops não insira um saldo negativo!")
        saldo = lernumero()
    print("insira a quantidade de dias que quer passar em nossa pousada abaixo, cada diária é 150 reais :")
    dias = lernumero()
    valor = 150 * dias
    while valor > saldo:
        print("seu saldo é insuficiente! Insira um saldo maior do que será retirado de sua conta!")
        saldo = lernumero()
    novosaldo = saldo - valor
    return novosaldo, dias
def costamar():
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
def imprimir_reserva(reserva):
    print(f"seu cadastro é:{reserva}")
def imprimir_todas_reservas(lista):
    for reserva in lista:
        print("===================")
        imprimir_reserva(reserva)
def data(dias):

    hora = datetime.date.today()
    datackin = hora + datetime.timedelta(days=4)
    datackout = datackin + datetime.timedelta(days=dias)

    dicionario["data do check-in"] = datackin.strftime('%d/%m/%Y')
    print("sua data de check-in é:", dicionario["data do check-in"])
    dicionario["data do check-out"] = datackout.strftime('%d/%m/%Y')
    print("sua data de check-out é:", dicionario["data do check-out"])
    return datackin,datackout

def ler_arquivo():
        with open("cadastro.json","r") as lercadastro:
            lista = json.load(lercadastro)
        return lista
def remover(lista):
    lista.pop(0)
    print("seu cadastro foi excluído!")

def editar(dicionario):
    print(dicionario)
    nome = input("insira o valor que você quer editar:")

    while nome not in dicionario:
        print("o valor que você está inserindo não está na lista!")
        nome = input("insira um valor válido:")

    nome_editar = input("insira o nome que você quer substituir")
    dicionario[nome] = nome_editar.capitalize()
    return dicionario
lista = ler_arquivo()

while True:
    dicionario = {}
    nome_adicionado = False
    local_adicionado = False
    pousada_adicionada = False
    data_adicionada = False
    fechar_programa = False
    dias = ""

    while not (nome_adicionado and local_adicionado and pousada_adicionada and data_adicionada):
        print("olá, seja bem vindo ao cadastro de viagem!\n1 - Para escrever seu nome\n2 - para inserir o local\n3- para inserir onde quer ficar\n4- para identificar quando vai ser o check-out e o check-in\nDigite qualquer outro número para sair!\nInsira abaixo a sua escolha!")
        menu = lernumero()
        if menu == 1 and not nome_adicionado:
            nome = lernome()
            dicionario["nome"] = nome.capitalize()
            print("seu nome é:",dicionario["nome"])
            nome_adicionado = True

        elif menu == 1 and nome_adicionado:
            print("você já botou seu nome!")
            time.sleep(2)

        elif menu == 2 and not local_adicionado:
            local = lugar()
            dicionario["lugar"] = local.capitalize()
            print("seu lugar cadastro é:",dicionario["lugar"])
            local_adicionado = True

        elif menu == 2 and local_adicionado:
            print("você já botou seu lugar!")
            time.sleep(2)

        elif menu == 3 and not pousada_adicionada:
            saldo, dias = pousada()
            dicionario["saldo"] = saldo
            print("seu saldo é:",dicionario["saldo"])
            pousada_adicionada = True

        elif menu == 3 and pousada_adicionada:
            print("você já botou sua pousada!")
            time.sleep(2)
        elif menu == 4 and not data_adicionada:
            try:
                data(dias)
                data_adicionada = True
            except:
                print("ops, você ainda não inseriu os dias que quer ficar em nossa pousada!")
                time.sleep(2)
                continue
        elif menu == 4 and data_adicionada:
            print("já amostramos a sua data de check-in e check-out!")
            time.sleep(2)
        elif menu >=0 or menu <4:
            fechar_programa = True
        if fechar_programa:
            print("fechando programa...")
            break
    if fechar_programa:
        break

    escolha = input("insira sim se quiser remover seu cadastro atual(qualquer outra coisa não excluirá seu cadastro):").lower()
    if escolha == "sim" or escolha == "si" or escolha == "s":
        remover(lista)
    else:
        escolha = input("você deseja editar algo da lista, insira sim!:").lower()
        if escolha == "sim":
            editar(dicionario)
        lista.append(dicionario)
        with open("cadastro.json", "w") as cadastro:
            lista_json = json.dumps(lista, indent=4)
            cadastro.write(lista_json)
        escolha = input("você deseja ver seu cadastro?,se sim digite ver:").upper()
        if escolha == "VER":
            imprimir_reserva(lista[-1])
        elif escolha == "VER TUDO":
            imprimir_todas_reservas(lista)
    escolha = input("insira se deseja continuar, caso queira digite sim:").lower().strip()
    if escolha == "sim" or escolha == "si" or escolha == "s":
        continue
    else:
        print("seu cadastro foi salvo em nosso site, fechando programa...")
        break
