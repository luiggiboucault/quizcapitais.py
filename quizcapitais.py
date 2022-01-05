print("Bem vindo ao meu quiz!")

jogador = input("Esta pronto para jogar, sim ou não? ")

if jogador.lower() != "sim":
    quit()

print("Teremos cinco perguntas.")
print("Vamos começar !")
ponto = 0

resposta = input("Qual a capital de São Paulo? ")
if resposta.lower() == "sao paulo":
    print("Resposta certa! ")
    ponto += 1
else:
    print("Resposta errada! ")

resposta = input("Qual a capital da Bahia? ")
if resposta.lower() == "salvador":
    print("Resposta certa! ")
    ponto += 1
else:
    print("Resposta errada! ")

resposta = input("Qual a capital do Espirito Santo? ")
if resposta.lower() == "vitoria":
    print("Resposta certa! ")
    ponto += 1
else:
    print("Resposta errada! ")

resposta = input("Qual a capital de Santa Catarina? ")
if resposta.lower() == "florianopolis":
    print("Resposta certa! ")
    ponto += 1
else:
    print("Resposta errada! ")

resposta = input("Qual a capital de Goias? ")
if resposta.lower() == "goiania":
    print("Resposta certa! ")
    ponto += 1
else:
    print("Resposta errada! ")

print("Você fez " + str(ponto) + " questões corretas! ")