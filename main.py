print("QUANTIFICAÇÃO DA ANÁLISE DOS PARÂMETROS MACROSCÓPIOS")

print('''\n COR DA ÁGUA
[ 1 ] - Escura
[ 2 ] - Clara
[ 3 ] - Transparente
''')

P1 = int(input("Digite sua Resposta: "))
if P1 == 1:
    P1 = 1
elif P1 == 2:
    P1 = 2
elif P1 == 3:
    P1 = 3
else:
    print("Opção Incorreta!")


print('''\n ODOR
[ 1 ] - Cheiro Forte
[ 2 ] - Cheiro Fraco
[ 3 ] - Sem Cheiro
''')


P2 = int(input("Digite sua Resposta: "))
if P2 == 1:
    P2 = 1
elif P2 == 2:
    P2 = 2
elif P2 == 3:
    P2 = 3
else:
    print("Opção Incorreta!")



print('''\n LIXO AO REDOR
[ 1 ] - Muito
[ 2 ] - Pouco
[ 3 ] - Sem Lixo
''')
P3 = int(input("Digite sua Resposta: "))
if P3 == 1:
    P3 = 1
elif P3 == 2:
    P3 = 2
elif P3 == 3:
    P3 = 3
else:
    print("Opção Incorreta!")


print('''\n MATERIAIS FLUTUANTES
[ 1 ] - Muito
[ 2 ] - Pouco
[ 3 ] - Sem materiais flutuantes
''')
P4 = int(input("Digite sua Resposta: "))
if P4 == 1:
    P4 = 1
elif P4 == 2:
    P4 = 2
elif P4 == 3:
    P4 = 3
else:
    print("Opção Incorreta!")


print('''\n ESPUMAS
[ 1 ] - Muita
[ 2 ] - Pouca
[ 3 ] - Sem espumas
''')
P5 = int(input("Digite sua Resposta: "))
if P5 == 1:
    P5 = 1
elif P5 == 2:
    P5 = 2
elif P5 == 3:
    P5 = 3
else:
    print("Opção Incorreta!")


print('''\n ÓLEOS
[ 1 ] - Muito
[ 2 ] - Pouco
[ 3 ] - Sem óleos
''')
P6 = int(input("Digite sua Resposta: "))
if P6 == 1:
    P6 = 1
elif P6 == 2:
    P6 = 2
elif P6 == 3:
    P6 = 3
else:
    print("Opção Incorreta")


print('''\n ESGOTOS
[ 1 ] - Esgoto domésticos
[ 2 ] - Fluxo superficial
[ 3 ] - Sem esgotos
''')
P7 = int(input("Digite sua Resposta: "))
if P7 == 1:
    P7 = 1
elif P7 == 2:
    P7 = 2
elif P7 == 3:
    P7 = 3
else:
    print("Opção Incorreta!")


print('''\n VEGETAÇÃO(preservação)
[ 1 ] - Alta Degradação
[ 2 ] - Baixa Degradação
[ 3 ] - Preservada
''')
P8 = int(input("Digite sua Resposta: "))
if P8 == 1:
    P8 = 1
elif P8 == 2:
    P8 = 2
elif P8 == 3:
    P8 = 3
else:
    print("Opção Incorreta!")


print('''\n USO POR ANIMAIS
[ 1 ] - Presença
[ 2 ] - Apenas marcas
[ 3 ] - Não detectado
''')
P9 = int(input("Digite sua Resposta: "))
if P9 == 1:
    P9 = 1
elif P9 == 2:
    P9 = 2
elif P9 == 3:
    P9 = 3
else:
    print("Opção Incorreta!")


print('''\n USO POR HUMANOS
[ 1 ] - Presença
[ 2 ] - Apenas marcas
[ 3 ] - Não detectado
''')
P10 = int(input("Digite sua Resposta: "))
if P10 == 1:
    P10 = 1
elif P10 == 2:
    P10 = 2
elif P10 == 3:
    P10 = 3
else:
    print("Opção Incorreta!")


print('''\n PROTEÇÃO DO LOCAL
[ 1 ] - Sem proteção
[ 2 ] - Com proteção(com acesso)
[ 3 ] - Com proteção(sem acesso)
''')
P11 = int(input("Digite sua Resposta: "))
if P11 == 1:
    P11 = 1
elif P11 == 2:
    P11 = 2
elif P11 == 3:
    P11 = 3
else:
    print("Opção Incorreta!")


print('''\n PROXIMIDADE COM RESIDÊNCIAS OU ESTABELECIMENTOS
[ 1 ] - Menos de 50 metros
[ 2 ] - Entre 50 e 100 metros
[ 3 ] - Mais de 100 metros
''')
P12 = int(input("Digite sua Resposta: "))
if P12 == 1:
    P12 = 1
elif P12 == 2:
    P12 = 2
elif P12 == 3:
    P12 = 3
else:
    print("Opção Incorreta!")


print('''\n TIPO DE ÁREA DE INSERÇÃO
[ 1 ] - Ausente
[ 2 ] - Propriedade privada
[ 3 ] - Parques ou Áreas protegidas
''')
P13 = int(input("Digite sua Resposta: "))
if P13 == 1:
    P13 = 1
elif P13 == 2:
    P13 = 2
elif P13 == 3:
    P13 = 3
else:
    print("Opção Incorreta!")


#print("\n CLASSIFICAÇÃO DAS NASCENTES \n")

resultado = int((P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11 + P12 + P13))
print(resultado)

if resultado <= 39 and resultado >= 37:
    print('''
    CLASSIFICAÇÃO DAS NASCENTES
    CLASSE A
    GRAU DE PRESERVAÇÃO - ÓTIMA
    ''')
elif resultado >= 34 and resultado <= 36:
    print('''
    CLASSIFICAÇÃO DAS NASCENTES
    CLASSE B
    GRAU DE PRESERVAÇÃO - BOA
    ''')
elif resultado >= 31 and resultado <= 33:
    print('''
    CLASSIFICAÇÃO DAS NASCENTES
    CLASSE C
    GRAU DE PRESERVAÇÃO - RAZOÁVEL
    ''')
elif resultado >= 28 and resultado <= 30:
    print('''
    CLASSIFICAÇÃO DAS NASCENTES
    CLASSE D
    GRAU DE PRESERVAÇÃO - RUIM
    ''')
elif resultado <= 27:
    print('''
    CLASSIFICAÇÃO DAS NASCENTES
    CLASSE E
    GRAU DE PRESERVAÇÃO - PÉSSIMO
    ''')