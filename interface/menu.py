import os
import json
from criptografia.rsa import gerar_chaves, cifrar, decifrarVirgula
import time


def get_opcoes(index: str = 'tudo') -> dict:
    dict_opcoes: dict = {
        '1': {
            'texto': 'Gerar Novas Chaves',
            'funcao': gerar_novas_chaves,
        },
        '2': {
            'texto': 'Visualizar Chaves',
            'funcao': visualizar_chaves,
        },
        '3': {
            'texto': 'Criptografar Texto',
            'funcao': criptografar_texto,
        },
        '4': {
            'texto': 'Decriptar Texto',
            'funcao': decriptar_texto,
        },
        '0': {
            'texto': 'Sair',
            'funcao': exit,
        },
    }
    return dict_opcoes if index == 'tudo' else dict_opcoes[index]


def limpar() -> None:
    """
    Limpa a Tela
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(msg: str = "BEM VINDO AO SISTEMA DE CRIPTOGRAFIA", opcao=None) -> None:
    if opcao is None:
        opcao = get_opcoes()
    print(f"..........::::::::::  {msg}   ::::::::::..........\n")
    for i, dados in opcao.items():
        print(f"{i} - {dados['texto']}")


def validar_opcao(index: str, opcoes: dict) -> float:
    return True if index in opcoes.keys() else False


def confirmar(mensagem: str) -> float:
    confirmacao = input(mensagem + '\n responda [S ou N]: ')
    return True if confirmacao.lower() == 's' else False


def salvar_chave(chaves: dict) -> None:
    with open('keys.json', 'w') as f:
        json.dump(chaves, f)


def gerar_novas_chaves():
    opcoes = {
        '1': {
            'texto': 'Salvar Chave Para Uso no Sistema.',
        },
        '0': {
            'texto': 'Voltar',
        },
    }
    chaves = gerar_chaves()

    while True:
        limpar()
        menu('GERAR NOVAS CHAVES', opcoes)
        print(f"\n Chave Pública: {chaves['publica']}\n Chave Privada: {chaves['privada']}")
        index = selecionar_opcao()
        if index == '0':
            break
        elif index == '1':
            salvar_chave(chaves)
            print('Chaves Salvas Com Sucesso!')
            input("\n\nPressione ENTER para retornar.")
            break
        else:
            print('Informe uma opção válida ex.: 2')
            time.sleep(2)


def chamar_opcao(index: str) -> None:
    validar = validar_opcao(index, get_opcoes())
    if validar is False:
        print('Informe uma opção válida ex.: 2')
        time.sleep(2)
    elif validar is None:
        return
    else:
        get_opcoes(index)['funcao']()


def visualizar_chaves():
    limpar()
    menu("CHAVES CADASTRADAS NO SISTEMA", {})
    try:
        chaves = carregar_chaves()
        print(f"\n Chave Pública: {chaves['publica']}\n Chave Privada: {chaves['privada']}")
        input("\n\nPressione ENTER para retornar.")
    except:
        print('\nNão foi possivel encontrar o arquivo, verifique sua integridade ou gere novas chaves.')
        time.sleep(2)

def carregar_chaves():
    with open('keys.json', 'r') as f:
        return json.load(f)


def importar_chave_publica():
    pass


def selecionar_opcao(msg: str = "\nSelecione uma das opções: ") -> str:
    return input(msg)


def criptografar_texto():
    limpar()
    opcoes = {
          '1': {
              'texto': 'Utilizar Chaves do Sistema.',
          },
          '2': {
                  'texto': 'Utilizar Chave Externa.',
              },
          '0': {
              'texto': 'Voltar',
          },
      }
    menu("CRIPTOGRAFAR MENSAGEM", opcoes)
    index = selecionar_opcao()

    if index == '1':
      try:
        chaves = carregar_chaves()
        chaves: dict = quebrar_string_chaves(chaves)
        chave: list = chaves['publica']
      except:
        print('\nNão foi possivel encontrar o arquivo, verifique sua integridade ou gere novas chaves.')
        return
    elif index == '2':
      chaves = input('\nInforme a chave pública a ser usada na criptografia ex.(n,e):\n')
      chave = chaves.split(',')
      
    while True:
        mensagem = input("Informe a mensagem a ser criptografada (obs.: máximo 180 caracteres): \n")
        if len(mensagem) > 180:
            print('Tamanho da mensagem excedeu o limite de 180 caracteres.')
            time.sleep(2)
        elif len(mensagem) == 0:
            break
        else:
          try:
            mensagem_cifrada = cifrar(mensagem, int(chave[1]), int(chave[0]))
            print(f"\nMensagem Criptografada: \n{mensagem_cifrada}")
            break
          except IndexError:
            print('\nFormato da chave inválido não foi possivel criptografar a mensagem.).\n')
            time.sleep(2)
            break
    input("\n\nPressione ENTER para retornar.")


def quebrar_string_chaves(chaves: dict) -> dict:
    chaves_dict = {
        'publica': [],
        'privada': []
    }
    for i, j in chaves.items():
        keys = j.split(',')
        chaves_dict[i] = keys
    return chaves_dict


def decriptar_texto():
    limpar()

    menu("DECIFRAR MENSAGEM", {})

    try:
        chaves = carregar_chaves()
    except:
        print('\nNão foi possivel encontrar o arquivo, verifique sua integridade ou gere novas chaves.')
        return
      
    chaves: dict = quebrar_string_chaves(chaves)
    chave_publica: list = chaves['publica']
    chave_privada: list = chaves['privada']

    

  
    while True:
        mensagem = input("Informe a mensagem a ser decifrada: \n")
        mensagem_decifrada = decifrarVirgula(mensagem,int(chave_privada[1]), int(chave_publica[1]), int(chave_publica[0]))
        print(f"\nMensagem Decifrada: \n{mensagem_decifrada}")
        break
    input("\n\nPressione ENTER para retornar.")
