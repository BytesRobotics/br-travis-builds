# br-perception

Bytes camera node and data collection utilities.

Make sure to follow [this](https://medium.com/@jonathantse/fix-pink-tint-on-jetson-nano-wide-angle-camera-a8ce5fbd797f) guide to remove the purple tint on the cameras if not already done so on the current image. The extracted tar can be found in the config folder of this repository. A convenience script is also provided in scripts. It is recommended you use that before attempting to manually fix the camera.

## Steps for data collection

1. Setup the gbnet router (192.168.1.1, admin, password)
2. Connected the ethernet cable to the master jetson (the one permanently mounted onto the GB unit)
3. Connect and power the slave jetson also with ethernet making sure to verify that the left side has the left camera etc.
4. See the image below for all the connections
5. Once connected you should be able to connect to the wifi network and ssh into the jetson nano slave and master. You will need to check the DHCP addresses of each computer in the attached devices tab at 192.168.1.1
6. In scripts run the `master_data_collection.sh`  on the the central Jetson Nano. Note that you may need to stop the software to running on start and then reset the computer before being able to control the launching of the software stack. Instructions will be updated once system is fully developed. You will want to get the IP address of the master to be able to fill out the master URI argument in the next step.
7. On the slave jetson run the script in br-perception called `slave_data_collection.sh` which will prompt for the master's IP and the start the correct ROS node to relay the image information. Again verify that the respective cameras are on the right side of the garbage bytes unit and mounted at 45 degree angles from center. This can be aided by the GB learning cap.
8. To start training make sure that either a file name is sent to `/data_collector/nav_file` or a pose array of lat and long is send to `/data_collector/nav_points`. The format is pose array position x (lat) y (long).
9. Start recording with the Bool topic `is_data_collecting`