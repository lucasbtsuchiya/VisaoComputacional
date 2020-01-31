#Importando biblioteca OpenCV
import cv2

#Carregando uma imagem
imagem = cv2.imread('pessoas.jpg')
classificador = cv2.CascadeClassifier('haarcascade_frontalface_defult.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza)

print(deteccoes)
#Quantas pessoas conseguiu detectar
print(len(deteccoes))


#Bounding box (caixa delimitadoras)
# - Haarcascade(OpenCV)
# - Left, top, width, height
for (x, y, l, a) in deteccoes:
  cv2.rectangle(imagem, (x,y), (x + l, y + a), (0,225,0),2)

 #Abrir a imagem com os retângulos
cv2.imshow('Detector de faces', imagem)

#Fechar a janela e liberar memoria, após pressionar qualquer tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
