# Aula 14 a 15 do Curso Python 3 - Mundo 2

## Sumário

- [Aula 14 - Estruturas de Repetição (Parte 2) + Exercícios 57 a 65](#aula-14---estruturas-de-repetição-parte-2--exercícios-57-a-65)
  - [Introdução ao Laço `while`](#introdução-ao-laço-while)
  - [Teste Lógico e Variável de Controle](#teste-lógico-e-variável-de-controle)
  - [Sintaxe e Indentação](#sintaxe-e-indentação)
  - [Aplicações Práticas do `while`](#aplicações-práticas-do-while)
    - [Repetições com Limite Conhecido](#repetições-com-limite-conhecido)
    - [Condição de Parada (*Flag*)](#condição-de-parada-flag)
    - [Repetição Controlada pelo Usuário](#repetição-controlada-pelo-usuário)
    - [Combinando `while` com Condicionais](#combinando-while-com-condicionais)
  - [Comparação entre `for` e `while`](#comparação-entre-for-e-while)
  - [Relação com os Exercícios 57 a 65](#relação-com-os-exercícios-57-a-65)

---
## Aula 14 - Estruturas de Repetição (Parte 2) + Exercícios 57 a 65

---
### Introdução ao Laço `while`

Na aula anterior, estudamos o laço `for`, indicado principalmente para situações em que o número de repetições ou o intervalo já é conhecido. Nesta aula, continuaremos o estudo das estruturas de repetição com o `while`, que executa um bloco de código enquanto uma condição lógica for verdadeira.

O `while` é especialmente útil quando não sabemos antecipadamente quantas vezes será necessário repetir uma ação. O laço pode, por exemplo, continuar até que o usuário informe um valor específico ou decida encerrar a execução.

---
### Teste Lógico e Variável de Controle

As estruturas `for` e `while` controlam a repetição de maneiras diferentes:

- **`for` (variável de controle):** percorre uma sequência ou intervalo, como `range(1, 10)`.
- **`while` (teste lógico):** verifica uma condição antes de cada repetição. O bloco é executado enquanto o resultado for verdadeiro.

Como o `while` depende de uma condição, é importante garantir que alguma ação dentro do laço possa eventualmente torná-la falsa. Caso contrário, o programa continuará repetindo indefinidamente.

---
### Sintaxe e Indentação

A palavra reservada `while` é seguida por uma condição lógica e dois-pontos (`:`). As instruções indentadas abaixo dela pertencem ao laço; as instruções alinhadas com `while` são executadas depois que a condição se torna falsa.

```Python
while not chegou_na_maca:
    dar_passo()

pegar_maca()
```

Nesse exemplo, `dar_passo()` é executado enquanto `chegou_na_maca` for falso. Quando a condição mudar, o programa sai do laço e executa `pegar_maca()`.

---
### Aplicações Práticas do `while`

---
#### Repetições com Limite Conhecido

Embora o `for` seja normalmente mais direto para intervalos conhecidos, também é possível fazer uma contagem com `while`. Nesse caso, inicializamos a variável de controle antes do laço e atualizamos seu valor dentro dele:

```Python
# Contagem de 1 até 9
c = 1
while c < 10:
    print('Contador atual: {}'.format(c))
    c += 1

print('Fim da contagem.')
```

O incremento `c += 1` é essencial: sem ele, `c` permaneceria igual a `1` e a condição `c < 10` continuaria verdadeira.

---
#### Condição de Parada (*Flag*)

Um *flag* é um valor usado para indicar que a repetição deve terminar. No exemplo abaixo, o programa continua lendo números até que o usuário digite `0`:

```Python
n = 1
while n != 0:
    n = int(input('Digite um valor (0 para parar): '))

print('Programa encerrado.')
```

A variável `n` começa com um valor diferente de `0` para que o laço seja iniciado e a primeira entrada seja solicitada. Quando o usuário digita `0`, a condição se torna falsa e o laço termina.

---
#### Repetição Controlada pelo Usuário

Também podemos perguntar ao usuário, ao final de cada repetição, se ele deseja continuar:

```Python
resposta = 'S'
while resposta == 'S':
    valor = int(input('Digite um valor: '))
    resposta = input('Deseja continuar? [S/N] ').strip().upper()

print('Execução finalizada.')
```

O método `.strip()` remove espaços antes e depois da resposta, e `.upper()` converte as letras para maiúsculas. Assim, tanto `s` quanto `S` permitem continuar.

---
#### Combinando `while` com Condicionais

Podemos usar estruturas condicionais dentro de um laço para decidir como processar cada valor. Neste exemplo, contamos números pares e ímpares até que `0` seja digitado. O valor de parada não entra na contagem:

```Python
n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor (0 para parar): '))

    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
```

O primeiro `if` verifica se o número é diferente do *flag*. Somente então o programa testa se ele é par ou ímpar.

---
### Comparação entre `for` e `while`

| Critério | `for` | `while` |
|---|---|---|
| Controle da repetição | Percorre uma sequência ou intervalo | Repete enquanto uma condição for verdadeira |
| Uso comum | Quantidade ou intervalo de repetições conhecido | Repetições que dependem de uma condição ou interação |
| Atualização do controle | Geralmente realizada pelo próprio laço | Deve ser considerada na lógica do programa |
| Atenção principal | Definir corretamente a sequência | Garantir uma condição de parada |

As duas estruturas podem resolver alguns dos mesmos problemas. A escolha depende de qual delas deixa mais clara a lógica da tarefa.

---
### Relação com os Exercícios 57 a 65

Os exercícios a seguir colocam em prática o uso do `while` em situações variadas, como validação de dados, repetição controlada pelo usuário, contadores, acumuladores e condições de parada. Ao resolvê-los, observe como a condição do laço determina quando cada programa deve continuar ou encerrar.

- <a href="exe057.py">Exercício 57 - Validação de Dados</a>
- <a href="exe058.py">Exercício 58 - Jogo da Adivinhação v2.0</a>
- <a href="exe059.py">Exercício 59 - Menu de Opções</a>
- <a href="exe060.py">Exercício 60 - Cálculo do Fatorial</a>
- <a href="exe061.py">Exercício 61 - Progressão Aritmética v2.0</a>
- <a href="exe062.py">Exercício 62 - Super Progressão Aritmética v3.0</a>
- <a href="exe063.py">Exercício 63 - Sequência de Fibonacci v1.0</a>
- <a href="exe064.py">Exercício 64 - Tratando Vários Valores v1.0</a>
- <a href="exe065.py">Exercício 65 - Maior e Menor Valores</a>

---
Ir para: <a href="aula12a13_mundo2">Mundo 2 - Aula 12 a 13</a>