import cv2
import os
import time
import pyautogui

print("Setting up the camera and path, please wait...")

captura = cv2.VideoCapture(0)
path = '/run/user/1000/gvfs/google-drive:host=gmail.com,user=lvctfruta/GVfsSharedWithMe/1EKXB6EA8oBaYaB1ZqVub4xDf8eRS2SuV/1Af5moXu0KUXqpgD56vpq8mKAkoOGWBkJ/1dw-MbWP9yfLTxvIsw-GkQBZSCZcquKXW'

#path = '/home/atrapamocas/Desktop'
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
      print("\n With the date: ",c_ti2)
      print("\n To the path: ", path)
      x = cv2.imwrite(os.path.join(path, c_ti2 + '.jpg'), imagen)
      print("Status of cv2.imwrite: ",x)   
      break

    
captura.release()  
cv2.destroyAllWindows()


