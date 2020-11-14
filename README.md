# IOT-air-quality 

This project aims at creating a portable device that allows you to monitor air quality.

1. [Requirements 📜](<#Requirements 📜>)
1. [Getting started 🚦](<#Getting started 🚦>)
1. [Automate with crontab 🤖](<#Automate with crontab 🤖>)

## Requirements 📜
- Raspberry pi (3B model used)
- DHT11 sensor (3 pins model)
- 3 wires

## Getting started 🚦

Setup the project by following these steps

```bash
cd                          # go at your home directory
mkdir IOT && cd ./IOT       # create IOT directory and enter in it
git clone https://github.com/aballiet/IOT-air-quality.git
```

1. **[Setup your DHT11 sensor](./DHT11/README.md)**
1. **[Setup a single ELK node](./ELK/README.md)**

## Automate with crontab 🤖
Once everything is setup, you can automate the uploading/measuring task thanks to crontab.

```bash
crontab -e
```

Then add the following line
> Be careful if your username is different (here `pi`)
```bash
*/1 * * * * bash /home/pi/IOT/IOT-air-quality/cron_measure.sh
```

This specific part at the beginning : `*/1 * * * *` defines the refresh rate of the script. It corresponds to a measure/upload **each minute**. See [this](https://crontab.guru/) link to help you write your refresh rate.