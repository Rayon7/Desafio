print('Insira uma frase para que sua ordem seja revertida: ')
fraseInput = input()
mix = fraseInput.split()
mix2 = mix[::-1]
fraseOutput = ' '.join(mix2)
print(fraseOutput)
print('Teste de push e commit')