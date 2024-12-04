# Trampa-de-Moscas-INAOE-LVC

Initial configuration for Raspberry with Ubuntu 22 to work headless:

1.Download RealVNC Server for Raspberry, making sure that you select the "ARM64" version.
The link is the next one: https://www.realvnc.com/es/connect/download/vnc/raspberrypi/

2.Open a terminal and go to the downloads folder by running:

	cd /Downloads

3.Run the command sudo dpkg -i <the realvnc file that you downloaded>.deb and finish the installation

4.Run the comand

	cd

and then run

	sudo nano /etc/gdm3/custom.conf

here, you would need to uncomment the line “WaylandEnable=false”. To save the changes just use Ctrl + o, then enter and then Ctrl + z

5.Run the RealVNC Server application and check that it opens correctly.

6.To improve the performance on VNC, you would need to run the next commands:

	cd
	sudo nano /boot/firmware/config.txt

add at the bottom of the text the following lines:

	hdmi_force_hotplug=1
	hdmi_force_mode=1
	hdmi_group=2
	hdmi_mode=82

and comment the following line:
	dtoverlay=vc4-kms-v3d

7.Get the IP of the raspberry by running the ifconfig command on a terminal and copying the IPV6 that you get on the wlan0 connection.

