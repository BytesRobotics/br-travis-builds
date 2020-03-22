#!/bin/bash

dir=$1_build_$(date +"%Y-%m-%d-%I:%M-%p")

mkdir $dir

cp -r $2/catkin_ws/build ./$dir/
cp -r $2/catkin_ws/devel ./$dir/

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git add .
git commit -m "Travis Build"

git remote add master https://$3@github.com/BytesRobotics/br-travis-builds.git > /dev/null 2>&1
git push --quiet --set-upstream master master
