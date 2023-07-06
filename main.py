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
        f_input = input('Insira uma frase para que sua ordem seja revertida: ')
        mix = f_input.split()  # Divide the string into substrings using a specified separator, in this case, blank spaces.
        mix2 = mix[::-1]  # Revert the order of all words.
        f_output = ' '.join(mix2)  # Rearrange them and put the blank spaces back.
        print(f'Frase Digitada: {f_input}\nFrase Revertida: {f_output}')

    elif op == 2:
        remove_dupli = input('Insira uma frase para que suas letras duplicas sejam removidas: ')
        letras = []  # empty list to receive the unique letters.

        for i in remove_dupli:
            if i not in letras:  # tests if the list already has the letter for each of the letters of remove_dupli
                letras.append(i)

        frase_resposta = ''.join(letras)
        print(f'Frase Digitada: {remove_dupli}\nFrase Sem Letras Duplicadas: {frase_resposta}')

    elif op == 3:
        palin = input('Insira uma frase para que o palindromo mais longo seja encontrado: ')
        tam_palin = 0
        for i in range(len(palin)):
            j, k = i, i
            while j >= 0 and k < len(palin) and palin[j] == palin[k]:
                if (k - j + 1) > tam_palin:
                    tam_palin = k - j + 1
                    resul_palin = palin[j:k+1]
                j -= 1
                k += 1
        print(resul_palin)
    elif op == 4:
        print()
    elif op == 5:
        print()
    else:  # If something wrong is typed in return to the start of the While
        print("Opção escolhida inválida.")
        continue