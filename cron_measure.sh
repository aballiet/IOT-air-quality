#!/bin/sh
bash /home/pi/IOT/IOT-air-quality/Tools/connect_vpn.sh &
PID=$!
sleep 5
python /home/pi/IOT/IOT-air-quality/ELK/upload_measure.py
sudo kill -9 $PID
exit 0