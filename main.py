print("___________________")
print("_______TOWFER______")
print("___________________")


def twofer():
    nome = input("Digite o seu nome")
    if not nome:
        nome = "você"
        print(f"Um para {nome}, um para mim")
    else:
        print(f"Um para {nome}, um para mim")

twofer()