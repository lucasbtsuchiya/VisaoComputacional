#Importando biblioteca OpenCV
import cv2

print(cv2.__version__)
imagem = cv2.imread('Imagens_Canecas/teste10.jpg')

classificador = cv2.CascadeClassifier('cascade_caneca1.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Parâmetros do detectMultiScale
# Scale Factor scaleFactor = valor_da_escala
# minNeighbors minNeighbors = valor
# minSize
deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor=1.1, minNeighbors=4)

print(deteccoes)
print(len(deteccoes))

# Haardcascade (OpenCV)
# Marcar as faces detectadas
for (x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

cv2.imshow('Detecctor de faces', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()