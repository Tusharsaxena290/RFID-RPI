# RFID-RPI
<br/>


## What is RFID?
<br/>
Radio-frequency identification uses electromagnetic fields to automatically identify and track tags attached to objects. An RFID system consists of a tiny radio transponder; a radio receiver and transmitter.
<br/>

![rfid](https://user-images.githubusercontent.com/53862641/103856926-7d966400-50db-11eb-8b63-82ff685edaa5.jpg)
<br/>



## A conventional RFID system is made up of three components:
- RFID reader.
- RFID antenna.
- RFID transponder (or tag) electronically programmed with unique data.
<br/>




## RFID modules used:
- **EM18 MODULE:** EM18 RFID Reader is a module which reads the ID information stored in RFID TAGS. This ID information is unique for every TAG which cannot be copied.
<br/>


![em18](https://user-images.githubusercontent.com/53862641/103857900-5ccf0e00-50dd-11eb-9f1c-6c5eb30d6931.jpg)
<br/>




- **MRC522 MODULE:** The RC522 is a 13.56MHz RFID module that is based on the MFRC522 controller from NXP semiconductors. The module can supports I2C, SPI and UART and normally is shipped with a RFID card and key fob. 
<br/>



![rc522](https://user-images.githubusercontent.com/53862641/103857925-6a849380-50dd-11eb-9555-79b65ffaab25.png)
<br/>





## Working with EM18 module
<br/>

### Enabling serial from Raspi-config:
1.  Open terminal and perform the command stated below
``` bash
sudo raspi-config
```
<br/>

<img width="300" alt="sudo1" src="https://user-images.githubusercontent.com/53862641/103859237-bafcf080-50df-11eb-9b3a-82758c2efa27.png">
<br/>



2.  Click interface options.
<br/>


<img width="305" alt="interface" src="https://user-images.githubusercontent.com/53862641/103859513-2c3ca380-50e0-11eb-9a2c-85c93a5d4776.png">
<br/>


3. Click Serial Port.
<br/>

<img width="303" alt="serial port" src="https://user-images.githubusercontent.com/53862641/103859677-7756b680-50e0-11eb-9c5b-f1fba8eefbfb.png">
<br/>

4.  Click no when it is asked that **WOULD YOU LIKE A LOGIN SHELL TO BE ACCESSIBLE OVER SERIAL?**.
<br/>

5. Click yes when it is asked that **WOULD YOU LIKE THE SERIAL PORT HARDWARE TO BE ENABLED?**
<br/>

6. Perform reboot using the command stated below
``` bash
sudo reboot
```
<br/>
<br/>

## Perform the connection
<br/>
1.TX of EM18 to RX of Raspberry pi<br/>
2.vcc to 5v<br/>
3.GND of EM18 to GND of raspberry pi<br/>

<br/>
<img width="464" alt="em18image" src="https://user-images.githubusercontent.com/53862641/103861113-e2a18800-50e2-11eb-8d83-97f7c0ee82f2.png">

<br/>
<br/>

##### Run the code stored in the EM18 rfid code.py file.
<br/>
<br/>


## Working with RC522 Module
<br/>
### Enabling SPI from raspi-config
1. Execute the command stated below on the terminal:
``` bash
sudo raspi-config
```
<br/>
2. Click interface options.
<br/>
<img width="305" alt="interface" src="https://user-images.githubusercontent.com/53862641/103867291-1b465f00-50ed-11eb-9c29-ad4507598f7d.png">
<br/>
3. Click SPI
<br/>
<img width="293" alt="spi" src="https://user-images.githubusercontent.com/53862641/103867374-3c0eb480-50ed-11eb-9d5a-6251cae9c710.png">
<br/>
4. Press Yes, When asked **WOULD YOU LIKE TO ENABLE SPI INTERFACE**
<br/>
5. Perform the reboot using the command stated below:
``` bash
sudo reboot
```
<br/>
<br/>

### Install **SPIDEV**
<br/>
1. Open the terminal and execute the command stated below:
``` bash
sudo pip3 install spidev
```
<br/>
<img width="580" alt="spidev" src="https://user-images.githubusercontent.com/53862641/103868008-48dfd800-50ee-11eb-9dde-3517b5afb661.png">
<br/>
<br/>

### Install **MFRC522**
<br/>
1. Open the terminal and execute the command stated below:
``` bash
sudo pip3 install mfrc522
```
<br/>
<img width="572" alt="rc522ter" src="https://user-images.githubusercontent.com/53862641/103868180-8c3a4680-50ee-11eb-945e-9eb584731b89.png">
<br/>
<br/>

### Perform the connections
<br/>
<img width="415" alt="rc522connection" src="https://user-images.githubusercontent.com/53862641/103868544-066acb00-50ef-11eb-8cd7-e28759e3b7c4.png">
<br/>
<br/>
### Run the codes stored in the rc522 folder.
<br/>
<br/>
**NOTE UNLIKE EM18, IN RC522 WE CAN STORE THE RFID CODES BY RUNNING THE CODE STORE IN THE RC522 READ FILE, BY JUST BRINGING THE TAG NEAR THE READER.













