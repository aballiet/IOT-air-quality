# Use a BOSCH sensor BME680 with your ESP8266

*You can find this chip (BME680) for around 5€ on marketplaces such as Aliexpress.*

> The BME680 is the first gas sensor that integrates high-linearity and high-accuracy gas, pressure, humidity and temperature sensors. In order to measure air quality for personal wellbeing the gas sensor within the BME680 can detect a broad range of gases such as volatile organic compounds (VOC). [see more](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors-bme680/)

**In order to compute IAQ, we will use the [BOSCH library](https://github.com/BoschSensortec/BSEC-Arduino-library).**

# Wiring your sensor

In this guide we will use the BME680 with the I2C protocol as it only requires 4 wires see: [Wiring-Diagram-I2C](./images/Wiring-Diagram-I2C.png)

> It is probably good to solder the chip to avoid further problems.

# Testing the sensor

As I encountered several problems while trying to use this library, we should first test the sensor to make sure it is working

1. Flash and run on your ESP8266, the [I2C_Scanner.ino](./I2C_Scanner/I2C_Scanner.ino)
    - Open the serial monitor with the frequency : 115200 bauds
    - You should see the message : 
    
        ```bash
        Scanning...
        I2C device found at address 0x77 # this address can be either 0x76 or 0x77 !!!
        done
        ```

    > Depending on the address value we will have to **configure the BOSCH Library differently !**

1. Flash and run on your ESP8266, the [Test_BME680.ino](./Test_BME680/Test_BME680.ino)

    > You may require to install the `Adafruit Sensor` & `Adafruit BME680 Libraries`. You can proceed as the installation for the BOSCH library explained below.

    - Open the serial monitor with the frequency : 115200 bauds
    - You should see a similar message :       
        ``` python
        Reading started at 126823 and will finish at 127005
        You can do other work during BME680 measurement.
        Reading completed at 127139
        Temperature = 30.27 *C
        Pressure = 1002.13 hPa
        Humidity = 24.74 %
        Gas = 328.68 KOhms
        Approx. Altitude = 93.16 m
        ```

# Installing and using BOSCH library

You can install it by using the Arduino Library Manager :

- Go to Sketch -> Include a Library -> Manage Libraries
- Search for `bsec`
- Install it

![bsec](./images/install_library.png)

- Open the [BOSCH-BSEC-test.ino](./BOSCH-BSEC-test/BOSCH-BSEC-test.ino) with your favorite editor

    - If you had an **address** = **0x76**, make sure that 18th line of the file is as follow : 
        ```c
        iaqSensor.begin(BME680_I2C_ADDR_PRIMARY, Wire);
        ```

    - If you had an **address** = **0x77**, make sure that 18th line of the file is as follow : 
        ```c
        iaqSensor.begin(BME680_I2C_ADDR_SECONDARY, Wire);
        ```
 
- Flash and run on your ESP8266
- Open the serial monitor with the frequency : 115200 bauds
- You should see a similar message:
    
    ```bash
    BSEC library version 1.4.6.0
    BSEC warning code : 10
    Timestamp [ms], raw temperature [°C], pressure [hPa], raw relative humidity [%], gas [Ohm], IAQ, IAQ accuracy, temperature [°C], relative humidity [%], Static IAQ, CO2 equivalent, breath VOC equivalent
    98, 25.36, 99673.00, 28.73, 287150.00, 25.00, 0, 25.36, 28.73, 25.00, 400.00, 0.50
    ```

In order to be able to exploit full features of the BME680 and avoid the `Error Code : 10`, we will need to edit the `platform.txt` in `C:\Users\YOUR_USERNAME\AppData\Local\Arduino15\packages\esp8266\hardware\esp8266\YOUR_VERSION` as explained in the [Bosch Tutorial](https://github.com/BoschSensortec/BSEC-Arduino-library) :

## Modify the platform.txt file

If you have already used the previous example code and hack guide, remove the linker flag `-libalgobsec` in the platform.txt file and reference to the `compiler.c.elf.extra_flags`.

The standard arduino-builder now passes the linker flags under `compiler.libraries.ldflags`. Most platform.txt files do not already include this new optional variable. You will hence need to declare this variable's default and add it to the end of the combine recipe. It is recommended to declare it in the following section like below,

```
# These can be overridden in platform.local.txt
compiler.c.extra_flags=
compiler.c.elf.extra_flags=
#compiler.c.elf.extra_flags=-v
compiler.cpp.extra_flags=
compiler.S.extra_flags=
compiler.ar.extra_flags=
compiler.elf2hex.extra_flags=
compiler.libraries.ldflags=
```

and add it in the combine recipe like the below examples

#### ESP8266 community forum's ESP8266 core

Original line [105](https://github.com/esp8266/Arduino/blob/68ee1216454eeea49dd3452c6ff21bc748f397b6/platform.txt#L105),

```
## Combine gc-sections, archives, and objects
recipe.c.combine.pattern="{compiler.path}{compiler.c.elf.cmd}" {build.exception_flags} -Wl,-Map "-Wl,{build.path}/{build.project_name}.map" {compiler.c.elf.flags} {compiler.c.elf.extra_flags} -o "{build.path}/{build.project_name}.elf" -Wl,--start-group {object_files} "{archive_file_path}" {compiler.c.elf.libs} -Wl,--end-group  "-L{build.path}"
```

should become

```
## Combine gc-sections, archives, and objects
recipe.c.combine.pattern="{compiler.path}{compiler.c.elf.cmd}" {build.exception_flags} -Wl,-Map "-Wl,{build.path}/{build.project_name}.map" {compiler.c.elf.flags} {compiler.c.elf.extra_flags} -o "{build.path}/{build.project_name}.elf" -Wl,--start-group {object_files} "{archive_file_path}" {compiler.c.elf.libs} {compiler.libraries.ldflags} -Wl,--end-group  "-L{build.path}"
```



