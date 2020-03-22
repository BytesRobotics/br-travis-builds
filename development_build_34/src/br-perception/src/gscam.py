#!/usr/bin/env python
import os

os.system("gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1280,height=720,framerate=15/1' ! nvvidconv flip-method=2 ! nvjpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000")
