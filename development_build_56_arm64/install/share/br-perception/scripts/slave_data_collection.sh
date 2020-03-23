#!/bin/bash

MASTER_URI=${1?Error: no master IP address given}
export ROS_MASTER_URI=http://${MASTER_URI}:11311
export ROS_IP=$(hostname -I | awk '{print $1}')
source ~/Github/br-core/catkin_ws/devel/setup.bash
roslaunch br-perception data_collector.launch
