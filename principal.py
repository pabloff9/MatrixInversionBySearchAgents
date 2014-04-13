#! /usr/bin/env python3

from fractions import Fraction

class Matriz():
    
    quantidadeDeColunas = 0
    quantidadeDeLinhas = 0
    linhasDaMatriz = None
    
    def __init__(self, listaDeLinhas=None):
        
        # Verificando se é uma matriz válida,
        # ou seja, se todas as linhasDaMatriz têm o mesmo tamanho
        
        if (listaDeLinhas != None and len(listaDeLinhas) != 0):
            quantidadeDeColunas = len(listaDeLinhas[0])
        else:
            quantidadeDeColunas = 0
            listaDeLinhas = []
            
        for linha in listaDeLinhas:
            if (len(linha) != quantidadeDeColunas):
                raise Exception
        
        #iniciando matriz
        self.linhasDaMatriz = listaDeLinhas

    def adicionarLinha(self, linha):
        
        #Se a matriz está vazia, não é necessário fazer nenhum teste
        
        if (self.quantidadeDeLinhas() == 0):
            pass
        else:
            if (len(linha) != self.quantidadeDeColunas()):
                raise Exception
        
        self.linhasDaMatriz.append(linha)
    
    def adicionarLinhaAPartirdeString(self, linha):
        
        novaLinha = []
        for numero in linha.split():
            novaLinha.append(Fraction(numero))
        
        self.adicionarLinha(novaLinha)
        
    def transposta(self):
        matrizTransposta = Matriz()
        
        for i in range(self.quantidadeDeColunas()):
            novaLinha = []
            for linha in self.linhasDaMatriz:
                novaLinha.append(linha[i])
