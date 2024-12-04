import cv2
import os
import time
import datetime
import pyautogui

print("Setting up the camera, path, and logs please wait...")

captura = cv2.VideoCapture(0)
path = '/run/user/1000/gvfs/google-drive:host=gmail.com,user=lvctfruta/GVfsSharedWithMe/1EKXB6EA8oBaYaB1ZqVub4xDf8eRS2SuV/1Af5moXu0KUXqpgD56vpq8mKAkoOGWBkJ/1dw-MbWP9yfLTxvIsw-GkQBZSCZcquKXW'
newpath = os.getcwd() + '/Reporte diario/Trampa 1' #Used for logs and if the camera fails.


#path = '/home/atrapamocas/Desktop'
start_time = cv2.getTickCount()  # Get the start time
timenow = datetime.datetime.now()
timeformat = timenow.strftime('%a %d %b %X %Y')

logfile = open(newpath + "/log-camera-1.txt", "a")
logfile.write("\n\n\nLog of the date ")
logfile.write(timeformat)

print("\nDate: ",timeformat)
print("\nPath: ", path)

n = ''

while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
  else:
      n = "\nImage not available, please check"
      print(n)
      logfile.write(n)
      break
   
    
  if cv2.waitKey(1) & 0xFF != 255:
    cv2.imwrite(os.path.join(path, timeformat + '.jpg'), imagen)      
    break
    # Check elapsed time in seconds
  elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
  if elapsed_time >= 5:  # 2 seconds
      print("\n2 seconds elapsed, closing the camera")
      iswritten = cv2.imwrite(os.path.join(path, timeformat + '.jpg'), imagen)
      if iswritten is True:
          n = "\nImage saved successfully on path "
          print(n)
          logfile.write(n)
      else:
          iswrittennew = cv2.imwrite(os.path.join(newpath, timeformat + '.jpg'), imagen)
          if iswrittennew is True:
              n = "\nImage was not saved on the original path. Please check. Image saved on Reporte diario folder"
              print(n)
              logfile.write(n)
          else:
              n = "\nImage was not saved on the original path, neither the Reporte diario folder. Please check"
              print(n)
              logfile.write(n)
      break

if captura.isOpened() is False:
    n = "\n Camera error, please check integrity or release "
    logfile.write(n)
    print(n)
    
captura.release()  
cv2.destroyAllWindows()
logfile.close()

