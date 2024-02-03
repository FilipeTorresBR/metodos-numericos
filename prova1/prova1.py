import sys
import numpy as np

arquivoResistencias = "resistencias.in"
arquivoTensoes = "tensoes.in"
arquivoSaida = "saida.out"
resistencias = []
tensoes = []
numeroCorrentes = 3
numeroLinhas = 3
numeroColunas = numeroCorrentes*numeroLinhas+1

def monta_matriz(resistencias, tensoes, numeroCorrentes, numeroLinhas):
    
    matriz = np.zeros((numeroLinhas*numeroCorrentes, numeroColunas), dtype=np.float64)
    linha = 0
    resistor = 0
    fimLinha = numeroCorrentes-1
    trocaLinha = True
    for linha in range(numeroLinhas*numeroCorrentes):
        for corrente in range(numeroCorrentes*numeroColunas+1):
            if trocaLinha == True:
                matriz[linha][linha] = resistencias[resistor]+resistencias[resistor+1]
                matriz[linha][linha+1] = -resistencias[resistor+1]
                matriz[linha][numeroColunas-1] = tensoes[0]-tensoes[1]
                resistor+=1
                trocaLinha = False
                break
            elif corrente+1 == linha:
                if linha == fimLinha:
                    matriz[linha][corrente] = -resistencias[resistor]
                    matriz[linha][corrente+1] = resistencias[resistor]+resistencias[resistor+1]
                    matriz[linha][numeroColunas-1] = tensoes[resistor]-tensoes[resistor+1]
                    fimLinha+=numeroCorrentes
                    resistor+=2
                    trocaLinha = True
                    break
                else:
                    matriz[linha][corrente] = -resistencias[resistor]
                    matriz[linha][corrente+1] = resistencias[resistor] + resistencias[resistor+1]
                    matriz[linha][corrente+2] = -resistencias[resistor+1]
                    matriz[linha][numeroColunas-1] = tensoes[resistor] - tensoes[resistor+1]
                    resistor+=1
                    break
    print(matriz)
    return matriz

if len(sys.argv)>1:
    arquivoResistencias = sys.argv[1]
if len(sys.argv)>2:
    arquivoTensoes = sys.argv[2]
try:
    resistencias = np.loadtxt(arquivoResistencias)
    tensoes = np.loadtxt(arquivoTensoes)
except:
    print("Erro ao ler o arquivo!")
    sys.exit()
matrizPronta = monta_matriz(resistencias, tensoes, numeroCorrentes, numeroLinhas)
np.savetxt(arquivoSaida, matrizPronta, fmt='%1.1f')