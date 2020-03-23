#!/usr/bin/env python2
import os

os.system("gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1280,height=720,framerate=15/1' ! nvvidconv flip-method=2 ! tee name=t1 t1. ! queue silent=true ! nvv4l2h264enc bitrate=8000000 ! h264parse config-interval=1 ! queue silent=true leaky=downstream ! rndbuffersize max=65000 ! udpsink host=127.0.0.1 port=5001 sync=false t1. ! queue silent=true ! nvjpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000 sync=false")
