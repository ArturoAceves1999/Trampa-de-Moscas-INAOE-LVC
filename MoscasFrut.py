import cv2
import os
import time
import pyautogui


captura = cv2.VideoCapture(1)
path = r'/home/atrapamocas/Desktop/MoscaFrut/Reporte diario/Trampa 1'
start_time = cv2.getTickCount()  # Get the start time
ti_c =os.path.getmtime(path)
c_ti = time.ctime(ti_c)
c_ti2 =c_ti.replace(":", ".")

while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
   
    
  if cv2.waitKey(1) & 0xFF != 255:
    cv2.imwrite(os.path.join(path, c_ti2 + '.jpg'), imagen)      
    break
    # Check elapsed time in seconds
  elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
  if elapsed_time >= 5:  # 2 seconds
      print("2 seconds elapsed, breaking the loop")
      cv2.imwrite(os.path.join(path, c_ti2 + '.jpg'), imagen)     
      break

    
captura.release()  
cv2.destroyAllWindows()


