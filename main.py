import easyocr
import cv2
import re

# Carregar a imagem
image_path = 'C:\\Users\\graci\\Pictures\\BlueStacks\\Screenshot_2025.01.12_12.26.13.453.png'  # Substitua pelo caminho da sua imagem
img = cv2.imread(image_path)

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplique o thresholding para binarizar a imagem
_, threshold_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Inicialize o leitor EasyOCR
reader = easyocr.Reader(['en'], gpu=False)  # 'en' é o código para o idioma inglês

# Usar EasyOCR para detectar o texto na imagem
results = reader.readtext(threshold_img)

# Variável para armazenar os números encontrados
numbers = ""

# Filtrar e extrair apenas os números
for result in results:
    text = result[1]
    numbers += ''.join(re.findall(r'\d', text))  # Pega apenas os dígitos numéricos

# Exibir os números encontrados
print(f"Números encontrados na imagem: {numbers}")
