import cv2
import numpy as np

# Função de callback para as trackbars
def on_trackbar_blur(value):
    global kernel_size_blur
    kernel_size_blur = 2 * value + 1  # Garante que o tamanho do kernel seja ímpar

def on_trackbar_gaussian(value):
    global kernel_size_gaussian
    kernel_size_gaussian = 2 * value + 1  # Garante que o tamanho do kernel seja ímpar

# Inicialize a câmera
cap = cv2.VideoCapture(0)

# Crie uma janela para exibir o vídeo
cv2.namedWindow('Video')

# Crie as trackbars para os filtros passa-baixa
cv2.createTrackbar('Blur', 'Video', 1, 15, on_trackbar_blur)
cv2.createTrackbar('Gaussian', 'Video', 1, 15, on_trackbar_gaussian)

kernel_size_blur = 1
kernel_size_gaussian = 1

while True:
    # Capture o quadro da câmera
    ret, frame = cap.read()

    # Converta o quadro para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplique os filtros passa-baixa Blur e Gaussian
    blurred = cv2.blur(gray, (kernel_size_blur, kernel_size_blur))
    gaussian_blur = cv2.GaussianBlur(gray, (kernel_size_gaussian, kernel_size_gaussian), 0)

    # Some os resultados dos filtros passa-baixa
    combined = cv2.addWeighted(blurred, 0.5, gaussian_blur, 0.5, 0)

    # Aplique um filtro passa-alta Laplacian
    laplacian = cv2.Laplacian(combined, cv2.CV_64F)

    # Binarize o resultado do filtro Laplacian
    _, binary = cv2.threshold(np.abs(laplacian).astype(np.uint8), 30, 255, cv2.THRESH_BINARY)

    # Exiba o vídeo na janela
    cv2.imshow('Video', binary)

    # Saia do loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cap.release()
cv2.destroyAllWindows()
