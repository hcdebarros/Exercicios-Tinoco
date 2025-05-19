# Fazer um quadrado com diagonal
#  oq fazer? 
# colocar um asteristico na primeira e ultima linha sempre
# sempre colocar na primeira coluna
# sempre colocar na ultima coluna
# colocar na diagonal
# for dentro de for é uma matriz[i,j]


num = int(input('Digite o tamanho do quadrado: '))

for i in range(num):
    for j in range(num):
        
        
        if i == 0 or i == num - 1 or j == 0 or i == j or j == num-1:
            print('*', end = ' ')
        else: 
            print(' ',end = ' ')
    print()   
