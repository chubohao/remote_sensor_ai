# **Remote Sensor Tag**
**Editor:** Bohao Chu, **Date:** 09.09.2022, **Email:** bohao.chu@qq.com

**Supervisor:**  Fuyin Wei, Fei Xiang, Bernd Noche

## **BASIC**
`git clone --recurse-submodules https://github.com/dexhoui/Sensor-AI.git ./`
> git clone --recurese-submodules = git submodule init && git submodule update

`git submodule update --remote` update submodule from branch.



## **INTRODUCTION**
![Alt text](/assets/arch.png)
### BACKGOURND
There are still many data collection needs in places where WiFi coverage is not available, for example, in suburban pastures, where daily cattle counts through cameras, or in forests, where real-time detection of fires is of high value. Fortunately, most of Germany is already covered by 4G base stations, and we chose to use 4G cellular networks to transmit the sampling data remotely.


### MOTIVATION
Transmitting data in an environment without WiFi has always been a difficult problem. usually, we choose low-frequency networking to build a sensing network, for example, ZigBee, or LoRa. single-point networking can also be realized by means of NB-IOT. But their disadvantages are obvious, that is, their single transmission volume is very small, for example, LoRa can't send data more than 256 bytes in a single time, and the distance between nodes and gateways is also limited and can't be too long. When faced with a large amount of data in real time (e.g., video streaming), data transmission can be performed over the almost ubiquitous 4G cellular network, which not only increases the transmission rate, but also avoids the additional overhead caused by networking.


## **HARDWARE**

![Alt text](/assets/hardware.jpg)

