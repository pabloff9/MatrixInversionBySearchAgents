from principal import Matriz
from fractions import Fraction

class MatrizEstendidaEstado(Matriz):
    """
    Essa classe representa um estado no espaço de busca.
    Ele é composto por uma matriz estendida x por y, onde y = 2x.
    """
    
    def __init__(self, matriz):
        self.linhasDaMatriz = matriz.linhasDaMatriz
        
    @staticmethod
    def estadoInicial(matriz):
        if (matriz.quantidadeDeColunas() == matriz.quantidadeDeLinhas()):
            novaMatriz = Matriz()
            for linha in matriz.linhasDaMatriz:
                novaLinha = linha[::] #copiando
                for i in range(matriz.quantidadeDeColunas()):
                    if (i == matriz.linhasDaMatriz.index(linha)):
                        novaLinha.append(Fraction(1))
                    else:
                        novaLinha.append(Fraction(0))
                novaMatriz.adicionarLinha(novaLinha)
                
        return MatrizEstendidaEstado(novaMatriz)
    
    def testeEstadoFinal(self):
        
        for indiceDaLinha, linha in enumerate(self.linhasDaMatriz):
            for posicaoDoElemento, elemento in enumerate(linha[:len(linha)//2]):
                if ((indiceDaLinha == posicaoDoElemento and elemento != 1) or
                    indiceDaLinha != posicaoDoElemento and elemento != 0):
                    return False
        
        return True
    
    def sucessores(self):
        listaDeSucessores = []
        
        """
        primeiro os sucessores que tornam 1 algum dos elementos.
        """
#         for linha in self.linhasDaMatriz:
#             for elemento in linha:
#                 if (elemento != 0):
#                     sucessor = self.multiplicarLinhaPorEscalarERetornarMatriz(self.linhasDaMatriz.index(linha), elemento)
#                     listaDeSucessores.append(sucessor)
          
        for numeroDaLinha in range(self.quantidadeDeLinhas()):
            for elemento in self.linhasDaMatriz[numeroDaLinha][:len(self.linhasDaMatriz[numeroDaLinha])//2]:
                if (elemento != 0 and elemento != 1):
                    sucessor = self.multiplicarLinhaPorEscalarERetornarMatriz(numeroDaLinha, 1/elemento)
                    listaDeSucessores.append(sucessor)
          
#         for numeroDaLinha in range(self.quantidadeDeLinhas()):
#             for indiceDoElemento in range(len(self.linhasDaMatriz[numeroDaLinha])//2):
#                 if (self.linhasDaMatriz[numeroDaLinha][indiceDoElemento] != 0):
#                     sucessor = self.multiplicarLinhaPorEscalarERetornarMatriz(numeroDaLinha, 1/self.linhasDaMatriz[numeroDaLinha][indiceDoElemento])
#                     listaDeSucessores.append(sucessor)
  
        """
        Agora os sucessores que são permutações das linhas
        """
          
          
                  
        sucessoresPorTrocaDeLinha = [self.trocarDuasLinhasDeLugar(i, j) for (i, j) in \
                                     [(i, j) for i in range(self.quantidadeDeLinhas()) \
                                      for j in range(self.quantidadeDeLinhas()) if j > i]]        
        listaDeSucessores += sucessoresPorTrocaDeLinha
          
      
        """
        Por fim, os sucessores por zerar elementos.
        Para cada elemento a de cada linha Li, multiplicar a linha Lj de todo b != 0
        na mesma coluna de a por -(a/b) e somar Lj sobre Li.
        """
          
#         for indiceDaLinha in range(self.quantidadeDeLinhas()):
#             for posicaoDoElemento in range(len(self.linhasDaMatriz[indiceDaLinha])):
#                                 
#                 listaDeSucessores += [self.somarLinhaComOutraLinhaMultiplicadaPorEscalar(indiceDaLinha,\
#                         indiceDaOutraLinha, -(self.linhasDaMatriz[indiceDaLinha][posicaoDoElemento]/self.linhasDaMatriz[indiceDaOutraLinha][posicaoDoElemento])\
#                         ) for indiceDaOutraLinha in list(range(indiceDaLinha)) + list(range(indiceDaLinha+1, self.quantidadeDeLinhas())) if\
#                         self.linhasDaMatriz[indiceDaOutraLinha][posicaoDoElemento] != 0]
        
        sucessoresParaZerar = []
        for indiceDaLinha in range(self.quantidadeDeLinhas()):
                        
            for posicaoDoElemento in range(len(self.linhasDaMatriz[indiceDaLinha])//2):
                
                linhaAtual = self.linhasDaMatriz[indiceDaLinha]
                elementoAtual = linhaAtual[posicaoDoElemento]
                
                if (elementoAtual != 0):
                
                    for indiceDeOutraLinha in list(range(indiceDaLinha)) + list(range(indiceDaLinha+1, \
                                        self.quantidadeDeLinhas())):
                                                
                        if (self.linhasDaMatriz[indiceDeOutraLinha][posicaoDoElemento] != 0):
                            
                            sucessoresParaZerar.append(self.somarLinhaComOutraLinhaMultiplicadaPorEscalar\
                                              (indiceDaLinha, indiceDeOutraLinha,\
                                            -(elementoAtual)/self.linhasDaMatriz[indiceDeOutraLinha][posicaoDoElemento]))
                            
                else:
                    continue
                
        listaDeSucessores += sucessoresParaZerar
        
        return [MatrizEstendidaEstado(sucessor) for sucessor in listaDeSucessores]
    
    def heuristica(self):
                
        valor = 0
                
        for indiceDaLinha, linha in enumerate(self.linhasDaMatriz):
            for posicaoDoElemento, elemento in enumerate(linha[:len(linha)//2]):
                if ((indiceDaLinha == posicaoDoElemento and elemento != 1) or
                    indiceDaLinha != posicaoDoElemento and elemento != 0):
                    valor += 1
        
        return valor
        
        
if __name__ == "__main__":
    
#     entrada = input("Digite a primeira Matriz.\n\n")
#     primeiraMatriz = Matriz()
#     
#     while(entrada != ""):
#         primeiraMatriz.adicionarLinhaAPartirdeString(entrada)
#         entrada = input()
#     
#     print("Sua matriz é: " + str(primeiraMatriz.linhasDaMatriz))
#     
#     print("Sua matriz é: " + str(primeiraMatriz))
#     
#     matrizEstendidaInicial = MatrizEstendidaEstado.estadoInicial(primeiraMatriz)
#     
#     print("Sua matriz estendida é: " + str(matrizEstendidaInicial))
#     
#     sucessoresParaZerar = matrizEstendidaInicial.sucessores()
#     for sucessor in sucessoresParaZerar:
#         print(str(sucessor))
#     
#     print("Oi")

#     a = MatrizEstendidaEstado.estadoInicial(Matriz([[1,2,3],[4,5,6],[7,8,9]]))
#     b = MatrizEstendidaEstado.estadoInicial(Matriz([[1,0,0],[0,1,0],[0,0,1]]))
#     print(a.testeEstadoFinal())
#     print(b.testeEstadoFinal())
    pass
