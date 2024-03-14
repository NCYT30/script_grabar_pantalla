import cv2
import numpy as np 
import pyautogui
import keyboard

fps = 10.0 
resolucion = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('grabacion.mp4', fourcc, fps, resolucion)

while True:
    frame = np.array(pyautogui.screenshot())

    if frame is not None and frame.any():
        frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
        out.write(frame)

    if keyboard.is_pressed('q'):
        break

out.release()
cv2.destroyAllWindows()
