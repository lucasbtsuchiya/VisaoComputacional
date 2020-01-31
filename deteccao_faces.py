import cv2

imagem = cv2.imread('pessoas.jpg')
classificador = cv2.CascadeClassifier('haarcascade_frontalface_defult.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detecMultiScale(imagemcinza)

print(deteccoes)
print(len(deteccoes))