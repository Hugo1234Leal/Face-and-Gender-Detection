import urllib.request
from PIL import Image
import cv2
import numpy as np

URL = 'https://img.freepik.com/fotos-gratis/pessoas-sorridentes-em-uma-sessao-de-terapia-de-grupo_23-2148752038.jpg?w=2000'


def url_to_image(url):
    response = urllib.request.urlopen(url)
    image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


imagem = url_to_image(URL)

# so para ver a imagem... nao faz falta
#cv2.imshow('URL Image', imagem)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


"""
# converter imagem url em jpg ou png

urllib.request.urlretrieve(
    'https://s2.glbimg.com/nhEYyvKrIApd3VXw0BADpUIjlNQ=/e.glbimg.com/og/ed/f/original/2019/04/18/montagem.jpg',
    "img_criada.jpg")

img = Image.open("img_criada.jpg")
img = img.resize((800, 500), Image.ANTIALIAS)
img.save(fp="img_criada.jpg")

img.show()

# reconhecimento de faces

imagem = cv2.imread('img_criada.jpg')
"""

classificadorFace = cv2.CascadeClassifier(
    'haarcascades/haarcascade_frontalface_default.xml')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
detecta = classificadorFace.detectMultiScale(image=imagemCinza,
                                             scaleFactor=1.05, minNeighbors=50,
                                             minSize=(10, 10))

for (x, y, l, a) in detecta:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)
    contador = str(detecta.shape[0])
    cv2.putText(imagem, contador, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2, cv2.LINE_AA)

cv2.imwrite("fotos/img_teste_6.jpg", imagem)
# cv2.imshow("Deteccao de pessoas", imagem)
# cv2.waitKey()

# USAR O COMANDO -->       py Gender.py --image(m.jpg)
