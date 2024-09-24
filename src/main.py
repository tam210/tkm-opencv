import cv2
from deteccion_gestos import HandGestureDetector
from texto_popup import display_text
from utils import load_config

def main():
    # Cargamos la configuración del texto desde config.yaml
    config = load_config()

    # Inicializamos la cámara
    cap = cv2.VideoCapture(0)
    gesture_detector = HandGestureDetector()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        # Detectar manos
        results = gesture_detector.detect_hands(frame)

        # Comprobar si hay un gesto de corazón
        if results.multi_hand_landmarks:
            if gesture_detector.is_heart_gesture(results.multi_hand_landmarks):
                display_text(frame, config)

        # Mostrar el frame
        cv2.imshow('Heart Gesture Detector', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
