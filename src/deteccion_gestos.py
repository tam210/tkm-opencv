import cv2
import mediapipe as mp

class HandGestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        """
        Detecta las manos en el frame dado y dibuja los puntos clave.
        """
        # Convierto el frame a RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Dibujar los puntos clave en la imagen
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return result

    def is_heart_gesture(self, landmarks):
        """
        Detecta si las manos están haciendo el gesto de corazón.
        Aquí se puede implementar la lógica comparando distancias entre puntos específicos.
        """
        if len(landmarks) == 2:  # Comprobamos que ambas manos están presentes
            left_hand = landmarks[0].landmark
            right_hand = landmarks[1].landmark

            # Comparamos las posiciones de los dedos índice y pulgar de ambas manos
            # El corazón se forma cuando los índices y pulgares se acercan lo suficiente.
            left_thumb_tip = left_hand[self.mp_hands.HandLandmark.THUMB_TIP]
            left_index_tip = left_hand[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]

            right_thumb_tip = right_hand[self.mp_hands.HandLandmark.THUMB_TIP]
            right_index_tip = right_hand[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calcular la distancia euclídea entre los puntos clave
            def distance(point1, point2):
                return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

            thumb_dist = distance(left_thumb_tip, right_thumb_tip)
            index_dist = distance(left_index_tip, right_index_tip)

            # Condición para que la distancia entre los dedos sea pequeña, indicando un corazón
            if thumb_dist < 0.1 and index_dist < 0.1:
                return True

        return False
