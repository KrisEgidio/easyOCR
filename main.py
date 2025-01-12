import easyocr
import cv2
import re

# Carregar a imagem
image_path = 'imagem.png'
img = cv2.imread(image_path)

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplique o thresholding para binarizar a imagem
_, threshold_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Inicialize o leitor EasyOCR
reader = easyocr.Reader(['en'], gpu=False)

# Detectar o texto na imagem
results = reader.readtext(threshold_img)


numbers = ""

# Filtrar e extrair apenas os números
for result in results:
    text = result[1]
    numbers += ''.join(re.findall(r'\d', text))


print(f"Números encontrados na imagem: {numbers}")
