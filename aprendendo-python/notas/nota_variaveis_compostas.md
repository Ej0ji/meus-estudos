# Variáveis Compostas em Python

As variáveis compostas (coleções) armazenam múltiplos valores em uma única estrutura. Abaixo estão suas características, comportamentos essenciais e cuidados técnicos.

---

## 1. Os Quatro Tipos Principais

* **Listas (`list`)**: Sequências **ordenadas e mutáveis**. Permitem duplicatas. Uso com colchetes `[]`. Ideal para coleções de dados que mudam de tamanho ou ordem.
* **Tuplas (`tuple`)**: Sequências **ordenadas e imutáveis**. Permitem duplicatas. Uso com parênteses `()`. Garantem segurança de dados protegidos e maior velocidade.
* **Dicionários (`dict`)**: Coleções **mutáveis de pares chave-valor**. Chaves devem ser únicas. Uso com chaves `{'chave': valor}`. Ideal para estruturar dados com etiquetas/identificadores.
* **Conjuntos (`set`)**: Coleções **não ordenadas e mutáveis que não admitem duplicatas**. Uso com chaves `{v1, v2}`. Ideal para eliminar repetições e operações matemáticas de conjuntos.

### Tabela Comparativa

| Tipo | Sintaxe | Ordenado? | Mutável? | Permite Duplicados? | Busca (`in`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Lista** | `[a, b]` | Sim | Sim | Sim | Lenta (Linear) |
| **Tupla** | `(a, b)` | Sim | Não | Sim | Lenta (Linear) |
| **Dicionário** | `{'k': v}` | Sim* | Sim | Não (chaves) | Instantânea (Hash) |
| **Conjunto** | `{a, b}` | Não | Sim | Não | Instantânea (Hash) |

*\*Nota: Dicionários preservam a ordem de inserção a partir do Python 3.7.*

---

## 2. Detalhes Técnicos e Cuidados Cruciais

### Atribuição vs. Cópia Real
Atribuir uma variável mutável (lista, dicionário ou conjunto) a outra **não copia os dados**, apenas cria uma referência ao mesmo objeto na memória. Alterar uma modificará a outra.
* **Incorreto:** `lista_b = lista_a` (compartilham a mesma memória).
* **Correto:** `lista_b = lista_a.copy()` (cria um novo objeto). Para estruturas aninhadas, use `copy.deepcopy()`.

### Restrição de Chaves e Elementos
Dicionários (chaves) e Conjuntos (elementos) exigem objetos **imutáveis (hashable)**. 
* **Permitido:** Strings, números, tuplas.
* **Proibido:** Listas, dicionários, conjuntos.

### Sintaxe de Tupla Unitária
Para criar uma tupla com apenas um elemento, a vírgula final é obrigatória.
* `(5)` é interpretado como um número inteiro isolado.
* `(5,)` é interpretado corretamente como uma tupla.

### Recursos Avançados de Sequências
Listas e tuplas suportam indexação negativa e fatiamento (`slicing`):
* `colecao[-1]` acessa o último elemento.
* `colecao[::-1]` inverte a sequência de forma otimizada.