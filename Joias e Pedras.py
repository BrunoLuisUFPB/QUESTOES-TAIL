#Descrição:
#Nessa questão, são dadas duas Strings como input: A primeira String representa uma lista de joias e a segunda String são suas pedras. É possível que uma das pedras seja também uma joia, ou seja, se as joias forem "aB" e as pedras forem "aaa", você sabe que existem três pedras que são joias.

#Tarefa:
#Implemente um script em Python para contar o número de pedras que são joias.

#Questão:
[ ]
def jewels_and_stones(jewels, stones):
#a 'função jewels_and_stones' recebe 'jewels' e 'stones'. A variável 'count' com inicialização em 0 serve para armazenar a quantidade de jewels enquanto a função é percorrida.
# se a pedra for jewels ela começará a contar e incrementar mais 1.
# a contagem irá "saltar" para fora se não houver mais jewels entre stones.
    
    count = 0
    
    for stone in stones:

        if stone in jewels:
            count += 1

    return count

jewels = "ac"
stones = "abc"

print(jewels_and_stones(jewels, stones))
