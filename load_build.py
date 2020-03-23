import os
import sys
import subprocess
import time

os.system("git pull")

print("WARNING: BY LOADING A BUILD, YOU ARE REMOVING THE SRC FOLDER FOR YOUR CURRENT BR-CORE REPO. MAKE SURE ALL CHANGES ARE COMMITED AND PUSHED.")

exists = False

while not exists:
	shell_choice = input("Which shell do you use [bash:1 / zsh:2]? >> ")

	if shell_choice == "1":
		shell = "bash"
		exists = True
	elif shell_choice == "2":
		shell = "zsh"
		exists = True
	else:
		print("Not an option.")

exists = False

while not exists:
	branch_choice = input("Which branch [master:1 / development:2 / release:3]? >> ")

	if branch_choice == "1":
		branch = "master"
		exists = True
	elif branch_choice == "2":
		branch = "development"
		exists = True
	elif branch_choice == "3":
		branch = "release"
		exists = True
	else:
		print("Not an option.")

exists = False

while not exists:
	arch_choice = input("Which arch [AMD64:1 / ARM64:2]? >> ")

	if arch_choice == "1":
		arch = "amd64"
		exists = True
	elif arch_choice == "2":
		arch = "arm64"
		exists = True
	else:
		print("Not an option.")

exists = False

while not exists:
	face_choice = input("Launch emotion_viewer [Y / N]? >> ")

	if face_choice == "Y":
		face = 1
		exists = True
	elif face_choice == "N":
		face = 0
		exists = True
	else:
		print("Not an option.")

build_list = []

for x in os.listdir(os.getcwd()):
	if branch in x and arch in x:
		build_list.append(x)

if len(build_list) == 0:
	print("No builds for this branch.")
	sys.exit()

else:
	new_list = []
	for x in build_list:
		x = x[len(branch) + 1:]
		new_list.append(x)
	build_list = sorted(new_list)

print()

count = 0

for x in build_list:
	count += 1
	print(str(count) + ": " + x)

print()

exists = False

while not exists:
	build_choice = input("Which build do you want? (Put the number not the name) >> ")

	try:
		if int(build_choice) > len(build_list) or int(build_choice) <= 0:
			print("Not a choice.")
		else:
			exists = True
	except ValueError:
		print("You did not enter a number.")

print ("Loading " + build_list[int(build_choice) - 1])

print("Launching..... Have a nice day!")

time.sleep(1)

sub = subprocess.Popen(["/bin/" + shell, "./run.sh", os.getcwd(), branch, build_list[int(build_choice) - 1], shell, face])
sub.wait()
