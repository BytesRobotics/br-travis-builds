# br-behavior-engine
Bytes behavior engine node. This node takes in inputs from the Bytes sensors and controller and outputs sounds and facial expressions to give the Byte a more sentient feel. It uses the smach library, pyglet library, and a database of 2 expressions and 20 sounds as of right now to achieve this.

-----------------------------------------------
# Installs
 - pip install tf argparse python-vlc pyglet==1.4.2 **REQUIRED PYTHON LIBS**
 - pip install psutil **TESTING ONLY / OPTIONAL**
 - https://linux4one.com/how-to-install-ffmpeg-on-ubuntu-18-04/ **FFMPEG 4 REQUIRED**
 - https://askubuntu.com/questions/736238/how-do-i-install-and-setup-the-environment-for-using-portaudio **PORTAUDIO REQUIRED**
 - sudo apt-get install ros-melodic-smach vlc **REQUIRED ROS PACKAGE AND VLC**

-----------------------------------------------
# Future Plans
 - Connect finite_emotion_engine to trash and face detecting AI and base emotions off that.
 - Grow database of facial expressions and sounds.
 - Hook up alexa using the lex api to allow the byte to have a conversation with a consumer.
