#!/bin/bash

# $1 travis branch
# $2 ci source path
# $3 Git token
# $4 travis build number
# $5 CPU Architecture
# $6 ROS distro

dir=$1_build_$4_$5_$6

mkdir $dir

if [ $6 == 'melodic' ]
then
  cp -r $2/catkin_ws/install ./$dir/
fi

if [ $6 == 'eloquent' ]
then
  cp -r $2/ros2_ws/install ./$dir/
fi

number_of_dirs=$(ls -l ../ | grep -c ^d)

if [ $number_of_dirs -gt 40 ]
then
  echo "COMPRESS OLD FOLDERS PLZ I NO GOOD AT SHELL SCRIPTS" >> ./compress.txt
fi

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git add .
git commit -m "Travis Build $4"

git remote add master https://$3@github.com/BytesRobotics/br-travis-builds.git > /dev/null 2>&1
git push --quiet --set-upstream master master
