# Connect to a SSL VPN

## Install OpenConenct

```bash
sudo apt-get install openconnect
```
You need to declare your password as env variable or modify the script to retrieve them as argument

```bash
export VPN_USER=<YOUR_USERNAME>
export VPN_PASSWORD=<YOUR_PASSWORD>
```

> If you can generate a SSL key, should be far more secure 😅 

## Test your VPN connection

```bash
./connect_vpn.sh
```
> os=win option was necessary to register to sucessfully login to the VPN

You should then be able to ping a machine in this network

```bash
ping YOUR_IP
```

## Automate the process

- In case you want to store permanently your credentials as env variable (quite unsafe), you can proceed as follow

    ```bash
    cd
    nano ./.bashrc
    ```
    
    Add the following lines at the end of the file
    
    ```bash
    export VPN_USER='<YOUR_USER_NAME>'
    export VPN_PASSWORD='<YOUR_PASSWORD>'
    ```

- Otherwise you can write your password directly in the script (hard-coded) 😅

