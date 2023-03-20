green = '\033[32m'
lightgrey = '\033[37m'
red = '\033[31m'

import random

def abertura():
    print(green + '╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋┏━━━┓')
    print('╋╋┃┃╋╋╋╋╋╋╋╋╋╋╋┃┃╋╋╋╋┃┏━━┛')
    print('╋╋┃┣━━┳━━┳━━┓┏━┛┣━━┓ ┃┗━━┳━━┳━┳━━┳━━┓')
    print('┏┓┃┃┏┓┃┏┓┃┏┓┃┃┏┓┃┏┓┃ ┃┏━━┫┏┓┃┏┫┏━┫┏┓┃')
    print('┃┗┛┃┗┛┃┗┛┃┗┛┃┃┗┛┃┏┓┃ ┃┃╋╋┃┗┛┃┃┃┗━┫┏┓┃')
    print('┗━━┻━━┻━┓┣━━┛┗━━┻┛┗┛ ┗┛╋╋┗━━┻┛┗━━┻┛┗┛')
    print('╋╋╋╋╋╋┏━┛┃')
    print('╋╋╋╋╋╋┗━━┛ \n\n' )
    print( '𝗕𝗲𝗺 𝘃𝗶𝗻𝗱𝗼𝘀 𝗮𝗼 𝗷𝗼𝗴𝗼 𝗱𝗮 𝗳𝗼𝗿𝗰𝗮 \n')
    print('Olá, vamos se enforcar?\n')
    print('A dica é: FRUTAS :)\n' + lightgrey)

def secreta():
    prr = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            prr.append(linha)

    n = random.randrange(0, len(prr))
    magica = prr[n].upper()
    return magica

def certu(palavra):
    return ["_" for letra in palavra]

def tentar():
    chute = input( "Qual letra você quer? " )
    chute = chute.strip().upper()
    return chute

def correto(chute, letras_acertadas, magica):
    kc = 0
    for letra in magica:
        if (chute == letra):
            letras_acertadas[kc] = letra
        kc += 1

def vencedor():
    print("\nNão fez mais do que sua obrigação!")
    print(green + "          _____      ")
    print("        '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .'   '.        ")
    print("        '-------'       ")

def perdedor(magica):
    print(green +"  \nFinalmente, foi enforcada")
    print(green +"  \nA palavra era '{}'".format(magica.upper()))
    print(red + '''                  _  /)
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |    FRACASSADO    ||
          |                  ||
  *       | *   **    * **   |**      **
   \))ejm97/.,(//,,..,,\||(,,.,\\,.((// \n''')

def desenhos(erros):
    print("  ______      ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      /|\ ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      /|\    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      /|\    ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("|__         ")
    print()

def jogar():

    abertura()

    magica = secreta()

    letras_acertadas = certu(magica)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = tentar()

        if (chute in magica):
            correto(chute, letras_acertadas, magica)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print(green +"\nDepois de tantos erros tinha que vir os dias de glória!! A palavra era '{}'".format(magica.upper()))
        else:
            erros += 1
            print(letras_acertadas)
            print('Faltam {} letras, não desista!/n'.format(letras_faltando))
            print('Você tem {} tentativas, persista!'.format(7-erros))
            desenhos(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        vencedor()
    else:
        perdedor(magica)

    print(green + "     ___   ___   __  __ ")
    print("    | __| |_ _| |  \/  |")
    print("    | _|   | |  | |\/| |")
    print("    |_|   |___| |_|  |_|")




if(__name__ == '__main__'):
    jogar()
            