# Trecho do código para abrir as imagens e carregar em um vetor de imagens.
import cv2
import glob
import numpy as np
from pathlib import Path

#Caminho para salvar imagem
caminhoImagem = Path('Atividades')

# Abre as imagens de um diretório e armazena em um vetor
filelist = glob.glob('Anexos, Imagens e Videos\Satelite_ruido\*.png')
imagens = np.array([np.array(cv2.imread(fname,cv2.IMREAD_GRAYSCALE)) for fname in filelist])

# Armazena as colunas e linhas de uma imagem
rows,cols = imagens[0].shape
# Cria uma imagem vazia para armazenar o resultado
resultadoMedianaManual = np.zeros((rows,cols),np.uint8)
resultadoMediaManual = np.zeros((rows,cols),np.uint8)

# Varre as linhas e colunas da imagem
for r in range(rows):
   for c in range(cols):
    # Ordena em um vetor o mesmo pixel de todas imagens
    xyTodasImagemsMediana = np.sort(imagens[:,r,c])
    #Calculando a posição da mediana
    posMediana = int(len(xyTodasImagemsMediana)/2)
    resultadoMedianaManual[r, c] = xyTodasImagemsMediana[posMediana]

    # Armazena em um vetor o mesmo pixel de todas imagens
    xyTodasImagemsMedia =  imagens[:,r,c]
    #For para obter a soma de todos os elementos do vetor
    soma = 0 
    for elemento in xyTodasImagemsMedia: 
      soma += elemento 
    #Calculando a media
    media = soma / len(xyTodasImagemsMedia)
    resultadoMediaManual[r, c] = media

#Mostrando as imagens
cv2.namedWindow('Imagem filtro Mediana', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro Mediana', resultadoMedianaManual)
cv2.namedWindow('Imagem filtro Media', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro Media', resultadoMediaManual)

#Salvando as imagens
#cv2.imwrite(str(caminhoImagem / 'ResultadoMediana.png'), resultadoMedianaManual)
#cv2.imwrite(str(caminhoImagem / 'ResultadoMedia.png'), resultadoMediaManual)

cv2.waitKey(0)
cv2.destroyAllWindows()
