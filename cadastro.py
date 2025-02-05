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
        if saldo < 0: #não podemos efetuar nenhum pagamento se for negativo por isso voltamos ao início do looping para inseir o saldo de novo
            print("saldo está errado! bote um número positivo")
            continue
        print("digite a quantidade de dias abaixo:")
        dias = lernumero()
        print("insira os dias para ficar:")
        if dias < 0: #impossível ter dias negativos por isso voltamos ao início do looping para inseir os dias de novo
            print("dia está errado! bote um número positivo")
            continue
        preco = dias * 200
        while saldo <= preco: #não tem como ficar com saldo negativo por isso botamos um while para ele inserir o saldo novamente
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
        if saldo < 0: #não podemos efetuar nenhum pagamento se for negativo por isso voltamos ao início do looping para inseir o saldo de novo
            print("saldo inválido")
            continue
        print("insira os dias para ficar:")
        dias = lernumero()
        if dias < 0: #impossível ter dias negativos por isso voltamos ao início do looping para inseir os dias de novo
            print("insira um número positivo de dias!")
            continue
        preco = dias * 150
        while saldo < preco: #não tem como ficar com saldo negativo por isso botamos um while para ele inserir o saldo novamente
            print("seu saldo é insuficiente, insira outro saldo!")
            print("caso queira sair insira um valor negativo")
            saldo = lernumero()
            if saldo < 0:
                print("saindo")
                break
        if saldo < 0: #dois breaks para voltar de vez para o menu
            break
        novosaldo = saldo - preco
        return novosaldo
def pousada():
    print("temos duas pousadas, a costa praia e a costa mar\na costa mar está à 150 R$ por dia\na costa praia está à 200 R$ por dia")
    #caso insiram espaço incorretamente
    while True:
        escolha = input("qual pousada deseja?: ").strip().upper()
        if escolha== "": #se a variável escolha for vazia
            print("está errado o nome não pode ser vazio!")
            continue
        if escolha != "COSTA PRAIA" and escolha != "COSTA MAR":
            print("não pode ser diferente das nossas pousadas!")
            continue
        for c in escolha:
            if not("a"<= c <= "z" or "A" <= c <= "Z" or c == " "): #para verificar se existe algum número ou símbolo na variável escolha
                print("está errado")
                continue
        break
    escolha = escolha.upper()
    if escolha == "COSTA PRAIA":
        return costapraia()
    elif escolha == "COSTA MAR":
       return costamar()
def remover():
    while True:
        if not lista: #se não tiver lista ele irá retornar ao menu
            print("ops, não tem lista,dito isso fechando a o programa")
            break

        remover = input("insira o item que deseja remover, se quiser remover tudo digite tudo:") #item para remoção ou remover tudo

        if remover == "tudo" or remover == "TUDO": #if caso queira remover tudo
            lista.clear() #função para remover todos os itens da lista
            print(f"fechando o programa, pois sua lista é vazia:{lista}")
            break
        while remover not in lista:
            remover = input("ops o item não está na lista digite novamente:")
            if remover == "sair" or remover == "SAIR":
                print("fechando o programa...")
                break
            elif remover == "tudo" or remover == "TUDO":
                lista.clear()
                print("você não tem lista, dito isso fechando o código!")
                break
        if remover in lista: #se o item "remover" estiver na lista ele remve esse item
            lista.remove(remover)
            print(f"removendo o item: {remover}")
            print(f"sua nova lista é: {lista}")
            print('informe abaixo se deseja continuar, caso deseja, digite sim. Se quiser fechar o programa digite qualquer coisa:')
            escolha = lernome()
            if escolha == "sim" or escolha == "si" or escolha =="s": #caso escolha sim ele irá retornar para o início do looping no while True
                continue
            else: #se digitar qualquer outra coisa ele fecha
                break
        if not lista: #se não tiver lista ele irá retornar ao menu
            print("ops, não tem lista,dito isso fechando a o programa")
            break
        return lista #retornar lista para o programa
def editar():
    while True:
        if not lista: #se não tiver lista volta para o menu
            print("fechando o programa pois não tem lista")
            break
        nome = input("insira o item da lista que você quer editar:")
        while nome not in lista: #quando o nome que a pessoa quer editar não está na lista não tem o porque dela querer editar ele
            nome= input("insira um valor que esteja na lista!:")
        if nome in lista: #se o nome estiver escrito totalmente correto
            nomeedit = input(f"insira o que você quer substituir no lugar de {nome}:")
            index = lista.index(nome) #para procurar o nome na lista
            lista[index] = nomeedit #para trocar o nome pelo novo nome da lista
            print(f"sua lista agora é:{lista}")
            print("insira sim abaixo caso queira sair:")
            escolha = lernome()
            if escolha == "sim" or escolha == "s" or escolha == "si":
                print("fechando o programa")
                break
        return lista

lista = []
while True:
    menu = print("--olá, bem vindo ao cadastro--\n1- fazer cadastro de nome\n2- para onde você vai?\n3-em qual pousada quer ficar. Pousadas:1- Costa mar 2- Costa areia\ntemos essas opções, digite 1,2 ou 3\nSe quiser sair do programa digite algum número maior que 3 ou menor que 0: ")
    print("insira abaixo a opção desejada:")
    menu = lernumero()

    if menu == 1: #botar o menu como um número, pois é mais interativo
        nome = cadastronome() #chamar uma função para o cadastro do nome
        print("o seu nome é:", nome.capitalize()) #função para deixar maiúsculo
        lista.append(nome.capitalize()) #insere o nome à lista
        print(f"sua lista agora é: {lista}")
        print("você deseja parar de enserir itens na lista?, caso queira digite sim abaixo")
        escolha = lernome().lower().strip() #retirar o espaço no final e início e botar em minúsculo
        if escolha == "sim" or escolha == "s" or escolha == "si": #se a escolha receber sim fecha o programa
            break
    if menu == 2:
        lugardesejado = lugar() #chama uma função para o local
        print("o seu lugar é: ",lugardesejado.capitalize())
        lista.append(lugardesejado.capitalize())#insere o nome à lista
        print(f"sua lista agora é: {lista}")
        print("você deseja parar de enserir itens na lista?, caso queira digite sim abaixo")
        escolha = lernome().lower().strip() #retirar o espaço no final e início e botar em minúsculo
        if escolha == "sim" or escolha == "s" or escolha == "si":
            break
    if menu == 3:
        saldo = pousada() #chama uma função para a pousada
        print("seu saldo após a compra é de: ",saldo)
        lista.append(saldo) #insere o saldo à lista
        print(f"sua lista agora é: {lista}")
        print("você deseja parar de enserir itens na lista?, caso queira digite sim abaixo")
        escolha = lernome().lower().strip() #retirar o espaço no final e início e botar em minúsculo
        if escolha == "sim" or escolha == "s" or escolha == "si": #se a escolha receber sim fecha o programa
            break
    if menu > 3 or menu < 0:
        print("errado!\ntem que ser 1 ou 2 ou 3\ninsira sim para continuar ou qualquer coisa para parar")
        escolha = lernome().lower().strip()
        if escolha == "sim" or escolha == "s" or escolha == "si": #se a escolha receber sim fecha o programa
            continue
        else:
            print("fechando o programa!")
            break

print("sua lista é: ",lista)
escolha = input("você deseja remover ou editar algum item?.Se quiser manter como está digite qualquer coisa:").lower().strip()
if escolha == "remover":
    remover()
elif escolha == "editar":
    editar()
