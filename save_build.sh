#!/bin/bash

dir=$1_build_$4

mkdir $dir

cp -r $2/catkin_ws/build ./$dir/
cp -r $2/catkin_ws/devel ./$dir/

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
