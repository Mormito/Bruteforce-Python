from utils import clear_terminal, ascii_art

clear_terminal()

arraySenha = []
senha = input("Insira aqui a senha que deseja testar: ")
path = input("Insira aqui o diretório da wordlist: ")

def BufferedReader():
    with open(path, "r") as arquivo:
        for linha in arquivo:
            arraySenha.append(linha.strip())
BufferedReader()

def BruteForce():
    cont = 0
    for i in arraySenha:
        cont += 1
        if i == senha:
            print("A senha foi encontrada: " + i)
            print("Numero de tentativas: " + str(cont))
            break
        else:
            print("Senha " + i + " incorreta.")
BruteForce()

print()
print("Code by: ")
print(ascii_art)