#             matrizTransposta.append(novaLinha)
            matrizTransposta.adicionarLinha(novaLinha)
        
        return matrizTransposta
    
    def somar(self, outraMatriz):
        resultado = Matriz([])
        
        for i in range(self.quantidadeDeLinhas()):
            novaLinha = []
            for j in range(self.quantidadeDeColunas()):
                novaLinha.append(self.linhasDaMatriz[i][j] + outraMatriz.linhasDaMatriz[i][j])
            resultado.adicionarLinha(novaLinha)
        
        return resultado
    
    def inversaDFS(self):
        
        """
        Exceção em:
        1 2 3
        4 5 0
        0 1 1
        """
        
        from inversãoDeMatrizes import MatrizEstendidaEstado        
        """
        Usaremos uma busca em profundidade.
        Vamos precisar de um estado inicial para fazer a busca e uma fila fronteira
        """
        estadoInicial = MatrizEstendidaEstado.estadoInicial(self)
        fronteira = [estadoInicial]
        quantidadeDeExpandidos = 0
        quantidadeDeVisitados = 0
        expansoesDeVisitados = 0
        conjuntoDeVisitados = set()
        
        """
        Agora, para cada estado no final da fila, verificamos se é o estado final.
        Se não for, adicionamos os sucessores dele que já não estão
        na fila ao fim dela.
        """
        while (len(fronteira) != 0):
            atual = fronteira.pop()
            conjuntoDeVisitados.add(atual)
            quantidadeDeVisitados += 1
            
            if (atual.testeEstadoFinal()):
                
                inversa = [linha[len(linha)//2:] for linha in atual.linhasDaMatriz]
                print("%s estados expandidos. %s visitados. %s expansões de visitados." \
                                        % (quantidadeDeExpandidos, quantidadeDeVisitados, expansoesDeVisitados))
                return Matriz(inversa)
            else:
                sucessoresDoAtual = atual.sucessores()
                quantidadeDeExpandidos += len(sucessoresDoAtual)
#                 for sucessor in [sucessor for sucessor in sucessoresDoAtual if sucessor not in fronteira \
#                                  and sucessor not in conjuntoDeVisitados]:
#                     fronteira.append(sucessor)
                    
                for sucessor in sucessoresDoAtual:
                    if (sucessor in conjuntoDeVisitados):
                        expansoesDeVisitados += 1
                    if (sucessor not in fronteira and sucessor not in conjuntoDeVisitados):
                        fronteira.append(sucessor)
    
    def inversaBFS(self):
        
        from inversãoDeMatrizes import MatrizEstendidaEstado        
        """
        Usaremos uma busca em largura.
        Vamos precisar de um estado inicial para fazer a busca e uma fila fronteira
        """
        estadoInicial = MatrizEstendidaEstado.estadoInicial(self)
        fronteira = [estadoInicial]
        quantidadeDeExpandidos = 0
        quantidadeDeVisitados = 0
        expansoesDeVisitados = 0
        conjuntoDeVisitados = set()
        
        """
        Agora, para cada estado no inicio da fila, verificamos se é o estado final.
        Se não for, adicionamos os sucessores dele que já não estão
        na fila ao fim dela.
        """
        while (len(fronteira) != 0):
            atual = fronteira.pop(0)
            conjuntoDeVisitados.add(atual)
            quantidadeDeVisitados += 1
            
            if (atual.testeEstadoFinal()):
                
                inversa = [linha[len(linha)//2:] for linha in atual.linhasDaMatriz]
                print("%s estados expandidos. %s visitados. %s expansões de visitados." \
                                        % (quantidadeDeExpandidos, quantidadeDeVisitados, expansoesDeVisitados))
                return Matriz(inversa)
            else:
                sucessoresDoAtual = atual.sucessores()
                quantidadeDeExpandidos += len(sucessoresDoAtual)
#                 for sucessor in [sucessor for sucessor in sucessoresDoAtual if sucessor not in fronteira \
#                                  and sucessor not in conjuntoDeVisitados]:
#                     fronteira.append(sucessor)
                    
                for sucessor in sucessoresDoAtual:
                    if (sucessor in conjuntoDeVisitados):
                        expansoesDeVisitados += 1
                    if (sucessor not in fronteira and sucessor not in conjuntoDeVisitados):
                        fronteira.append(sucessor)

    def inversaComHeuristica(self):
        
        from inversãoDeMatrizes import MatrizEstendidaEstado
        import heapq
        
        """
        Vamos precisar de um estado inicial para fazer a busca e um heap fronteira
        """
        estadoInicial = MatrizEstendidaEstado.estadoInicial(self)
        fronteira = [(estadoInicial.heuristica(), estadoInicial)]
        conjuntoDeVisitados = set()
        heapq.heapify(fronteira)
        quantidadeDeExpandidos = 0
        quantidadeDeVisitados = 0
        expansoesDeVisitados = 0
        
        """
        Agora, escolhemos o estado com a menor heurística e, verificamos se é o estado final.
        Se não for, adicionamos os sucessores dele que já não estão
        na fila ao fim dela.
        """
        while (True):
#             (heuristica, estadoAtual) = fronteira[0]            
            
            (heuristicaDoEstadoAtual, estadoAtual) = heapq.heappop(fronteira)
            quantidadeDeVisitados += 1
            
            if (estadoAtual.testeEstadoFinal()):
                print("%s estados expandidos. %s visitados. %s expansões de visitados." \
                                        % (quantidadeDeExpandidos, quantidadeDeVisitados, expansoesDeVisitados))
                inversa = Matriz([linha[len(linha)//2::] for linha in estadoAtual.linhasDaMatriz])
                return inversa
            else:
                
                sucessoresDoAtual = estadoAtual.sucessores()
                quantidadeDeExpandidos += len(sucessoresDoAtual)
                                 
                for sucessor in sucessoresDoAtual:
                    tuplaSucessor = (sucessor.heuristica(), sucessor)
                    
                    if (tuplaSucessor in conjuntoDeVisitados):
                        expansoesDeVisitados+=1
                    
                    if (tuplaSucessor not in fronteira and tuplaSucessor not in conjuntoDeVisitados):
                        heapq.heappush(fronteira, tuplaSucessor)
                    
                    
            
            conjuntoDeVisitados.add((heuristicaDoEstadoAtual, estadoAtual))
#                 for (heuristica, sucessor) in [(sucessor.heuristica(), sucessor) for sucessor in sucessoresDoAtual
#                                                if (sucessor.heuristica(), sucessor) not in fronteira]:
#                     heapq.heappush(fronteira, (heuristica, sucessor))
                        
    def multiplicarLinhaPorEscalarERetornarLinha(self, linha, escalar):
        resultado = self.linhasDaMatriz[linha][::]
        for i in range(len(resultado)):
            resultado[i] = resultado[i]*escalar
        return resultado
    
    def somarLinhaComOutraLinhaMultiplicadaPorEscalar(self, linhaQueReceberaASoma, linhaQueSeraMultiplicada, escalar):
        
        resultado = Matriz([linha[::] for linha in self.linhasDaMatriz])
        
        for indiceDoElemento in range(self.quantidadeDeColunas()):
            resultado.linhasDaMatriz[linhaQueReceberaASoma][indiceDoElemento] =\
                    self.linhasDaMatriz[linhaQueReceberaASoma][indiceDoElemento]\
                    + escalar*self.linhasDaMatriz[linhaQueSeraMultiplicada][indiceDoElemento]
        return resultado
    
    def multiplicarLinhaPorEscalarERetornarMatriz(self, linha, escalar):
        resultado = Matriz([linha[::] for linha in self.linhasDaMatriz])
        resultado.linhasDaMatriz[linha] = self.multiplicarLinhaPorEscalarERetornarLinha(linha, escalar)
        return resultado
    
    def trocarDuasLinhasDeLugar(self, indiceDaPrimeira, indiceDaSegunda):
        resultado = Matriz([linha[::] for linha in self.linhasDaMatriz])
        resultado.linhasDaMatriz[indiceDaPrimeira] = self.linhasDaMatriz[indiceDaSegunda][::]
        resultado.linhasDaMatriz[indiceDaSegunda] = self.linhasDaMatriz[indiceDaPrimeira][::]
        return resultado
        
    def __str__(self):
        
#         matriz = "\n"
#         for linha in self.linhasDaMatriz:
#             matriz += "|"
#             for numero in linha:                
#                 matriz += "%4s " % (numero,)
#             matriz += "\n|\n"
#         
#         return matriz
    
        matriz = "\n"
        for linha in self.linhasDaMatriz:
            matriz += "| "
            for numero in linha:
                matriz += "%4s " % (numero,)
            matriz += "|\n\n"
        
        return matriz
    
    def quantidadeDeLinhas(self):
        return len(self.linhasDaMatriz)
    
    def quantidadeDeColunas(self):
        if (self.quantidadeDeLinhas() != 0):
            return len(self.linhasDaMatriz[0])
        else:
            return 0
    
    def __eq__(self, outraMatriz):
        
        for indiceDaLinha, linha in enumerate(self.linhasDaMatriz):
            for indiceDaColuna, elemento in enumerate(linha):
                if (elemento != outraMatriz.linhasDaMatriz[indiceDaLinha][indiceDaColuna]):
                    return False
        return True
    
    def __lt__(self, outraMatriz):
        total = 0
        for indiceDaLinha, linha in enumerate(self.linhasDaMatriz):
            for indiceDaColuna, elemento in enumerate(linha):
                total += elemento - outraMatriz.linhasDaMatriz[indiceDaLinha][indiceDaColuna]
        return (total < 0)
    
    def __hash__(self):
        total = 0
        
        for indiceDaLinha, linha in enumerate(self.linhasDaMatriz):
            for indiceDaColuna, elemento in enumerate(linha):
                total+=(indiceDaLinha*self.quantidadeDeLinhas() + indiceDaColuna) * elemento
                
        return int(total)
        
    
if __name__ == "__main__":

    entrada = input("Digite a matriz a ser invertida. (Enter your matrix to get is inverse)\n\n")
    primeiraMatriz = Matriz()
     
    while(entrada != ""):
        primeiraMatriz.adicionarLinhaAPartirdeString(entrada)
        entrada = input()
          
#     a = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     
#     s = set([a])


    print("Com heurística (using heuristic): " + str(primeiraMatriz.inversaComHeuristica()))

    print("Sem heurística - DFS: (no heuristic - DFS)" + str(primeiraMatriz.inversaDFS()))
        
    print("Sem heurística - BFS: (no heuristic - BFS)" + str(primeiraMatriz.inversaBFS()))
         
