import cv2

imagem = cv2.imread('/home/ngwebsig/Documents/Estágio/fotos/img_teste_4.jpg')
classificadorFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
detecta = classificadorFace.detectMultiScale(image = imagemCinza, scaleFactor = 1.05, minNeighbors = 50, minSize = (10, 10))

for (x, y, l, a) in detecta:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)
    contador = str(detecta.shape[0])
    cv2.putText(imagem, contador, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imwrite("/home/ngwebsig/Documents/Estágio/fotos/img_teste_5.jpg", imagem)
#cv2.imshow("Deteccao de pessoas", imagem)
#cv2.waitKey()