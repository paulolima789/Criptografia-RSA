import random as rd
import math


def gerar_chave_publica(n: int) -> list:
    e_lista = []
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            e_lista.append(i)
        if len(e_lista) > 9999:
            break
    return rd.choice(e_lista)


def gerar_chave_privada(totiente: int, e: int) -> int:
    d = pow(e, -1, totiente)
    return d


def cifrar(mensagem: str, e: int, n: int) -> list:
    msg_cifrada = []
    for letra in mensagem:
        let = ord(letra)
        l_msg = (let ** e) % n
        msg_cifrada.append(str(l_msg))
    msg_cifrada = ','.join(msg_cifrada)
    return cifraVirgula(msg_cifrada, e, n)


def cifraVirgula(msg: list, e: int, n: int) -> str:
    listaL = []
    for i in msg:
        listaL.append(str(i))
    multiplicador = e * n
    mull = []
    for k in listaL:
        if k == ',':
            indexl = listaL.index(k)
            listaL[indexl] = str(multiplicador)
            int(multiplicador)
            mull.append(multiplicador)
            multiplicador += multiplicador
    listaL = ''.join(listaL)
    return listaL


def decifrarVirgula(mensagem: str, d: int, e: int, n: int) -> str:
    kf = n * e
    listaNT = []
    while True:
        if str(kf) in mensagem:
            listaNT.append(str(kf))
            int(kf)
            kf += kf
        else:
            break
    for i in listaNT:
        mensagem = mensagem.replace(i, ',')
    return decifrar(mensagem, n, d)


def decifrar(mensagem: str, n: int, d: int, ) -> str:
    msg_decifrada = []
    mensagem = mensagem.split(',')
    for letra in mensagem:
        l_msg = pow(int(letra), d, n)
        l_msg = chr(l_msg)
        msg_decifrada.append(l_msg)
    return "".join(msg_decifrada)


def criptografia_rsa():
    msg = str(input('mensagem: '))
    p = 47
    q = 1009
    n = p * q
    totiente = (p - 1) * (q - 1)
    e = gerar_chave_publica(totiente)
    d = gerar_chave_privada(totiente, e)

    print(f'\nChave publica: ({n} , {e})')
    print(f'\nChave privada: ({n} , {d})')

    msg = cifrar(msg, e, n)
    print('\nMENSAGEM CIFRADA:  ')
    print(msg)

    mensagem = input('\nInforme o texto para descriptografar: ')
    msg = decifrarVirgula(mensagem, d, e, n)
    print(f'\nMENSAGEM DECIFRADA: {msg}')


"""criptografia_rsa()
print('Terminou')
"""

def primo(n): # verifica se o número é primo
    if n <= 1:
        return False

    if n <=3:
        return True

    if n%2 == 0 or n%3 == 0:
        return False

    i = 5
    while (i * i) <= n:
        if (n % i) == 0 or (n % (i + 2)) == 0:
            return False
        i += 6
    return True


def gerar_numero(): # gera um número primo aleatório

    while True:
        numero = rd.randint(1000, 9999)
        if primo(numero) == True:
            return numero
def gerar_chaves():
    p = gerar_numero()
    q = gerar_numero()

    #p = 42
    #q = 1009
    n = p * q
    totiente = (p - 1) * (q - 1)
    e = gerar_chave_publica(totiente)
    d = gerar_chave_privada(totiente, e)
    return {'publica': f"{n},{e}", 'privada': f"{n},{d}"}


