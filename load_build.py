import os
import sys
import shutil

os.system("git pull")

print("WARNING: BY LOADING A BUILD, YOU ARE REMOVING THE SRC FOLDER FOR YOUR CURRENT BR-CORE REPO. MAKE SURE ALL CHANGES ARE COMMITED AND PUSHED.")

exists = False

while not exists:
	shell_choice = raw_input("What is your shell [zsh:1 / bash:2]? >> ")
	if "1" in shell_choice:
		shell = "zsh"
		exists = True
	elif "2" in shell_choice:
		shell = "bash"
		exists = True
	else:
		print("Not a choice.")

exists = False

while not exists:
	branch_choice = raw_input("Which branch [master:1 / development:2 / release:3]? >> ")

	if "1" in branch_choice:
		branch = "master"
		exists = True
	elif "2" in branch_choice:
		branch = "development"
		exists = True
	elif "3" in branch_choice:
		branch = "release"
		exists = True
	else:
		print("Not a branch")

exists = False

while not exists:
	arch_choice = raw_input("Which arch [AMD64:1 / ARM64:2]? >> ")

	if "1" in arch_choice:
		arch = "amd64"
		exists = True
	elif "2" in arch_choice:
		arch = "arm64"
		exists = True
	else:
		print("Not a branch")

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
	build_choice = raw_input("Which build do you want? (Put the number not the name) >> ")
	build_choice.rstrip()

	try:
		if int(build_choice) > len(build_list) or int(build_choice) <= 0:
			print("Not a choice.")
		else:
			exists = True
	except ValueError:
		print("You did not enter a number.")

print ("Loading " + build_list[int(build_choice) - 1])

print("Creating source script install...")

if os.path.exists("./source.zsh"):
	os.system("rm -rf source.zsh")

os.system("echo 'source ./" + branch + "_" + build_list[int(build_choice) - 1] + "/install/setup." + shell + " && source .venv/bin/activate' > source.zsh")

print("Done..... Source source.zsh and roslaunch!")
