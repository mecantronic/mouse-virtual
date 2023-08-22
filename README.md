# Control virtual de mouse con Movimiento de los ojos 🐀

Este script en python captura el movimiento de los ojos utilizando la biblioteca [MediaPipe](https://developers.google.com/mediapipe) y controla el movimiento del mouse en la pantalla utilizando la biblioteca PyAutoGUI.

## Características

- Captura el movimiento de los ojos utilizando el módulo [FaceMesh de MediaPipe](https://developers.google.com/mediapipe/solutions/vision/face_landmarker).
- Rastrea los puntos de referencia de los ojos para controlar un cursor virtual.
- Dibuja la trayectoria del cursor en un lienzo.

## Instalación 💻

1. Clona este repositorio:
``` bash
git clone https://github.com/mecantronic/
```
2. Accede al directorio del proyecto:
``` bash
cd 
```
3. Crea y activa el entorno virtual:
``` bash
python -m venv env
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
4. Instala las dependencias:
``` bash
pip install -r requeriments.txt # En Windows: venv\Scripts\activate
```

## Ejecutar el Mouse Virtual  ▶️

Para ejecutar el teclado virtual, simplemente corra el script teclado_virtual.py:

``` bash
python teclado_virtual.py
```

## Cómo contribuir 🤝

Si deseas contribuir a este proyecto, simplemente sigue estos pasos:

* Crea un fork del repositorio.
* Crea una nueva rama para tu funcionalidad o corrección de errores, desde la rama `develop`: `git checkout -b nombre_de_la_rama`.
* Realiza tus cambios y realiza los commits: `git commit -m "Descripción de los cambios"`.
* Sube los cambios a tu repositorio remoto: `git push origin nombre_de_la_rama`.
* Crea un Pull Request en este repositorio.

¡Gracias por usar nuestro mouse virtual! Esperamos que sea útil para tus necesidades. Si tienes alguna pregunta o problema, no dudes en abrir un issue en este repositorio.