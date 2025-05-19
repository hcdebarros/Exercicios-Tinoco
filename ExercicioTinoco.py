# Realizar divisão através de soma

num = int(input("Digite um número: "))
divisor = int(input("Digite um divisor: "))
cont = 0
resultado = 0
resto = 0



for i in range(0,num + 1, divisor):
        if i < num:
            resultado +=1
            cont += divisor
            if cont > num:
                cont -= divisor
                resultado -= 1
                resto = num - cont
                

                
    
print(f'O resultado da divisão é: {resultado}')
print(f'O resto da divisão é: {resto}')
    