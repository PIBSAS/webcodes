#!/bin/sh
#Tutorial with Sr. Carlos Ca
#https://sites.google.com/view/raspberrypibuenosaires/reconnect-wifi
ping -c3 192.168.0.1

if [ $? -eq 0 ]; then
    echo "ok"
else
    sudo ip link set wlan0 down
    sudo ip link set wlan0 up
fi
