

memory = [0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0]

"""Mapas de bits, a memória é 
dividida em unidades de alocação. 
Cada bit do mapa representa uma 
unidade de alocação, sendo que se 
o bit for 0, a unidade está livre; 
caso contrário, a unidade está 
ocupada. Quanto menor for a unidade 
de alocação, maior será o mapa de 
bits e vice-versa.
O parâmetro tmpSize precisa ser 
divisor do parâmetro tmpMemory"""
#tmpMemory: Unidade de memória
#tmpSize: Tamanho de cada segmento
def bitmap(tmpMemory, tmpSize):
  units = len(tmpMemory)/tmpSize 
  listUnits = [] 
  while units == 0:
    listUnits.append(0)
    units -= 1
  return listUnits

"""Aloca um programa de tamanho *tmpFileSize*
no primeiro segmento de espaco vazio
que for maior ou igual ao seu 
tamanho, e toma como unidade de memoria 
*tmpBitmap* """
def firstFit(tmpBitmap, tmpFileSize):
  idxInit = 0
  increment = 0
  lista = tmpBitmap
  while True:
    """Se a soma dos 
    elementos do intervalo 
    lista[idxInit:tmpFileSize+idxInit]
    forem igual a 0 substitua o valor
    de todos os elementos desse 
    intervalo por 1"""
    if sum(lista[idxInit:(tmpFileSize+idxInit)])==0:
      increment = idxInit
      print(lista)
      while lista[tmpFileSize+idxInit-1]==0:
        lista[increment] = 1
        print(lista)
        increment += 1
      return lista
    #Senão, adicione 1 a variavel idxInit
    else:
      idxInit+=1
       
#def nextFit(tmpBitmap, tmpFileSize):
  
      
firstFit(memory, 3)
    
  





  