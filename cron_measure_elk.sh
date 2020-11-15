#!/bin/sh
bash $HOME/IOT/IOT-air-quality/Tools/connect_vpn.sh &
PID=$!
sleep 10
python $HOME/IOT/IOT-air-quality/ELK/upload_measure_elk.py
sudo kill -9 $PID
exit 0