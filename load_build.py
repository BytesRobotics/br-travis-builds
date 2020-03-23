import os
import sys
import shutil

print("WARNING: BY LOADING A BUILD, YOU ARE REMOVING THE SRC FOLDER FOR YOUR CURRENT BR-CORE REPO. MAKE SURE ALL CHANGES ARE COMMITED AND PUSHED.")

if os.path.exists(os.path.expanduser("~") + "/Github/br-core/catkin_ws"):
	print("Default path found.")
	path = os.path.expanduser("~") + "/Github/br-core/catkin_ws"

else:
	print("Could not find default location for br-core repo, manual input required.")

	exists = False

	while not exists:
		path = os.path.expanduser("~") + "/" + input("What is the path (after home folder) to br-core's catkin_ws folder? >> ")
		if os.path.exists(path) and os.path.exists(path + "/src"):
			exists = True
		elif os.path.exists(path) and not os.path.exists(path + "/src"):
			print("The path you entered exists, but has no src directory.")
			print("This may not be your br-core workspace.")
			choice = input("Do you want to continue? [Y or N] >> ")

			if choice == "Y":
				exists = True
			elif choice == "N":
				print("Aborting.")
			else:
				print("Not a choice, exiting.")
				sys.exit()
		else:
			print("That is not a path")

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
		print("Not a branch")

build_list = []

for x in os.listdir(os.getcwd()):
	if branch in x:
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

if os.path.exists(path + "/install"):
	print("Deleting old install dir.")
	shutil.rmtree(path + "/install")

if os.path.exists(path + "/src"):
	print("Deleting old src dir. Remember to re git clone when making new changes.")
	shutil.rmtree(path + "/src")

print("Copying install...")

src = os.getcwd() + "/" + branch + "_" + build_list[int(build_choice) - 1] + "/install"
dest = path + "/install"

try:
	shutil.copytree(src, dest)
except shutil.Error as e:
	print('Directory not copied, probably the same dir. Error: %s' % e)
except OSError as e:
	print('Directory not copied, probably doesnt exist. Error: %s' % e)

print("Copying src...")

src = os.getcwd() + "/" + branch + "_" + build_list[int(build_choice) - 1] + "/src"
dest = path + "/src"

try:
	shutil.copytree(src, dest)
except shutil.Error as e:
	print('Directory not copied, probably the same dir. Error: %s' % e)
except OSError as e:
	print('Directory not copied, probably doesnt exist. Error: %s' % e)

print("Done..... Have a nice day!")
