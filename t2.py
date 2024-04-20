import sys

def recursao_simples(matriz, x=0, y=0):
    xlen = len(matriz)
    ylen = len(matriz[0])

    if x >= xlen or y >= ylen or matriz[x][y] == 1:
        return 0

    if x == xlen - 1 and y == ylen - 1:
        return 1

    return recursao_simples(matriz, x, y + 1) + recursao_simples(matriz, x + 1, y + 1)

def recursao_memoizacao(matriz, x=0, y=0, memoria={}):
    xlen = len(matriz)
    ylen = len(matriz[0])

    if (x, y) in memoria:
        return memoria[(x, y)]

    if x >= xlen or y >= ylen or matriz[x][y] == 1:
        return 0

    if x == xlen - 1 and y == ylen - 1:
        return 1

    memoria[(x, y)] = recursao_memoizacao(matriz, x, y + 1, memoria) + recursao_memoizacao(matriz, x + 1, y + 1, memoria)
    return memoria[(x, y)]

def iterativo(matriz):
    xlen= len(matriz)
    ylen= len(matriz[0])
    imatriz = []

    for _ in range(xlen):
        linha = []
        for _ in range(ylen):
            linha.append(0)
        imatriz.append(linha)

    imatriz[0][0] = 1

    for x in range(xlen):
        for y in range(ylen):
            if matriz[x][y] != 1:
                if y < ylen -1:
                    imatriz[x][y + 1] += imatriz[x][y]

                if x < xlen -1 and y < ylen -1:
                    imatriz[x + 1][y + 1] += imatriz[x][y]
            else:
                continue

    return imatriz[xlen - 1][ylen - 1]

def leitura_arquivo(nomeArq):
    with open(nomeArq, 'r') as arquivo:
        linhas, colunas = map(int, arquivo.readline().split())
        matriz = []

        for _ in range(linhas):
            linha = arquivo.readline().split()
            if len(linha) != colunas:
                raise ValueError("Arquivo nao segue o padrao estabelecido.")
            matriz.append(list(map(int, linha)))

    return matriz


if len(sys.argv) == 2:
    nomeArq = sys.argv[1]
    matriz = leitura_arquivo(nomeArq)
    print("Tambem ha possibilidade de executar individualmente cada modo: rs = recursao simples, rm = recursao com memoizacao, i = iterativo, rmi = recursao com memoizacao e iterativo. \nPara isso: python t2.py <nome_arquivo> <modo>")
    print("\nResultado com Recursao simples:       ", recursao_simples(matriz))
    print("Resultado com recursao com memoizacao:", recursao_memoizacao(matriz))
    print("Resultado com metodo iterativo:       ", iterativo(matriz))

if len(sys.argv) == 3:
    nomeArq = sys.argv[1]
    modo = sys.argv[2]
    matriz = leitura_arquivo(nomeArq)
    
    if modo == 'rs':
        print("Resultado com Recursao simples:", recursao_simples(matriz))

    if modo == 'rm':
        print("Resultado com recursao com memoizacao:", recursao_memoizacao(matriz))

    if modo == 'i':
        print("Resultado com metodo iterativo:", iterativo(matriz))

    if modo == 'rmi':
        print("Resultado com recursao com memoizacao:", recursao_memoizacao(matriz))
        print("Resultado com metodo iterativo:       ", iterativo(matriz))

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Para utilizar o programa, execute: python t2.py <nome_arquivo>")
    print("\nTambem ha possibilidade de executar por modo: rs = recursao simples, rm = recursao com memoizacao, i = iterativo, rmi = recursao com memoizacao e iterativo. \nPara isso: python t2.py <nome_arquivo> <modo>")
    sys.exit(1)