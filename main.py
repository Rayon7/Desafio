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
        if f_input.isalpha():
            mix = f_input.split()  # Divide the string into substrings using a specified separator, in this case, blank spaces.
            mix2 = mix[::-1]  # Revert the order of all words.
            f_output = ' '.join(mix2)  # Rearrange them and put the blank spaces back.
            print(f'Frase Digitada: {f_input}\nFrase Revertida: {f_output}')

        else:
            print('Digite apenas letras.')

    elif op == 2:
        remove_dupli = input('Insira uma frase para que suas letras duplicas sejam removidas: ')
        if remove_dupli.isalpha():
            letras = []  # empty list to receive the unique letters.
            for i in remove_dupli:
                if i not in letras:  # tests if the list already has the letter for each of the letters of remove_dupli
                    letras.append(i)

            frase_resposta = ''.join(letras)
            print(f'Frase Digitada: {remove_dupli}\nFrase Sem Letras Duplicadas: {frase_resposta}')
        else:
            print('Digite apenas letras.')

    elif op == 3:
        palin = input('Insira uma frase para que o palindromo mais longo seja encontrado: ')
        if palin.isalpha():

            tam_palin = 0  # Initializing the variable.
            for i in range(len(palin)):  # The for loop iterates over each position "i" in the string.
                j, k = i, i  # The loop check for palindromes centered at "i" of odd length.
                while j >= 0 and k < len(palin) and palin[j] == palin[k]:  #  The while loop continues as long as "j" and "k" are
                    if (k - j + 1) > tam_palin:  #  whithin the bounds of the string and the characters at those positions are equal.
                        tam_palin = k - j + 1
                        resul_palin = palin[j:k+1]
                        j -= 1
                        k += 1

            print(f'Maior Palindromo encontrado: {resul_palin}')

        else:
            print('Digite apenas letras.')

    elif op == 4:
        frase_maiuscula = input('Insira uma frase para tornar cada inicio de frase maiúsculo: ')
        while True:
            print('Escolha o método de separação da frase')
            print('1 - Para " " Espaço. 2 - Para "." Ponto. 3 - Cancelar')
            op = input('Escolha a Opção Desejada: ')

            if op.isdigit():
                op = int(op)

            if op == 3:
                print('Opção cancelada.')
                break

            elif op == 1:
                frase1 = frase_maiuscula.split()  # The same principle as the first task
                result = []

                for i in frase1:
                    i = i.capitalize()  # This method capitalizes all the first letters of the phrase.
                    result.append(i)

                frase_maiuscula = ' '.join(result)
                print(f'Resultado: {frase_maiuscula}')
                break  # End the infinite loop

            elif op == 2:
                frase1 = frase_maiuscula.split('. ')  # The same principle as the first task but this time separating by .
                result = []

                for i in frase1:
                    i = i.capitalize()
                    result.append(i)

                frase_maiuscula = '. '.join(result)
                print(f'Resultado: {frase_maiuscula}')
                break  # End the infinite loop

            else:
                print('Opção inválida')
                continue

    elif op == 5:
        anagram_palin = input('Insira uma palavra para verificar se é um anagrama de um palindromo: ')
        anagram_palin = anagram_palin.replace(' ', '').lower()  # Remove the blank spaces and change the phrase to lower case.
        counter = {}

        for i in anagram_palin:  # Counts the frequency of every character in the string.
            counter[i] = counter.get(i, 0) + 1

        num_odd = 0
        for j in counter.values():  # Verifies if at max there is only one odd numbered letter.
            if j % 2 != 0:
                num_odd += 1

            anagram_result = True

            if num_odd > 1:
                anagram_result = False

        if anagram_result:
            print(f'O resultado de {anagram_palin} é...')
            print('true')

        else:
            print(f'O resultado de {anagram_palin} é...')
            print('false')

    else:  # If something wrong is typed in return to the start of the While loop.
        print("Opção escolhida inválida.")
        continue