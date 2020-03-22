import os

path = input("What is the full path to br-core's catkin_ws folder? >> ")

branch = input("Which branch? >> ")

build_list = [for x in os.listdir(os.getcwd()) if branch in x]

print(build_list)
