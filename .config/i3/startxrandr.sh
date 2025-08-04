#!/bin/bash

sleep 2

# Configuration for your monitor(s). Use xrandr and/or lxrandr for help
# First monitor
xrandr --output HDMI-A-0 --mode 1920x1080 -r 74.97
# Second monitor
xrandr --output HDMI-A-1 --mode 1280x1024 -r 75.02 --rotate left --right-of HDMI-A-0
