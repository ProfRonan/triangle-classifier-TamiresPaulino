a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

if a + b > c and a + c > b and b + c > a:

    if a==b and b==c:
        print('Equilátero')
    elif a==b or b==c or a==c:
        print('Isósceles')
    else:
        print('Escaleno')
else: 
    print('Não é um triângulo')
