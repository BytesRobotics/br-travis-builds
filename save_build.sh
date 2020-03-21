#!/bin/bash

dir=$1_build_$(date +"%Y-%m-%d-%I:%M-%p")

mkdir $dir

cp -r ../catkin_ws/build ./$dir/
cp -r ../catkin_ws/devel ./$dir/
