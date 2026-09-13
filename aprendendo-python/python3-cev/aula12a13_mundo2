# Aula 12 a 13 do Curso Python 3 - Mundo 2

## Sumário

- [Aula 12 - Condições (Parte 2) + Exercícios 36 a 45](#aula-12---condições-parte-2--exercícios-36-a-45)
    - [Introdução ao Mundo 2 do Curso de Python 3](#introdução-ao-mundo-2-do-curso-de-python-3)
    - [O Conceito de Aninhamento](#o-conceito-de-aninhamento)
    - [A Anatomia do `elif` em Python](#a-anatomia-do-elif-em-python)
    - [Regras da Estrutura `if...elif...else`](#regras-da-estrutura-ifelifelse)
    - [Demonstração Prática](#demonstração-prática)
    - [Relação com os Exercícios 36 a 45](#relação-com-os-exercícios-36-a-45)
- [Aula 13 - Estruturas de Repetição (Parte 1) + Exercícios 46 a 56 ](#aula-13---estruturas-de-repetição-parte-1--exercícios-46-a-56)

---
## Aula 12 - Condições (Parte 2) + Exercícios 36 a 45

### Introdução ao Mundo 2 do Curso de Python 3

Aqui damos início a segunda parte deste curso, o **Mundo 2**. Neste novo módulo, exploraremos as estruturas de controle que permitem criar programas mais complexos, dinâmicos e inteligentes.

Iniciando com as estruturas **condicionais aninhadas.** Enquanto no **Mundo 1**, estudamos as **estruturas condicionais simples e compostas** (`if...else`). Nelas, o fluxo do algoritmo possuía, no máximo, duas trajetórias possíveis: ou uma condição era verdadeira, ou ela era falsa.
Contudo, na vida real e no desenvolvimento de software, os problemas frequentemente apresentam três, quatro ou múltiplas possibilidades de escolha. Para resolver cenários com múltiplos caminhos, aprenderemos a utilizar as **Condições Aninhadas**.

---
### O Conceito de Aninhamento

Aninhar significa colocar uma estrutura dentro de outra. O termo vem da ideia de criar ninhos ou, como em uma metáfora visual, das bonecas russas (matrioscas), onde uma estrutura menor se encaixa perfeitamente dentro de outra maior.
Em lógica de programação, condições aninhadas ocorrem quando inserimos novas verificações condicionais dentro dos blocos de uma condição já existente.

#### Analogia do Carro e da Estrada

Seguindo a mesma analogia do fluxo de trânsito da aula de estruturas condicionais (parte 1), imagine um carro em uma estrada:

- **Estrutura Simples/Composta**: O carro encontra um cruzamento com apenas dois caminhos: virar à esquerda ou à direita.

- **Estrutura Aninhada**: O carro avança e encontra uma bifurcação com três caminhos: esquerda, direita ou seguir em frente.

Se o carro não virar à esquerda, ele não tem apenas uma opção restante; ele precisa testar uma segunda condição para decidir se vira à direita ou se continua em frente.

---
### A Anatomia do `elif` em Python

Para tratar múltiplos caminhos sem criar códigos poluídos ou excessivamente deslocados para a direita, já que é possível estruturar condicionais simples e/ou compostas uma dentro das outra para criar condicionais aninhadas

```Python
if 1 > 0:
    if 3 > 1:
        print('Aninhou!')
    else:
        print('Também aninhou!')
```

o Python introduz a palavra reservada `elif`.

A palavra `elif` é a contração de `else` + `if` ("se não, se")

Aqui vai um comparativo de estruturas:

| Tipo de Condição | Estrutura Lógica | Descrição |
|---|---|---|
| Simples | `if` | Executa um bloco apenas se a condição for verdadeira. |
| Composta| `if...else` | Executa um bloco se for verdadeiro e outro se for falso. |
| Aninhada | `if...elif...else `| Avalia múltiplas condições em sequência até encontrar uma verdadeira. |

---
### Regras da Estrutura `if...elif...else`

Ao construir uma estrutura condicional aninhada em Python, observe as seguintes regras fundamentais:

1. **Início obrigatório**: Toda estrutura condicional deve começar obrigatoriamente com um comando `if`. Nunca inicie um bloco com `elif` ou `else`;

2. **Uso de elif**: É possível utilizar quantos `elif` forem necessários entre o `if` inicial e o `else` final;

3. **Uso de else**: O bloco `else` é opcional. Quando utilizado, pode aparecer no máximo uma vez, sempre ao final da estrutura;

4. **Sintaxe dos dois pontos (:)**: Toda linha contendo `if`, `elif` ou `else` exige o caractere : ao final;

5. **Indentação**: O código dentro de cada bloco deve estar devidamente recuado (4 espaços).

```Python
# Estrutura Geral das Condições Aninhadas

if condição_1:
    # Executa se a condição_1 for verdadeira
elif condição_2:
    # Executa se a condição_1 for falsa E a condição_2 for verdadeira
elif condição_3:
    # Executa se as condições 1 e 2 forem falsas E a condição_3 for verdadeira
else:
    # Executa se TODAS as condições anteriores forem falsas
```

---
### Demonstração Prática
Observe a implementação prática feita durante a aula. O programa analisa o nome digitado pelo usuário e emite saídas customizadas dependendo do grupo em que o nome se enquadra.

```Python
# Leitura do nome do usuário
nome = str(input('Qual é o seu nome? ')).strip()

# Condição Aninhada em Ação
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {nome}!')
```

#### Análise do Fluxo de Execução:

1. Se o usuário digitar "Gustavo", o programa entra no bloco do `if`, exibe "Que nome bonito!" e ignora todos os `elif` e o `else`;
2. Se digitar "Maria", a primeira condição é falsa. O Python testa o primeiro `elif`, identifica a igualdade e exibe "Seu nome é bem popular no Brasil.";
3. Se digitar "Ana", o operador `in` identifica que o nome está contido na *string* 'Ana Cláudia Jéssica Juliana', executando a mensagem referente;
4. Se digitar qualquer nome que não atenda às condições anteriores (ex: "Hélio"), o fluxo é direcionado para o bloco `else`.

---
### Relação com os Exercícios 36 a 45

Para aprofundamento prático, consulte:

- <a href="exe036.py">Exercício 36</a>
- <a href="exe037.py">Exercício 37</a>
- <a href="exe038.py">Exercício 38</a>
- <a href="exe039.py">Exercício 39</a>
- <a href="exe040.py">Exercício 40</a>
- <a href="exe041.py">Exercício 41</a>
- <a href="exe042.py">Exercício 42</a>
- <a href="exe043.py">Exercício 43</a>
- <a href="exe044.py">Exercício 44</a>
- <a href="exe045.py">Exercício 45</a>

Os exercícios acima mostram na prática como criar estruturas condicionais em casos específicos e até mesmo exemplos reais, onde são realizadas lógicas de comparação de quantidades e valores para determinar novas ações.

---
## Aula 13 - Estruturas de Repetição (Parte 1) + Exercícios 46 a 56

### Introdução a Estruturas de Repetição

Até o momento nos estudos de programação, o fluxo baseava-se em seguir condições para realizar determinadas ações. A partir de agora, o foco passa a ser a repetição de ações. As estruturas de controle de repetição, também conhecidas como laços ou iterações, existem para evitar a escrita de códigos exaustivos e idênticos.

Imagine um personagem em um jogo que precisa dar dezenas de passos para alcançar uma maçã. Em vez de escrever o comando "dar passo" repetidas vezes, cria-se um laço que instrui o computador a repetir essa ação automaticamente. Esta aula explora a estrutura de repetição mais simples e essencial da linguagem: o laço com variável de controle, conhecido no Python como `for`.

### O Comando `for` e a Sintaxe Básica

O comando `for` atua estabelecendo um limite exato de repetições. Para o Python compreender onde a contagem se inicia e onde ela termina, utiliza-se a função `range()` (que significa "intervalo"), sempre associada à indentação do código.

    Regra de Ouro: Tudo o que está indentado abaixo da linha do `for` pertence ao laço e se repetirá. O que estiver alinhado à margem esquerda, fora do bloco, executará apenas após o término de todas as repetições. Lembre-se, também, de sempre finalizar a linha de declaração do `for` com os dois pontos (:).

#### **Exemplo Prático 1**: Contagem Simples

Observe o código a seguir. Ele repetirá a impressão da mensagem na tela baseando-se no intervalo estipulado.

```Python
# O laço executará de 1 até 5. O número 6 é sempre ignorado pelo Python.
for contador in range(1, 6):
    print("Passo número {}".format(contador))
    
print("Fim do trajeto!")
```

### Explorando a Função `range()`

A função `range(início, fim, passo)` é altamente flexível e recebe até três parâmetros simultâneos. O Python permite realizar contagens progressivas, contagens regressivas ou, até mesmo, pular números em intervalos maiores.

Considere a seguinte particularidade: o Python ignora o último número do intervalo. Portanto, se o objetivo for uma contagem que inclua o número 10, determine o final do *range* como 11.

#### **Exemplo Prático 2**: Contagem Regressiva e Saltos

Para executar uma contagem para trás, defina o início maior que o fim e utilize o passo como -1. Para saltar números, como pular de dois em dois, altere o passo para 2.

```Python
# Contagem regressiva de 6 até 1
for c in range(6, 0, -1):
    print("Contagem regressiva: {}".format(c))

print("Decolar!")

# Contagem de 0 a 10, pulando de 2 em 2 (mostra apenas os pares)
for c in range(0, 11, 2):
    print("Número par detectado: {}".format(c))
```

### Integração do `for` com Condicionais (`if`)

A lógica de programação permite aninhar comandos, isto é, inserir uma estrutura dentro de outra. Coloque tranquilamente estruturas condicionais (como o `if`) dentro do laço `for` se o problema em questão exigir verificações a cada repetição.

Caso o personagem do jogo precise caminhar, pular buracos e pegar moedas apenas se elas existirem naquele espaço, insere-se um bloco `if` dentro da indentação do `for`. Deste modo, o programa avaliará a condição a cada passo dado.

### Interação com o Usuário e Somatórios (Acumuladores)

O laço `for` demonstra seu maior potencial quando processa dados inseridos dinamicamente pelo usuário. Lê-se valores diversas vezes posicionando o comando `input()` internamente ao laço e, aplicando lógicas matemáticas, soma-se todos os valores em uma variável acumuladora.

#### **Exemplo Prático 3**: Lendo e Acumulando Valores

Execute mentalmente o código abaixo e compreenda como o somatório se atualiza e cresce a cada repetição, guardando o resultado total no final do processo.

```Python
soma = 0
# Repete 4 vezes, solicitando um novo número a cada volta
for c in range(0, 4):
    numero = int(input("Digite o {}º valor para a soma: ".format(c + 1)))
    soma = soma + numero  # A variável 'soma' acumula o valor digitado atual

print("O somatório de todos os valores fornecidos é igual a {}".format(soma))
```

### Relação com os Exercícios 46 a 56

Para aprofundamento prático, consulte:

- <a href="exe046.py">Exercício 46</a>
- <a href="exe047.py">Exercício 47</a>
- <a href="exe048.py">Exercício 48</a>
- <a href="exe049.py">Exercício 49</a>
- <a href="exe050.py">Exercício 50</a>
- <a href="exe051.py">Exercício 51</a>
- <a href="exe052.py">Exercício 52</a>
- <a href="exe053.py">Exercício 53</a>
- <a href="exe054.py">Exercício 54</a>
- <a href="exe055.py">Exercício 55</a>
- <a href="exe056.py">Exercício 56</a>

Os exercícios desta aula mostram a importância dessa estrutura, pois ela integra as ferramentas mais relevantes para a fluidez e otimização do seu código.

Da indentação: Um `print()` alinhado de forma equivocada mudará o comportamento de toda a aplicação, repetindo na tela textos que deveriam ser impressos uma única vez.

E atenção aos sinais vitais do Python: Esquecer os dois pontos (:) no final do comando for consiste no erro mais comum para quem está começando.

---
Ir para: <a href="aula14a15_mundo2">Mundo 2 - Aula 14 a 15</a>