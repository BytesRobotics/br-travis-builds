source $1/$2_$3/install/setup.$4

if [ $5 = 1 ]
then
  roslaunch launch_files br.launch face:=true
fi

if [ $5 = 0 ]
then
  roslaunch launch_files br.launch
fi