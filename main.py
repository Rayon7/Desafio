while True:
    print('Opções\n1 - Reverter a Ordem das Palavras.\n2 - Remover Caracteres Duplicados.')
    print('3 - Encontrar Palindromo Mais Longo.\n4 - Colocar a Primeira Letra de Cada Frase Maiúscula.')
    print('5 - Verificar se Uma String é um Anagrama de Um Palindromo.\n6 - Sair.')
    op = input('Escolha a Opção Desejada: ')
    if op.isdigit():  # Test if the operator texted is in fact a number.
        op = int(op)  # Transform the number texted in an integer.

    if op == 6:  # Ends the infinite loop.
        print('Programa Encerrado.')
        break

    elif op == 1:
        fInput = input('Insira uma frase para que sua ordem seja revertida: ')
        mix = fInput.split()  # Divide the string into substrings using a specified separator, in this case, blank spaces.
        mix2 = mix[::-1]  # Revert the order of all words.
        fOutput = ' '.join(mix2)  # Rearrange them and put the blank spaces back.
        print(f'Frase Digitada: {fInput}\nFrase Revertida: {fOutput}')

    elif op == 2:
        removeDupli = input('Insira uma frase para que suas letras duplicas sejam removidas: ')
        letras = []

        for i in removeDupli:
            if i not in letras:
                letras.append(i)
        print(f'Frase Digitada: {removeDupli}\nFrase Sem Letras Duplicadas: {letras}')
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    else:  # If something wrong is typed in return to the start of the While
        print("Opção escolhida inválida.")
        continue