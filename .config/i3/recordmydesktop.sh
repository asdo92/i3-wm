#!/bin/bash

mkdir -p ~/Recordings
cd ~/Recordings
echo "# RecordMyDesktop"
echo "# The files will save in ~/Recordings"
echo ""
kitty -T "recordmydesktop" -e "recordmydesktop"
