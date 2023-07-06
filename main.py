while True:
    print('Opções\n1 - Reverter a Ordem das Palavras.\n2 - Remover Caracteres Duplicados.')
    print('3 - Encontrar Palindromo Mais Longo.\n4 - Colocar a Primeira Letra de Cada Frase Maiúscula')
    print('5 - Verificar se Uma String é um Anagrama de Um Palindromo.\n6 - Sair.')
    op = input('Escolha a Opção Desejada: ')
    if op.isdigit():
        op = int(op)
    if op == 6:
        break






    print('Insira uma frase para que sua ordem seja revertida: ')
    fraseInput = input()
    mix = fraseInput.split()
    mix2 = mix[::-1]
    fraseOutput = ' '.join(mix2)
    print(fraseOutput)