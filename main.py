from interface.menu import menu, validar_opcao, chamar_opcao, selecionar_opcao, get_opcoes, gerar_novas_chaves, limpar



limpar()
while True:
    menu()
    index = selecionar_opcao()
    chamar_opcao(index)

    limpar()



