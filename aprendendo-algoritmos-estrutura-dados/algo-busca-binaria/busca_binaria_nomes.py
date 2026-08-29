# IMPORTAÇÕES 

import time
from math import trunc
from dicionario_nomes import dicionarioGenerico # Biblioteca local com o dicionário de nomes genéricos

# LÓGICA 

def buscaBinaria(iniLista, fimLista): # -> int

    '''
    Algoritmo de busca binária para dicionários que possuem chaves (como índices numéricos - int) e valores (como nomes - strings).

    iniLista -> Parâmetro de entrada de identificação do início do intervalo onde será buscado o determinado valor.

    fimLista -> Parâmetro de entrada de identificação do fim do intervalo onde será buscado o determinado valor.

    '''

    # Inicialização de contagem de tempo de funcionamento da função.
    inicioFuncao = time.time()

    # Preenchimento da lista 'intervaloDeIndices' com o intervalo gerado a partir dos parâmetros de entrada da função.
    intervaloDeIndices = []

    for itensLista in range(iniLista, (fimLista + 1)):
        intervaloDeIndices.append(itensLista)

    # Inicialização de variáveis da função.
    indicePrincipal = 0 
    indiceMax = max(intervaloDeIndices)
    indiceMin = min(intervaloDeIndices)
    sinal = 0
    contadorDeLoops = 0

    # Iteração da busca binária de nomes - Terminará apenas quando o nome a ser buscado dentro do dicionário for encontrado, caso ocorra uma exceção será retornado um erro.
    while True:
        try:
            # Nome a ser buscado dentro do dicionário.
            nomeASerBuscado = input("Digite um nome: ")
            # Índice do nome a ser buscado dentro do dicionário (caso o nome inserido não exista dentro do dicionário, a variável receberá o valor 'None').
            indiceASerBuscado = next((chave for chave, valor in dicionarioGenerico.items() if valor == nomeASerBuscado), None)

            # Se o índice do nome a ser buscado não existir, não terá como encontrá-lo dentro do dicionário. Para isso uma exceção é criada.
            if indiceASerBuscado == None:
                raise Exception("O valor a ser buscado não está presente no dicionário!")

            # Enquanto o indice de busca ('indicePrincipal') não for o mesmo que o indice a ser buscado ('indiceASerBuscado'), ocorrerá o loop para encontrar o indice desejado.
            # (OBS: É interessante observar que se o nome a ser buscado possuir o indice 0, ou seja, se o mesmmo for o primeiro nome da lista, não ocorrerá um loop, pois 'indicePrincipal' é inicializado com o valor 0).
            while indicePrincipal != indiceASerBuscado:

                contadorDeLoops += 1 # Será usado para verificar, ao final, a quantidade loops que foram necessários para encontrar o índice do nome.

                # Inicialização da lista temporária que varia conforme o afunilamento do intervalo.
                listaTmp = []

                for itensListaTmp in range(indiceMin, (indiceMax + 1)):
                    listaTmp.append(itensListaTmp)
            
                # Bloco de alteração do indice de busca ('indicePrincipal') conforme afunilamento dos intervalos da lista temporária ('listaTmp').
                if indiceMin != 1 and sinal == 0:
                    indicePrincipal = indicePrincipal + int(((max(listaTmp) + 1) - min(listaTmp)) / 2)
                elif indiceMin != 1 and sinal == 1:
                    indicePrincipal = indicePrincipal - int(((max(listaTmp) + 1) - min(listaTmp)) / 2)
                else:
                    indicePrincipal = int(max(listaTmp) / 2)

                # Bloco de verificação de proximidade do indice de busca ('indicePrincipal') com o indice a ser buscado ('indiceASerBuscado').
                if indicePrincipal > indiceASerBuscado:

                    indiceMax = indicePrincipal
                    sinal = 1
                    continue

                if indicePrincipal < indiceASerBuscado:

                    indiceMin = indicePrincipal
                    sinal = 0
                    continue

            # Finalização da contagem de tempo da função.
            fimFuncao = time.time()
            tempoExec = str(trunc(fimFuncao - inicioFuncao)) + ' segundos'

            # Dados de retorno -> Índice correspondente ao nome buscado no dicionário de nomes genéricos ('dicionarioGenerico'); Quantidade de loops ocorridos para encontrar o nome; Tempo de execução do programa.
            dadosIndice = {
                    "indice" : indicePrincipal,
                    "loops" : contadorDeLoops,
                    "tempo em execução" : tempoExec
            }


            return dadosIndice
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
# Teste unitário da entrada, chamada e saída da função de busca binária de nomes.
if __name__ == "__main__":

    inicioIntervalo = min(dicionarioGenerico)
    fimIntervalo = max(dicionarioGenerico)
    print(buscaBinaria(inicioIntervalo, fimIntervalo))










