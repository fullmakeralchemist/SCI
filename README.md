<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the tinyml-mapping-backlight and create a pull request or simply open
*** an issue with the tag "suggest".
*** Thanks again! Now go create something AMAZING! :D
***
***
*** 
-->

<!--#     The TensorFlow Microcontroller Challenge    -->
   <h1>🏆 AI as a tool to achieve sustainable development. 🏆</h1>
   <h2>🏆 AI as a tool to achieve sustainable development. 🏆</h2>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/fullmakeralchemist/tinyml-mapping-backlight">
    <img src="assets/logo.png" alt="Logo" width="720">
  </a>
  <br />
</p>
<br />

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Club](#about-the-project)
  * [Motivation](#motivation)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [What's next for Tiny ML in Mapping Dance, Visual Arts and interactive museums](##whats-next-after-club)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
* [Information resources](#information-resources)

<!-- ABOUT THE PROJECT -->
## About The Club

<!-- [![Tiny ML in Mapping Dance](https://i9.ytimg.com/vi/3YUVTDTo-Zk/mq1.jpg?sqp=CNTs2IcG&rs=AOn4CLBiPsvQ2bGNVZvn_j-nJXj8d81hLA)](https://www.youtube.com/watch?v=3YUVTDTo-Zk) -->


Currently we have all witnessed the changes in the environment, technology cannot solve everything at the moment, but with the open source tools that currently exist we can get an idea of what is happening. Currently, Data Science and Machine Learning can help us create evidence to put current problems on the table and start developing projects that could solve or improve some of them. Python is currently one of the most important tools for data science. The IoT, the maker culture and DIY can help us obtain variables, create prototypes for the different situations or projects that are required. In this course we will see the tools and techniques to create databases with different types of sensors and how to connect them to the Arduino, how and when to use them, later we will be able to analyze and create predictive models with data from the environment, we will know the different algorithms that exist, the advantages they have and we will learn to evaluate and adjust them to have better results.


### Motivation

Some facts:

- There are a lot of new projects adding technology nowadays.
- Factors like the difficulties that students come up with during their attempts to familiarize with new technologies, so that they can integrate them in their projects.
- High cost of buying and installing new software together with its supporting systems.
- Limited access that a large percentage of the student population has to new technologies made it sometimes 

### Built With

With a lot of love 💖, motivation to help others 💪🏼 and [Python](https://www.python.org/) 🐍, using:

* [Google Colab](https://colab.research.google.com/) <img src="https://colab.research.google.com/img/favicon.ico" width="15"> (with its wonderful GPUs)
* A [Raspberry Pi](https://www.raspberrypi.org/) 4 <img src="https://www.raspberrypi.org/homepage-9df4b/favicon.png" width="15">
* A [Arduino Nano 33 BLE SENSE](https://store.arduino.cc/usa/nano-33-ble-sense)
* A [NodeMCU ESP8266](https://nodemcu.readthedocs.io/en/release/) board
* Arduino IDE
* ESP8266 Board [Package](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide)


<!-- GETTING STARTED -->
## Getting Started

Go to the folders [Python Codes](https://github.com/fullmakeralchemist/SCI/tree/'main'/Python%20Codes)


### Prerequisites

* Have a computer
* Arithmetic (Basic math knowledge)
* Computer
* Google Account
* Google Chrome

<!--
This is an example of how to list things you need to use the software and how to install them. 

For this particular section I will suppose that you already have a Raspberry Pi already setup. If not I have a guide in Medium about [Getting started on Raspberry Pi 4](https://fullmakeralchemist.medium.com/setting-up-your-raspberry-pi-4-wireless-f51c16937d1e). Also you will need git installed on your system. If not, I have a guide posted on [Medium](https://fullmakeralchemist.medium.com/install-git-and-visual-studio-code-on-raspberry-pi-48d054fdee07) to do it .

Before installing the libraries in Raspberry Pi run the following code lines in the Raspberry Pi terminal:

```
sudo apt update
sudo apt upgrade
```
-->

<!--
After updating and upgrading we will write the following command:

```
sudo pip3 install python-vlc
```

To install the Mosquitto Broker enter these next commands:

```
pi@raspberry:~ $ sudo apt install -y mosquitto mosquitto-clients
```

You’ll have to type Y and press Enter to confirm the installation. To make Mosquitto auto start on boot up enter:

```
pi@raspberry:~ $ sudo systemctl enable mosquitto.service
```
```
pi@raspberry:~ $  mosquitto -v
```
This returns the Mosquitto version that is currently running in your Raspberry Pi. It should be 1.5.X or above.

<center>
<img src="assets/mosquittov.png" width="60%">
</center>

#### Raspberry Pi IP Address & Paho Package

To use Mosquitto broker later on your projects, you’ll need your Raspberry Pi IP address. To retrieve your Raspberry Pi IP address, type the next command in your Terminal window:
```
pi@raspberry:~ $ hostname -I
```
<center>
<img src="assets/iprasp.png" width="60%">
</center>

The Paho package provides a client class which enables applications to connect to an MQTT broker to publish messages, and to subscribe to topics and receive published messages. In this project, the Python script is going to publish messages to the ESP8266 to turn the GPIOs on and off to control the lights.
To install paho-mqtt run the following command:

```
sudo pip install paho-mqtt
```

And those are the steps that we will follow to set up our Raspberry Pi. In any case, this specific setup can be seen in the corresponding [Raspberry_Script](https://github.com/fullmakeralchemist/tinyml-mapping-backlight/tree/master/Raspberry_Script) folder.

Now lets see the setup for the Arduino IDE


#### Setup Arduino IDE

To install the ESP8266 Board Package enter:

```
http://arduino.esp8266.com/stable/package_esp8266com_index.json
```
Into Additional Board Manager URLs field in the Arduino v1.6.4+ preferences.

<center>
<img src="assets/boardurl.png" width="60%">
</center>

Next, use the Board manager to install the ESP8266 package.

<center>
<img src="assets/boardmanager.png" width="60%">
</center>

After the install process, you should see that esp8266 package is marked INSTALLED. Close the Boards Manager window once the install process has completed.

Setup ESP8266 Support When you've restarted, select Adafruit Feather HUZZAH ESP8266  from the Tools->Board dropdown.

<center>
<img src="assets/dropdown.png" width="60%">
</center>

#### Getting the MQTT library for the ESP8266
For the ESP8266 to interact with the Raspberry Pi web server, you need to install the PubSubClient [library](https://github.com/knolleary/pubsubclient). This library provides a client for doing simple publish/subscribe messaging with a server that supports MQTT (basically allows your ESP8266 to talk with a Python web server).

##### Installing the Library
1. [Click here to download the PubSubClient library](https://github.com/knolleary/pubsubclient/archive/master.zip). You should have a .zip folder in your Downloads folder
2. Unzip the .zip folder and you should get pubsubclient-master folder
3. Rename your folder from pubsubclient-master to pubsubclient
4. Move the pubsubclient folder to your Arduino IDE installation libraries folder
5. Then, re-open your Arduino IDE

The library comes with a number of example sketches. See File > Examples > PubSubClient within the Arduino IDE software.

Finally, you can upload the full [sketch](https://github.com/fullmakeralchemist/tinyml-mapping-backlight/tree/master/ESP8266_Sketches/lightsmqtt) to your ESP8266 (replace with your SSID, password and RPi IP address **see the comments in the sketch**):

### Run the script


Clone the tinyml-mapping-backlight repo, download it or just copy and paste from the files from this repo:
bash
```
git clone https://github.com/fullmakeralchemist/tinyml-mapping-backlight
```

The simplest way is just using the Thonny IDE which is included with Raspberry Pi OS, Thonny comes with Python 3.6 built in, so you don’t need to install anything. Just open up the program, which you’ll find under Menu > Programming. It offers a lot of advanced features not currently available in the Python 3 (IDLE) program. Also you can follow my guide to install Visual Studio Code, but some libraries show some errors trying to run the script. So I recommend you to use the Thonny IDE.

<center>
<img src="assets/run.png" width="60%">
</center>
-->


## What's next after club

- Develop own embedded device for the model deployment (which should already include a accelerometer, gyroscope and a wifi connection)
- Improve user data acquisition through the accelerometer and gyroscope.
- Add Bluetooth recording of accelerometer and gyroscope (you can find a file using python as a receiver of the information and the INO file that sends the data through the BLE library).
- Implement in a dance presentation or a museum (also in my house in holidays)
- Add kinetic sculptures with servo motors to add an effect like the matilda movie.
- Test prototype with a dancer.
- Add the MadMapper API to add more visual effects with the animations.


## License


<!-- CONTACT -->
## Contact

Eduardo Padron - [@makeralchemist](https://twitter.com/makeralchemist) - 
Eduardo Padron - [@fullmakeralchemist](www.linkedin.com/in/fullmakeralchemist
)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* Icons made by [Flat Icons](https://www.flaticon.com/authors/flat-icons) from [www.flaticon.com](https://www.flaticon.com/)
* Images and gifs made by [Canva](https://www.canva.com/) 

<!-- Information resources -->
## Information resources