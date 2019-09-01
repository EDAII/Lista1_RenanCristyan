# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Algorítmos de busca

from random import randint
from time import time

# Realiza a busca sequencial em um intervalo first <= x < last
def busca_sequencial(vetor, elemento, first, last, return_exec_time=False):
    start = time()

    n = first
    while n < last:
        if vetor[n] == elemento:
            if return_exec_time:
                finish = time()
                exec_time = finish - start
                return n, exec_time
            else:
                return n
        n += 1

    return None

# Realiza a busca sequencial utilizando uma sentinela no final
# (como é muito semelhante à busca sequencial padrão, não implementei
# a medição do tempo de execução)
def busca_sequencial_com_sentinela(vetor, elemento):
    vetor.append(elemento)
    
    i = 0
    while elemento != vetor[i]:
        i += 1
    
    if i < len(vetor)-1:
        return i
    else:
        return None

# Realiza uma busca sequencial apenas em um intervalo específico do vetor,
# sendo bem mais rápido do que a busca sequencial padrão
def busca_sequencial_indexada(vetor, elemento, groups=10, return_exec_time=False):
    tam = len(vetor)
    
    if elemento > tam:
        return None

    group_len = tam // groups
    group_inf = 0
    group_sup = group_len

    n = 0
    while True:
        if group_inf < elemento and elemento < group_sup:
            if return_exec_time:
                j, exec_time = busca_sequencial(vetor, elemento, group_inf, group_sup, return_exec_time)
                return j, exec_time
            else:
                j = busca_sequencial(vetor, elemento, group_inf, group_sup)
                return j

        elif elemento > group_sup:
            group_inf = group_sup
            group_sup += group_len

        n += 1

# Função auxiliar que corta um vetor em um intervalo inf <= x < sup
def cut(vetor, inf, sup):
    n = 0
    cut_vector = []

    while n <= sup:
        if n >= inf:
            cut_vector.append(vetor[n])
        n += 1

    return cut_vector

# As funções abaixo (sobre busca binária) NÃO FUNCIONAM corretamente ou como deveriam.
# Alguns casos funcionam mas outros não.
# Tentei algumas abordagens diferentes mas pelo visto não deram certo.

def busca_binaria(vetor, elemento):
    inf = 0
    sup = len(vetor) - 1

    n = 0
    meio = (sup - inf) // 2

    while n < 10:
        print(inf, sup, meio, vetor[meio])

        if elemento < vetor[meio]:
            meio = (sup - inf) // 2 # Considerando que o vetor tem tamanho par
            sup = meio
        elif elemento > vetor[meio]:
            inf = meio
            meio = (sup + inf) // 2
        else: # Achou
            print(vetor[meio])
            return meio

        n += 1

def busca_binaria_recursiva(vetor, elemento, inf, sup, aux=0):
    if aux > 10:
        return False

    meio = (sup - inf) // 2

    print(vetor, elemento, inf, sup, meio)

    if elemento == vetor[meio]: # Achou
        print(meio)
        return True

    elif elemento < vetor[meio]:
        busca_binaria_recursiva(vetor, elemento, inf=0, sup=meio)

    elif elemento > vetor[meio]:
        busca_binaria_recursiva(vetor, elemento, inf=inf + meio, sup=len(vetor)-1, aux = aux + 1)

def busca_binaria_cut(vetor, elemento):
    inf = 0
    sup = len(vetor) - 1
    meio = (sup - inf) // 2

    vetor_aux = []

    if elemento == vetor[meio]:
        print(meio)

    elif elemento < vetor[meio]:
        vetor_aux = cut(vetor, inf, meio)
        busca_binaria_cut(vetor_aux, elemento)

    elif elemento > vetor[meio]:
        vetor_aux = cut(vetor, meio, sup)
        busca_binaria_cut(vetor_aux, elemento)

# Função auxiliar para comparar os tempos de execução da busca sequencial padrão
# e da busca sequencial indexada com diferentes tamanhos de grupos
# O elemento a ser buscado é sempre o último do vetor
def compara_busca_padrao_com_busca_indexada(vetor):
    indice_bs,  tbs  = busca_sequencial(vetor, len(vetor)-1, first=0, last=len(vetor), return_exec_time=True) # tbs = tempo de busca sequencial
    print('Busca sequencial encontrou o último elemento do vetor em \n{} segundos\n'.format(tbs))

    groups = 10
    while groups < len(vetor):
        indice_bsi, tbsi = busca_sequencial_indexada(vetor, len(vetor)-1, groups=groups, return_exec_time=True) # tbsi = tempo de busca sequencial indexada
        print('Busca sequencial indexada com {} grupos encontrou o último elemento do vetor em \n{} segundos\n'.format(groups, tbsi))
        groups *= 10

# x = [12, 25, 33, 37, 48, 57, 86, 92, 100]
# busca_binaria_cut(x, 100)
# busca_binaria_recursiva(vetor=x, elemento=86, inf=0, sup=len(x)-1)

y = list(range(100000))
# print(busca_sequencial(y, 2, first=0, last=len(y), return_exec_time=True))

# print(busca_sequencial(y, 9999, first=0, last=len(y), return_exec_time=True))
# print(busca_sequencial_indexada(y, 9999, groups=1000, return_exec_time=True))

compara_busca_padrao_com_busca_indexada(y)