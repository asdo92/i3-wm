#!/bin/bash

status_bar=0

while [ ${status_bar} -eq 0 ] ; do
  updates=$(~/.config/i3/scripts/checkUpdates.sh)
  kernel=$(~/.config/i3/scripts/kernel_version.sh)
  cpuinfo=$(~/.config/i3/scripts/cpu_info.sh)
  meminfo=$(~/.config/i3/scripts/mem_info.sh)
  volume=$(~/.config/i3/scripts/get_volume.sh)
  lang=$(~/.config/i3/scripts/get_lang.sh)
  battery=$(~/.config/i3/scripts/battery.sh)
  date=$(~/.config/i3/scripts/current_date.sh)
  echo "${updates} ${kernel} ${cpuinfo} ${meminfo} ${volume} ${lang} ${battery} ${date}"
  sleep 2
done
