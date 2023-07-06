while True:
    print('Opções\n1 - Reverter a Ordem das Palavras.\n2 - Remover Caracteres Duplicados.')
    print('3 - Encontrar Palindromo Mais Longo.\n4 - Colocar a Primeira Letra de Cada Frase Maiúscula.')
    print('5 - Verificar se Uma String é um Anagrama de Um Palindromo.\n6 - Sair.')
    op = input('Escolha a Opção Desejada: ')
    if op.isdigit():  # Test if the operator texted is in fact a number.
        op = int(op)  # Transform the number texted in an integer.
    if op == 6:
        print('Programa Encerrado.')
        break
    elif op == 1:
        fInput = input('Insira uma frase para que sua ordem seja revertida: ')
        mix = fInput.split()  # Divide the string into substrings using an specified separator, in this case, blank spaces.
        mix2 = mix[::-1]  # Revert the order of all words.
        fOutput = ' '.join(mix2)  # Rearrange them and put the blank spaces back.
        print(f'Frase Entrada: {fInput}\nFrase Saída: {fOutput}')