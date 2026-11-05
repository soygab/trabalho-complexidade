dados = []      # vetor único usado por pilha, fila e fila circular
tipo = None     # "pilha", "fila" ou "circular"
MAX = 0
topo = -1       # pilha
spos = 0        # fila / fila circular
rpos = 0
qtd = 0         # fila circular


def ler_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print("\nValor inválido!")
        return None


# Criação
def criar(t):
    global dados, tipo, MAX, topo, spos, rpos, qtd
    n = ler_int("Tamanho da estrutura: ")
    if n is None or n <= 0:
        print("\nTamanho inválido!")
        return
    MAX = n
    tipo = t
    topo, spos, rpos, qtd = -1, 0, 0, 0
    dados = [None] * MAX if t == "circular" else []
    print("\nEstrutura criada!")


# Armazenar
def push(valor):
    global topo, spos, qtd
    if tipo == "pilha":
        if topo == MAX - 1:
            print("\nPilha Cheia!!!")
            return
        dados.append(valor)
        topo += 1
    elif tipo == "fila":
        if spos == MAX:
            print("\nFila Cheia!!!")
            return
        dados.append(valor)
        spos += 1
    else:
        if qtd == MAX:
            print("\nFila Circular Cheia!!!")
            return
        dados[spos] = valor
        spos = (spos + 1) % MAX
        qtd += 1


# Extrair
def pop():
    global topo, rpos, qtd
    if tipo == "pilha":
        if topo < 0:
            print("\nPilha Vazia!!!")
            return None
        valor = dados.pop()
        topo -= 1
        return valor
    if tipo == "fila":
        if rpos == spos:
            print("\nFila Vazia!!!")
            return None
        valor = dados[rpos]
        dados[rpos] = None
        rpos += 1
        return valor
    if qtd == 0:
        print("\nFila Circular Vazia!!!")
        return None
    valor = dados[rpos]
    dados[rpos] = None
    rpos = (rpos + 1) % MAX
    qtd -= 1
    return valor


# Imprimir
def show():
    print("\nTipo:", tipo, "| dados =", dados)
    if tipo == "fila":
        print("rpos =", rpos, "spos =", spos, "| elementos:", dados[rpos:spos])
    elif tipo == "circular":
        print("rpos =", rpos, "spos =", spos, "qtd =", qtd)


# Acesso aos elementos válidos (ordem lógica)
def obter_itens():
    if tipo == "pilha":
        return dados[:]
    if tipo == "fila":
        return dados[rpos:spos]
    return [dados[(rpos + i) % MAX] for i in range(qtd)]


def gravar_itens(v):
    global rpos, spos
    if tipo == "pilha":
        dados[:] = v
    elif tipo == "fila":
        dados[rpos:spos] = v
    else:
        # normaliza: elementos ordenados a partir do índice 0
        for i in range(MAX):
            dados[i] = v[i] if i < qtd else None
        rpos = 0
        spos = qtd % MAX


# Ordenação
def bubble(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]


def selection(v):
    n = len(v)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if v[j] < v[m]:
                m = j
        v[i], v[m] = v[m], v[i]


def insertion(v):
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave


def ordenar(algoritmo):
    v = obter_itens()
    algoritmo(v)
    gravar_itens(v)
    print("\nEstrutura ordenada!")
    show()


# Menus
def menu_estrutura(t):
    while True:
        print(f"\n=== {t.upper()} ===")
        print("1 - Criar estrutura")
        print("2 - Armazenar Valor")
        print("3 - Extrair Valor")
        print("4 - Imprimir Conteúdo")
        print("5 - Voltar ao Menu Anterior")
        op = ler_int("Opção: ")
        if op == 5:
            return
        if op == 1:
            criar(t)
        elif op in (2, 3, 4):
            if tipo != t:
                print(f"\nCrie primeiro a estrutura ({t}) na opção 1!")
            elif op == 2:
                v = ler_int("Valor: ")
                if v is not None:
                    push(v)
            elif op == 3:
                v = pop()
                if v is not None:
                    print("\nValor extraído:", v)
            else:
                show()
        else:
            print("\nOpção inválida!")


def menu_ordenar():
    while True:
        print("\n=== ORDENAR ===")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao Menu Anterior")
        op = ler_int("Opção: ")
        if op == 4:
            return
        if op not in (1, 2, 3):
            print("\nOpção inválida!")
            continue
        if tipo is None:
            print("\nNenhuma estrutura criada. Escolha primeiro PILHA, FILA ou FILA CIRCULAR no menu principal.")
            return
        ordenar({1: bubble, 2: selection, 3: insertion}[op])


def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Pilha")
        print("2 - Fila")
        print("3 - Fila Circular")
        print("4 - Ordenar")
        print("5 - Sair")
        op = ler_int("Opção: ")
        if op == 1:
            menu_estrutura("pilha")
        elif op == 2:
            menu_estrutura("fila")
        elif op == 3:
            menu_estrutura("circular")
        elif op == 4:
            menu_ordenar()
        elif op == 5:
            break
        else:
            print("\nOpção inválida!")


main()