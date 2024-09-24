import cv2

def display_text(frame, config):
    """
    Muestra el texto 'Tkm' con los parámetros definidos en config.
    """
    font_scale = config['display']['font_scale']
    color = tuple(config['display']['color'])
    position = tuple(config['display']['position'])
    thickness = config['display']['thickness']
    text = config['display']['text']

    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)
