#!/bin/bash

# Reload i3
i3-msg reload

# Load screen configuration
sleep 1
~/.config/i3/startxrandr.sh
