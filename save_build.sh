#!/bin/bash

dir=$1_build_$(date +"%Y-%m-%d-%I:%M-%p")

mkdir $dir

cp -r $2/catkin_ws/build ./$dir/
cp -r $2/catkin_ws/devel ./$dir/
