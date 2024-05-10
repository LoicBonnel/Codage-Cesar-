# Chiffement César --> decale la saisie de 3

def decaler(lettre, n = 3):
    alphabet = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"
    for i in range(len(alphabet)):
        if lettre == alphabet[i]:
            if i+n > len(alphabet)-1:
                return alphabet[i + n -len(alphabet)]
            else:
                return alphabet[i+n]
    return lettre

def cesar (L, n = 3):  #cesar --> nom du chiffrement
    C = []
    for lettre in L:
        t = decaler(lettre, n)
        C.append(t)
    return ''.join(C)     # permet de retourner le caractaire s'il n'est pas prit en charge par le programe


def dechifrer(L, n=3):
    return cesar (L, n)


def vignere(message, cle):
    clerepetee = []
    C = []
    for i in range(len(message)):
        lettre = message[i]
    t = decaler(lettre, -place(cle[i % len(cle)]))
    C.append(t)
    return''.join(C)

assert (cesar("LOIC")==("ORLF"))    # teste : si le teste n'est pas bon --> erreurs --> arret du programe

message = "LOI   '678C"
print(cesar(message,3))
