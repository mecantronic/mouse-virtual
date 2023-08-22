import cv2
import mediapipe as mp
import pyautogui
import numpy as np

def main():
    """
    Captura el movimiento de la mano utilizando la biblioteca MediaPipe y controla el cursor virtual en pantalla
    usando la biblioteca PyAutoGUI.
    """
    # Inicialización de FaceMesh
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    
    # Inicialización de la cámara
    cam = cv2.VideoCapture(0)
    
    # Tamaño de la pantalla
    screen_w, screen_h = pyautogui.size()
    
    # Crear un lienzo en blanco del tamaño de la pantalla
    canvas = np.ones((screen_h, screen_w, 3), np.uint8) * 255
    
    # Posición previa del cursor
    prev_x, prev_y = pyautogui.position()

    while True:
        # Obtener la posición actual del cursor
        current_x, current_y = pyautogui.position()

        # Dibujar una línea desde la posición anterior a la actual con opacidad reducida
        cv2.line(canvas, (prev_x, prev_y), (current_x, current_y), (0, 0, 0), 2, cv2.LINE_AA)

        # Aplicar desvanecimiento al lienzo
        canvas = cv2.addWeighted(canvas, 0.95, np.ones_like(canvas) * 255, 0.05, 0)

        # Capturar un frame de la cámara
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (426, 340))
        
        # Procesar la imagen con FaceMesh
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                
                # Dibujar un punto en la imagen
                cv2.circle(frame, (x, y), 2, (0, 255, 0))
                
                if id == 1:
                    # Calcular la posición en la pantalla
                    screen_x = screen_w / frame_w * x
                    screen_y = screen_h / frame_h * y
                    
                    # Mover el cursor virtual
                    pyautogui.moveTo(screen_x, screen_y)
                    
                    # Actualizar la posición previa
                    prev_x, prev_y = current_x, current_y
                    
                    # Mostrar la ventana con la trayectoria dibujada
                    cv2.imshow("Cursor Trajectory", canvas)
        
        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imshow('Mouse virtual', frame)

    # Cerrar todas las ventanas al finalizar
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
