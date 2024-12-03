import cv2
import os
import time
import matplotlib.pyplot as plt


captura = cv2.VideoCapture(0)
path = r'C:\Users\emman\OneDrive\Escritorio\MoscaFrut\Reporte diario'
ti_c =os.path.getmtime(path)
c_ti = time.ctime(ti_c)
c_ti2 =c_ti.replace(":", "-")

while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
      #cv2.imwrite(os.path.join(path , 'Dato.jpg'), imagen)
      cv2.imwrite(os.path.join(path, c_ti2 + '.jpg'), imagen)
      
      #plt.imsave( c_ti2 + '.jpg',imagen )

      break
      captura.release()
      


  else: break
cv2.destroyAllWindows()
