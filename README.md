# Trampa-de-Moscas-INAOE-LVC

Initial configuration for Raspberry with Ubuntu 22 to work headless:

1.Download RealVNC Server for Raspberry and select the "ARM64" version.
The link is the next one: https://www.realvnc.com/es/connect/download/vnc/raspberrypi/

2.Open a terminal and go to the downloads folder by running:

	cd /Downloads

3.Run the command sudo dpkg -i <the realvnc file that you downloaded>.deb and finish the installation

4.Run the command

	cd

and then run

	sudo nano /etc/gdm3/custom.conf

here, you would need to uncomment the line:

	WaylandEnable=false

To save the changes use Ctrl + o, then enter, and then Ctrl + z

5.Run the RealVNC Server application and check that it opens correctly.

6.To improve the performance on VNC, you would need to run the following commands:

	cd
	sudo nano /boot/firmware/config.txt

add at the bottom of the text the following lines:

	hdmi_force_hotplug=1
	hdmi_force_mode=1
	hdmi_group=2
	hdmi_mode=82

and comment the following line:

	dtoverlay=vc4-kms-v3d

7.Get the IP of the Raspberry by running the ifconfig command on a terminal and copying the IPV6 that you get on the wlan0 connection.

For the first implementation, the hostname is 

	"atramacoscas-desktop"

you can use it on RealVNC to access the machine, make sure that you use the correct Raspberry password *AND* that you are connected to the same network as the Raspberry.

# Scripts:

We have 2 main scripts on the project present in the same git folder:

1.camera.py: 
This one opens the camera and lets you see the current image for 2 seconds. It is mainly used for debugging the camera functionality.

2.MoscasFrut.py:
This is the main program, where we turn on the camera and store the image on the drive folder related to the project. It has a basic error handling for multiple scenarios. It also has an error log management. The result messages can be seen on:

	./Reporte diario/Trampa 1/log-camera-1.txt
The error handling covers:

	1.If Drive folder path is not available, store the image locally and send the alert to the log file.
	2.If the local folder and drive folder are not available, send an error to the log file.
	3.If the camera is not detected, send an error to the log file.
	
*IMPORTANT*
Please make sure that the path mentioned on the code is the correct one or that the drive is mounted correctly, some times you would need to log again into the LVC Google account on your Raspberry device. Take note that the Google access token expires from time to time, so review the connection constantly.

Currently, we have another 2 necessary scripts to implement the automatic uploading of the image to drive once the Raspberry connects to the internet:

1.startup.sh:
This script mounts the drive folder of the desired account

2.cameraexecute.sh:
This script runs the MoscasFrut.py program. Make sure that the path mentioned there is the correct one where your code is stored.

*IMPORTANT*
On the first deployment, make sure to make the .sh files executable and store them in the /usr/local/bin folder. That last path can be changed to your necessities, but you would need to modify the information according on the services files.

# Services:

We created 2 services for ubuntu to run the .sh scripts:

1.startdrive.service:
This service executes when the device turns on and connects to the internet and executes the startup.sh scrip. This service may be executed several times at the startup of the device, so it has a restart function if the connection couldn't be made correctly.

1.imagescript.service:
This service executes once the startdrive finishes executing. It waits for 40 seconds and runs the cameraexecute.sh script.

*IMPORTANT*
Make sure to move the services to the /etc/systemd/system folder AND enable de services. To do so, once you moved the files, you need to run the following commands:

	cd /etc/systemd/system
	sudo systemctl enable startdrive.service
	sudo systemctl enable imagescript.service
	
Once you boot/reboot the device, you can go to the log file of the camera execution to make sure that it ran correctly. For further debugging, you could use:

	sudo systemctl status <The service that you are tracking>.service

You can create new .services and .sh files to automate the execution of the MoscasFrut.py program.


