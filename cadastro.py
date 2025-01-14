def cadastronome():
    cadastronome = input("insira o seu nome: ")
    while cadastronome == "": #lopping primário para validar nome vazio
        print("opa, o nome está errado!")
        cadastronome = input("insira o nome novamente: ")
    while True: #lopping para verificar números, símbolos e nomes vazios invalidá-los
        if cadastronome == "": #nova verificação, pois quando entramos nesta verificação sem o if para identificar o nome vazio se botarmos outro nome dará errado
            print("está incorreto tente novamente")
            cadastronome = input("insira seu nome: ")
            continue #para voltar para o While True e validar o nome de novo
        for char in cadastronome:
             if not (("A" <= char <= "Z") or ("a" <= char <= "z") or (char == " ") or (char == "ã") or (char == "õ") or ("á" <= char <= "ú") or char =="ç" or ("â" <= char <= "û")): #o inverso da condição if, se usasemos o if normalmente sem o not ele validaria como erradas essas caracteres e botariam os símbolos como certos
                print("o nome está errado, ele não pode receber símbolos")
                cadastronome = (input("insira novamente: "))
                break
        else: #else para caso não aconteça nada do While True
            return cadastronome
def lugar():
    lugar = input("insira o local que deseja ir: ")
    while True:
        if lugar == "":
            print("está errado!")
            lugar = input("insira novamente o local: ")
            continue
        for char in lugar:
            if not (("A" <= char <= "Z") or ("a" <= char <= "z") or (char == " ") or (char == "ã") or (char == "õ") or ("á" <= char <= "ú") or char == "ç" or ("â" <= char <= "û")):
                print("está errado")
                lugar = input("insira novamente o local: ")
                break
        else:
            return lugar
def lernumero():
    while True:
        escolha = input("insira um número: ")
        try:
            numero = int(escolha)
            return numero
        except:
            print("valor inválido!, insira um número, não uma letra ou símbolo")
def lernome():
    while True:
        nome = input("insira a sua escolha!: ")
        if nome == "":
            print("está errado escreva um nome não vazio!")
            continue
        for char in nome:
            if not (("A" <= char <= "Z") or ("a" <= char <= "z") or (char == " ") or (char == "ã") or (char == "õ") or ("á" <= char <= "ú") or char =="ç" or ("â" <= char <= "û")):
                print("está errado insira apenas letras e espaços!")
                break
        else:
            return nome

def costapraia():
    while True:
        print("insira seu saldo:")
        saldo = lernumero()
        if saldo < 0:
            print("saldo está errado! bote um número positivo")
            continue
        print("digite a quantidade de dias abaixo:")
        dias = lernumero()
        print("insira os dias para ficar:")
        if dias < 0:
            print("dia está errado! bote um número positivo")
            continue
        preco = dias * 200
        while saldo <= preco:
            print("seu saldo é insuficiente, insira outro saldo!")
            print("caso queira sair insira um valor negativo")
            saldo = lernumero()
            if saldo < 0:
                print("saindo...")
                break
        if saldo < 0:
            break
        novosaldo = saldo - preco
        return novosaldo
def costamar():
    while True:
        print("insira seu saldo:")
        saldo = lernumero()
        if saldo < 0:
            print("saldo inválido")
            continue
        print("insira os dias para ficar:")
        dias = lernumero()
        if dias < 0:
            print("insira um número positivo de dias!")
            continue
        preco = dias * 150
        while saldo < preco:
            print("seu saldo é insuficiente, insira outro saldo!")
            print("caso queira sair insira um valor negativo")
            saldo = lernumero()
            if saldo < 0:
                print("saindo")
                break
        if saldo < 0:
            break
        novosaldo = saldo - preco
        return novosaldo
def pousada():
    print("temos duas pousadas, a costa praia e a costa mar\na costa mar está à 150 R$ por dia\na costa praia está à 200 R$ por dia")
    escolha = input("qual pousada deseja?: ").strip()#caso insiram espaço incorretamente
    while True:
        if escolha== "":
            print("está errado!")
            escolha = input("insira novamente o local: ")
            continue
        if not all(("a" <= c <= "z" or "A" <= c <= "Z" or c == " ") for c in escolha):
            print("está errado")
            escolha = input("insira novamente o local: ")
            continue
        break
    escolha = escolha.upper()
    if escolha == "COSTA PRAIA":
        return costapraia()
    elif escolha == "COSTA MAR":
       return costamar()
lista = []
while True:
    menu = print("--olá, bem vindo ao cadastro--\n1- fazer cadastro de nome\n2- para onde você vai?\n3-em qual pousada quer ficar. Pousadas:1- Costa mar 2- Costa areia\ntemos essas opções, digite 1,2 ou 3: ")
    print("insira abaixo a opção desejada:")
    menu = lernumero()

    if menu == 1: #botar o menu como um número, pois é mais interativo
        nome = cadastronome() #chamar uma função para o cadastro do nome
        print("o seu nome é:", nome)
        lista.append(nome)
        print("você deseja sair?, caso queira digite sim abaixo")
        escolha = lernome().lower()
        if escolha == "sim" or escolha == "s" or escolha == "si":
            break

    if menu == 2:
        lugardesejado = lugar()
        print("o seu lugar é: ",lugardesejado)
        lista.append(lugardesejado)
        print("você deseja sair?, caso queira digite sim abaixo")
        escolha = lernome().lower()
        if escolha == "sim" or escolha == "s" or escolha == "si":
            break

    if menu == 3:
        saldo = pousada()
        print("seu saldo após a compra é de: ",saldo)
        lista.append(saldo)
        print("você deseja sair?, caso queira digite sim abaixo")
        escolha = lernome().lower()
        if escolha == "sim" or escolha == "s" or escolha == "si":
            break
    if menu > 3 or menu < 0:
        print("errado!\ntem que ser 1 ou 2 ou 3\ninsira sim para continuar ou qualquer coisa para parar")
        escolha = lernome().lower()
        if escolha == "sim" or escolha == "s" or escolha == "si":
            continue
        else:
            print("fechando o programa!")
            break

print("sua lista é: ",lista)
while True:
    escolha = input("você deseja remover algum item?")
    if escolha == "sim" or escolha == "s" or escolha == "si":
        print("insira o índice do ítem abaixo,(sequência onde o item está) para remove-lo. EX: 1,2,3,4...:")
        remover = lernumero()
        while 0 > remover or remover >= len(lista):
            print("está incorreto, insira um número do meio da lista")
            remover = lernumero()
    remover -= 1
    itemremovido = lista.pop(remover)
    print("o item retirado foi: ",itemremovido)
    print("sua nova lista é: ", lista)
    print("você deseja sair do programa e parar de excluir item?. Digite abaixo sim para sair")
    escolha = lernome().lower()
    if escolha == "sim" or escolha == "s" or escolha == "si":
        break
