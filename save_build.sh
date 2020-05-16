#!/bin/bash

# $1 travis branch
# $2 ci source path
# $3 Git token
# $4 travis build number
# $5 CPU Architecture
# $6 ROS distro

let "a = $4 - 1"
sudo rm -R development_build_${a}_*

dir=$1_build_$4_$5_$6

mkdir $dir

if [ $6 == 'melodic' ]
then
  mv $2/catkin_ws/install ./$dir/
fi

if [ $6 == 'eloquent' ]
then
  mv $2/ros2_ws/install ./$dir/
fi

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git add .
git commit -m "Travis Build $4"

git remote add master https://$3@github.com/BytesRobotics/br-travis-builds.git > /dev/null 2>&1
git push --quiet --set-upstream master master
