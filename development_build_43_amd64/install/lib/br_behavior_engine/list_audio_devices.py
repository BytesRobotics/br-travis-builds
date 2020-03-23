#!/usr/bin/env python2

import sounddevice as sd

print(sd.query_devices())

print("---------------------------------------------------------------------")
print("This is a list of all audio devices on your computer.")
print("The microphone will have iTalk in the name.")
print("The speaker will have [INSERT NAME HERE] in the name.")
print("Also take note of number of channels available for each.")
print("A star will be next to the selected audio device for the system.")
print("The ros params for the speaker are [speaker] and [speaker_channels]")
print("No ros param for microphones yet. Defaults for speaker are 5 and 32.")
print("---------------------------------------------------------------------\n")

