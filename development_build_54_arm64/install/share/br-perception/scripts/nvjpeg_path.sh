#!/bin/bash

sudo rm /usr/lib/aarch64-linux-gnu/tegra/libnvjpeg.so
sudo cp ~/Github/br-core/catkin_ws/src/br-perception/scripts/libnvjpeg.so /usr/lib/aarch64-linux-gnu/tegra/
