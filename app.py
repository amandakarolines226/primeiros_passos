"""Este módulo realiza operações matemáticas básicas e demonstra comparações em Python."""
print('hello world!')

# Soma de três números
A = 6
B = 3
C = 2
SOMA = A + B + C
print(SOMA)

# Subtração de dois números
SUBTRACAO = A - C
print(SUBTRACAO)

# Divisão de dois números inteiros
DIVISAO = A / C
print(DIVISAO)

# Multiplicação de dois números inteiros
MULTIPLICACAO = A * B
print(MULTIPLICACAO)

# Divisão de chão (parte inteira da divisão)
DIVISAO_CHAO = A // C

# Resto da divisão
RESTO = A % C

# Exponenciação
EXPONENCIACAO = A ** B
print(EXPONENCIACAO)

# Comparações
print(A < B)    # False
print(A > B)    # True
print(A == B)   # False
print(A != B)   # True
print(A <= B)   # False
print(A >= B)   # True

# Estrutura condicional correta
if A > B:
    print('A é maior que B')
else:
    print('A é menor ou igual a B')
