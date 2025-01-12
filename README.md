# OCR para Extração de Números

Este script utiliza a biblioteca EasyOCR para extrair números de uma imagem. Ele processa a imagem, converte para escala de cinza, aplica um thresholding para binarização e, em seguida, utiliza o EasyOCR para identificar e filtrar apenas os números presentes na imagem.

## Requisitos
- Python 3.11 ou superior
- Bibliotecas Python:
  - `easyocr`: para realizar o reconhecimento de texto.
  - `opencv-python`: para manipulação e processamento de imagens.
  - `re`: para expressões regulares, usadas para filtrar apenas números.

## Instalação

1. Certifique-se de que o Python 3.11 ou superior esteja instalado em sua máquina. Caso não tenha o Python instalado.
2. Instale as dependências necessárias com o seguinte comando:

```python pip install easyocr opencv-python```
