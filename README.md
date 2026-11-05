# Estruturas de Dados Simples + Algoritmos de Ordenação

Programa em Python, via terminal, que integra **pilha**, **fila** e **fila circular** com os algoritmos **Bubble Sort**, **Selection Sort** e **Insertion Sort**.

## Execução

```bash
python3 estruturas_ordenacao.py
```

Requer Python 3. Não usa bibliotecas externas.

## Menus

**Menu principal**

1. PILHA
2. FILA
3. FILA CIRCULAR
4. ORDENAR
5. SAIR

**Menu de cada estrutura**

1. Criar estrutura (pede o tamanho)
2. Armazenar valor (`push`)
3. Extrair valor (`pop`)
4. Imprimir conteúdo
5. Voltar ao menu anterior

**Menu ORDENAR**

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Voltar ao menu anterior

## Funcionamento

- As três estruturas usam o mesmo vetor global, `dados`. Criar uma nova estrutura substitui a anterior.
- A ordenação é aplicada à última estrutura criada. Se nenhuma existir, o programa avisa para criar uma antes.
- Apenas os elementos válidos são ordenados:
  - **Pilha:** todo o vetor.
  - **Fila:** de `rpos` até `spos`.
  - **Fila circular:** os `qtd` elementos a partir de `rpos`. Após ordenar, o vetor é normalizado, com `rpos = 0` e `spos = qtd % MAX`.
- A fila simples não reaproveita posições liberadas: `spos == MAX` significa fila cheia. A fila circular resolve essa limitação.
- A fila circular usa um contador `qtd` para diferenciar fila cheia de fila vazia.

## Exemplo

```
=== FILA CIRCULAR ===
Tipo: circular | dados = [5, 20, 40, 50, 60]
rpos = 0 spos = 0 qtd = 5
```

## Estrutura do projeto

```
.
├── estruturas_ordenacao.py
└── README.md
```