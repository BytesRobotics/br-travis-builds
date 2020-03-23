#!/bin/bash

echo "Make sure you are running this from within the scripts directory!"
sudo cp ../config/camera_overrides.isp /var/nvidia/nvcam/settings/
sudo chmod 664 /var/nvidia/nvcam/settings/camera_overrides.isp
sudo chown root:root /var/nvidia/nvcam/settings/camera_overrides.isp
echo "Complete!"
