#!/bin/bash

echo "Make sure no current roscore is running"
MASTER_URI="http://$(hostname -I | awk '{print $1}'):11311"
echo $MASTER_URI
export ROS_MASTER_URI=$MASTER_URI
export ROS_IP=$(hostname -I | awk '{print $1}')
source ~/Github/br-core/catkin_ws/devel/setup.bash
roslaunch  launch_files gb.launch face:=true rviz:=false