### 硬件模块
- 自定义传感器板子
- [树莓派4B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [ME909S-821AP 4G模块](https://item.taobao.com/item.htm?spm=a230r.1.14.96.7be01c48e9Djc6&id=623513174618&ns=1&abbucket=15#detail)
- [10000MA UPS](https://item.taobao.com/item.htm?spm=2013.1.20141001.2.4cd61af8DzmVZt&id=627042754058&scm=1007.12144.97955.42296_0_0&pvid=26bde26b-6df5-47b3-9480-cfe2321c0848&utparam=%7B%22x_hestia_source%22%3A%2242296%22%2C%22x_object_type%22%3A%22item%22%2C%22x_hestia_subsource%22%3A%22default%22%2C%22x_mt%22%3A0%2C%22x_src%22%3A%2242296%22%2C%22x_pos%22%3A2%2C%22wh_pid%22%3A-1%2C%22x_pvid%22%3A%2226bde26b-6df5-47b3-9480-cfe2321c0848%22%2C%22scm%22%3A%221007.12144.97955.42296_0_0%22%2C%22x_object_id%22%3A627042754058%7D)


### 传感器模块

<table border="1" style="text-align: center;">
    <tr>
        <td><b>Module</b></td>
        <td><b>Model</b></td> 
        <td><b>Protocol</b></td>
        <td><b>Frequency</b></td> 
        <td><b>Channel</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td>Microphone</td>
        <td><a href="https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test">INMP441</a></td> 
        <td>I2S</td> 
        <td>15K</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Motion Processing Unit</td>
        <td><a href="https://invensense.tdk.com/products/motion-tracking/9-axis/mpu-9250/">MPU9250</a></td> 
        <td>I2C</td> 
        <td>1K</td>
        <td>3</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>Laser</td>
        <td><a href="https://www.sparkfun.com/products/14722">VL53L1X</a></td> 
        <td>I2C</td> 
        <td>20</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>EYE</td>
        <td><a href="https://www.sparkfun.com/products/14607">AMG8833</a></td> 
        <td>I2C</td> 
        <td>20</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>BME</td>
        <td><a href="https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/">BME280</a></td> 
        <td>I2C</td> 
        <td>20</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>Camera</td>
        <td><a href="https://www.raspberrypi.com/products/camera-module-v2/">IMX219</a></td> 
        <td>CSI</td> 
        <td>80</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
</table>

### 硬件组装
- 底层：UPS电源
- 二层：4G模块
- 三层：树莓派
- 四层：传感器集群


## **SENSOR TAG**
We need to do some initialization before runing our embedded program and machine learning model.
![CM4 IO Board](assets/images/edge/sensor%20edge.png "CM4 IO Board")

### **BASIC ENVIRONMENT**
We recommend to install the following softwares before starting this section.

[Advance IP Scanner](https://download.radmin.com/download/files/Radmin_3.5.2.1_EN.zip) for getting the IP of ECSK.

[PUTTY](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.77-installer.msi) for connecting the ECSK via SSH. 



We recommend that the following two commands before executing any installation to ensure proper installation of the latest software.

- `sudo apt update`

- `sudo apt upgrade`

Install some common software. Some software requires your confirmation, so type Y when prompted.

- `sudo apt install git vim i2c-tools python3-pip portaudio19-dev libsndfile1`


Downlaod source code.

- `sudo git clone https://github.com/chubohao/remote_sensor_ai.git`

Install some python libraries.
- `sudo pip3 install smbus sparkfun-qwiic serial pyaudio matplotlib librosa tflite-runtime adafruit-python-shell`

### **A. Sensors Driver**
<table border="1" style="text-align: center;">
    <tr>
        <td><b>Module</b></td>
        <td><b>Model</b></td> 
        <td><b>Protocol</b></td>
        <td><b>Frequency</b></td> 
        <td><b>Channel</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td>Microphone</td>
        <td><a href="https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test">INMP441</a></td> 
        <td>I2S</td> 
        <td>15K</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Motion Processing Unit</td>
        <td><a href="https://invensense.tdk.com/products/motion-tracking/9-axis/mpu-9250/">MPU9250</a></td> 
        <td>I2C</td> 
        <td>1K</td>
        <td>3</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>Laser</td>
        <td><a href="https://www.sparkfun.com/products/14722">VL53L1X</a></td> 
        <td>I2C</td> 
        <td>20</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>EYE</td>
        <td><a href="https://www.sparkfun.com/products/14607">AMG8833</a></td> 
        <td>I2C</td> 
        <td>20</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>BME</td>
        <td><a href="https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/">BME280</a></td> 
        <td>I2C</td> 
        <td>20</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
    <tr>
        <td>Camera</td>
        <td><a href="https://www.raspberrypi.com/products/camera-module-v2/">IMX219</a></td> 
        <td>CSI</td> 
        <td>80</td>
        <td>1</td>
        <td>The MPU-9250 is the company’s second generation 9-axis Motion Processing Unit™ for smartphones, tablets, wearable sensors, and other consumer markets.</td>
    </tr>
</table>

#### **A1. Microphone Driver**

**First**, install INMP441 Driver, execute the following commands sequentially in Terminal.
1. `cd ~/remote_sensor_ai/software/edge/tools/ && sudo python3 i2smic.py`
2. Please type y when prompt `"Auto load module at boot"?`
3. Please type y when prompt `"REBOOT NOW? [Y/n]"`
4. Connect it again via ssh.

**Second**, Test the INMP441 Driver.
1. `arecord -l`
- ![CM4 IO Board](/assets/images/edge/arecord.png "CM4 IO Board")

2. `arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -v file.wav`
- ![CM4 IO Board](/assets/images/edge/arecord2.png "CM4 IO Board")

3. `rm file.wav`

4. `python3 ~/edge/source/drivers/micDriver.py`
- ![MIC](/assets/images/edge/mic.png "MIC")

#### **A2. Motion Processing Unit**
![CM4 IO Board](/assets/images/edge/mpu92501.png "CM4 IO Board")

**First**, Open I2C1 interface of CM4.
1. `sudo raspi-config`
2. Select `3 Interface Options` and type *Enter* key.
3. Select `I5 I2C` and type *Enter* key.
4. Select `YES` via *Tab* Key
5. Select `Finish` via *Tab* Key
3. `sudo reboot` and then connect it again via ssh.

**Second**, Check the status of i2c1 and the device mount on it.

1. `i2cdetect -l` to show all i2c interfaces.

- ![CM4 IO Board](/assets/images/edge/i2c1.png "CM4 IO Board")

2. `i2cdetect -y 1` the show all device mount on i2c1 interface, the **0x68** is the address of MPU9250.

- ![CM4 IO Board](/assets/images/edge/i2c2.png "CM4 IO Board")

**Third**, test the driver of MPU9250.

1. `python3 ~/edge/source/drivers/mpuDriver.py`
- ![CM4 IO Board](/assets/images/edge/mpu9250.png "CM4 IO Board")

[Not work for Magnetometer](https://github.com/kriswiner/MPU9250/issues/123)


#### **A3. Laser Distance**
**First**, Open I2C1 interface of CM4.

It has been opened in the above, no need to open it again. If there is no i2c-1, please operate again.

`i2cdetect -l` to show all i2c interfaces.

- ![CM4 IO Board](/assets/images/edge/i2c1.png "CM4 IO Board")

**Second**, Check the status of i2c1 and the device mount on it.
1. `i2cdetect -y 1` the show all device mount on i2c1 interface, the **0x29** is the address of VL53L1X.

- ![CM4 IO Board](/assets/images/edge/vl53l1x.png "CM4 IO Board")


**Third**, test the driver of VL53L1X.

1. `python3 ~/edge/source/drivers/laserDriver.py`

- ![CM4 IO Board](/assets/images/edge/vl53l1x1.png "CM4 IO Board")

#### **A4. EYE**
**First**, Open I2C1 interface of CM4.

It has been opened in the above, no need to open it again. If there is no i2c-1, please operate again.

1. `i2cdetect -l` to show all i2c interfaces.`
- ![CM4 IO Board](/assets/images/edge/i2c1.png "CM4 IO Board")

2. `i2cdetect -y 1` the show all device mount on i2c1 interface, the **0x69** is the address of AMG8833.
- ![CM4 IO Board](/assets/images/edge/eye.png "CM4 IO Board")

**Second**, test the driver of AMG8833.

1. `python3 ~/edge/source/drivers/eyeDriver.py`
- ![CM4 IO Board](/assets/images/edge/eye2.png "CM4 IO Board")

#### **A5. BME**
**First**, Open I2C1 interface of CM4.

It has been opened in the above, no need to open it again. If there is no i2c-1, please operate again.

1. `i2cdetect -l` to show all i2c interfaces.`
- ![CM4 IO Board](/assets/images/edge/i2c1.png "CM4 IO Board")

2. `i2cdetect -y 1` the show all device mount on i2c1 interface, the **0x77** is the address of BME280.
- ![CM4 IO Board](/assets/images/edge/bme.png "CM4 IO Board")

**Second**, test the driver of BME280.

1. `python3 ~/edge/source/drivers/bmeDriver.py`
- ![BME](/assets/images/edge/bme1.png "BME")

#### **A6. Camera**
**First**, Open CSI1 interface of CM4.

1. `sudo vim /boot/config.txt`
2. add `dtoverlay=imx219,cam1` below *# Automatically load overlays for detected cameras*.
- ![](/assets/images/edge/i2c3.png)
3. save it and execut the command `sudo reboot` to reboot the ECSK.

**Second**, Check the status of CSI1.
1. `i2cdetect -l`
- ![](/assets/images/edge/csi.png)

2. `libcamera-hello --list`
- ![](/assets/images/edge/cam1.png)

**Third**, make a picture.
1. `libcamera-jpeg -o test.jpg`
- ![](/assets/images/edge/cam.png)
- ![](/assets/images/edge/test.jpg)

*You can use SFTP software to download the picture from ECCSK, e.g. [FileZilla](https://filezilla-project.org/), the SFTP Port is 22. You can also use other software, e.g. [Pycharm](https://www.jetbrains.com/pycharm/). Here we do not intruduce how to use SFTP, please Google it yourself.*

## **SAMPLING**

In this section, we introduce how to use **ECSK** to sample the raw data for model training. Please ignore this section If you just want to use the sampled raw data or trained models. Because we have already sampled the raw data and trained some models for some scenes, e.g. CNC machine, Office, BOH machine, Logistics Car, so you can use these raw directly to train you model, and then deploy these model on you ECSK.

Here, we strongly recommend [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) to develop edge project, and we do not make too much of the use of Pycharm, please Google it yourself.

### **Download source code to PC**
1. Create a empty folder named ECSK on PC in your perferred location. enter the floder and open the **Git Bash Here** by right click, *(make sure that you have already installed the **git**)*.
- ![git](/assets/images/edge/git.png)

2. `git clone https://github.com/chubohao/edge-computing-sensor-kit.git ./` please ignore thie step if you have already downloaded it.
- ![git](/assets/images/edge/git1.png)

3. Use pycharm to open its subfolder *"ecsk/software/edge/"*
- ![pycharm](/assets/images/edge/pycharm.png)

4. Make the configuration for deployment.
- Tools-> Deployment-> Configuration

- ![pycharm](/assets/images/edge/pycharm1.png)
- Click "**+**", and select SFTP, and input the alias, here I inputted "**edge**".
- ![pycharm](/assets/images/edge/pycharm2.png)
- SSH configuration
- ![pycharm](/assets/images/edge/pycharm3.png)
- Input the *host ip*, *username*, and *password* of ECSK, and test connnection.
- ![pycharm](/assets/images/edge/pycharm4.png)
- In **Connection** page, click **Autodetect**.
- ![pycharm](/assets/images/edge/pycharm5.png)
- In **Mappings** page, input */edge* to Deployment path.
- ![pycharm](/assets/images/edge/pycharm6.png)
- Finally, select **Automatic Upload(Always)**, then your code will automatically upload to ECSK after the code is changed.
- ![pycharm](/assets/images/edge/pycharm7.png)
- Open SSH tools of Pycharm/.
- ![pycharm](/assets/images/edge/pycharm8.png)
- Then you can use it to control your ECSK instead of PuTTY.
- ![pycharm](/assets/images/edge/pycharm9.png)


5. Config the scene information in the file of **source/arguments.py**, you should change the variable **dataset**, **activity**, and **duration** according your scenes.
- ![pycharm](/assets/images/edge/sampling1.png)

6. Execute the sampling program, please make sure the activity is taking place in your scenario.
- `python3 ~/edge/source/sampling/sampling.py`
- ![pycharm](/assets/images/edge/pycharm10.png)

7. Download the data from ECSK for the next training.
- Tools-> Deployment-> Browse Remote Host
- ![pycharm](/assets/images/edge/pycharm11.png)
- In the ECSK, select the folder dataset, and downlaod form here.
- ![pycharm](/assets/images/edge/pycharm12.png)
- Then you can find them in you PC.
- ![pycharm](/assets/images/edge/pycharm13.png)


## WARNING
> ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround21
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround21
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround40
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround41
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround50
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround51
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround71
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.iec958
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.iec958
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.simple-card.pcm.hdmi.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4745:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5233:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM hdmi
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.simple-card.pcm.hdmi.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4745:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5233:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM hdmi
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2660:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline

`sudo cp ~/edge/tools/alsa.conf /usr/share/alsa/`

## **4G Modules**
1. `sudo apt install libmbim-utils ppp -y`
2. `sudo vim /etc/mbim-network.conf`

> APN=internet
> APN_USER=
> APN_PASS=
> APN_AUTH=
>PROXY=yes

4. `sudo mbim-network /dev/cdc-wdm0 start`
![Alt text](/assets/images/4G.png)

6. `ifconfig`
![Alt text](/assets/images/4G1.png)

## **PCB**
![Alt text](/assets/top.png)
![Alt text](/assets/bottom.png)