#Descrição:
#Para lidar com valores textuais, são utilizadas variáveis de tipo String, podendo ser tratados como Listas (outra Estrutura de Dados) em Python. Dessa forma, é possível identificar caracteres de um String a partir de seu índice, o que ajuda bastante em analisar o comportamento de uma certa palavra.

#Tarefa:
#Faça um programa que printe todos os números de 1 a 100, mas printe "TAIL" no lugar dos números divisíveis por 3, printe "UFPB" no lugar dos números divisíveis por 5, e printe "TAILUFPB" no lugar dos números divisíveis por 3 e por 5.

#Código:
[ ]
# usei a estrutura repetitiva 'for' para imprimir a sequência de 1 a 101.
# usei a estrutura condicional 'if else' para substituição dos números divisíveis por 3 e 5.

for i in range(1, 101):
     if i % 3 == 0 and i % 5 == 0:
         print("TAILUFPB")
     elif i % 3 == 0:
         print("TAIL")
     elif i % 5 == 0:
         print("UFPB")
     else:
         print(i)
