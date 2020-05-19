#!/usr/bin/env python

import speech_recognition as sr
from os.path import expanduser
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import numpy as np
import time, sys, rospy, os
from std_msgs.msg import String

## REMEBER TO CHANGE AUDIO DEVICE

def publish(data, topic):
    pub = rospy.Publisher(topic, String, queue_size=10) # Set topic
    pub.publish(data) # Send to topic

if __name__ == '__main__':
    rospy.init_node('mic', anonymous=True) # Create ros node

    os.system("pactl set-default-source 'alsa_input.usb-Solid_State_System_Co._Ltd._iTalk-02_000000000000-00.analog-mono'")
    os.system("pactl set-default-sink 'alsa_output.usb-Generic_USB2.0_Device_20130100ph0-00.iec958-stereo'")

    cwd = expanduser("~") + '/Github/br-core/catkin_ws/src/br-behavior-engine/src/wav_files/'  # Get working directory

    r = sr.Recognizer()  # Setup library

    # Set keywords
    keyWord = 'record for'
    exitKeyWord = 'exit'

    with sr.Microphone() as source:  # Open mic channel
        rospy.loginfo("Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=2)  # listen for 2 seconds and figure out level of ambient noise
        rospy.loginfo("Mic Ready!")

        while not rospy.is_shutdown():  # loop
            audio = r.listen(source)  # Listen to audio
            try:
                text = r.recognize_google(audio)  # Put transcribed audio in variable
                if keyWord.lower() in text.lower():  # Check for keyword
                    rospy.loginfo("Google thinks you said '" + r.recognize_google(audio) + "'")

                    a, b, seconds = text.split(" ")  # Get seconds to record

                    rospy.loginfo('Recording audio for ' + seconds + " seconds.")
                    rospy.loginfo('Start Speaking in 3...')
                    time.sleep(1)  # Sleep for 1 second
                    rospy.loginfo('2...')
                    time.sleep(1)  # Sleep for 1 second
                    rospy.loginfo('1...')
                    time.sleep(1)  # Sleep for 1 second
                    rospy.loginfo("Go!")
                    time.sleep(0.5)  # Sleep for 0.5 seconds

                    fs = 44100  # Sample rate
                    sd.default.samplerate = fs  # Set it as default
                    sd.default.device = 'default'  # Set input mic
                    sd.default.channels = 32  # Set channels of mic
                    recording = sd.rec(int(int(seconds) * fs))  # Get recording in numpy array
                    sd.wait()  # Wait until recording is finished

                    counter = 0
                    while not rospy.is_shutdown():

                        if os.path.isfile('output' + counter + '.wav'):
                            pass
                        else:
                            write(cwd + 'output' + counter + '.wav', fs, recording) # Write numpy array to output.wav (Taken out for now)
                            file_name = 'output' + counter + '.wav'
                            break

                        counter += 1

                    rospy.loginfo("Done recording audio, sending to audio_play.py...")
                    # sd.default.device = 'default'  # Set for output device
                    # sd.default.channels = 32  # Set channels of output device (Usually 32)
                    #
                    # sd.play(recording, fs)  # Play the waveform out the speakers
                    # status = sd.wait()  # Wait for end of waveform

                    publish(file_name, "audio_file")
                elif exitKeyWord.lower() in text.lower():  # Check for exit keyword
                    rospy.loginfo("Exiting microphone...")
                    sys.exit()  # Exit
                else:
                    rospy.loginfo("Google thinks you said '" + r.recognize_google(audio) + "'")  # Normal print transcription

            except sr.UnknownValueError:  # If google cant transcribe the audio
                rospy.loginfo("Google could not understand audio")

            except sr.RequestError as e:  # If something unknown happens
                rospy.loginfo("Google error; {0}".format(e))
