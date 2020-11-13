# Connect to a SSL VPN

Install OpenConenct

```bash
sudo apt-get install openconnect
```
You need to declare your password as env variable or modify the script to retrieve them as argument

```bash
export VPN_USER=<YOUR_USERNAME>
export VPN_PASSWORD=<YOUR_PASSWORD>
```

Run the following command

```bash
./connect_vpn.sh
```
> os=win option was necessary to register to sucessfully login to the VPN

You should then be able to ping a machine in this network

```bash
ping YOUR_IP
```