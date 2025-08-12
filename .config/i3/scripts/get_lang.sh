#!/bin/bash

if [ -f /usr/bin/setxkbmap ] ; then
  get_lang=$(setxkbmap -query 2> /dev/null | grep "layout:" | tr -s " " | cut -d ":" -f 2)
  if [ -z ${get_lang} ] ; then
    echo "  us "
  else
    echo " ${get_lang} "
  fi
else
  echo "  us "
fi 

