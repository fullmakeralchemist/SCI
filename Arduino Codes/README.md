<h1>Arduino Folder </h1>

[Documentation Arduino](https://www.arduino.cc/en/Guide/Introduction)

## What is Arduino?
Arduino is an open platform of hardware software, community, microcontroller, project company designed to be used in a simple way by anyone. we are going to learn to create solutions to problems that we have every day, the Arduino are cheap and we can get them easily, it is multiplatform. The programming environment is simple, it is one of the largest open source projects in the world. If I use other forms of communication permitting, there are many community projects. It is based on microcontrollers ATmega328P, we can design our own cards. an arduino to your measure and needs.

[Where to buy it](https://store-usa.arduino.cc/)

## What you will need 

* A computer 
* A selection of electronics components, such as a LED with appropriate resistor and servomotor
* The Arduino IDE
* Google Chrome

## Content 

* What is  Arduino
* Microcontroller
* Arduino IDE
  * Variables
  * Librarys
* Excercises
  * LED (if)
  * LED RGB (for)
  * Sensors
* Actuators
  * Servo
  * Servo (for)
* Raspberry PI PICO
  * Raspberry PI PICO (LED)
  * Raspberry PI PICO (Sensor temp)
  * Raspberry PI PICO (Sensor analog and write)

## Configurate

Install the [Arduino IDE](https://www.arduino.cc/en/software)

## Platforms to use 

* [Thinkercad](https://www.tinkercad.com/)
* [Fritzing](https://fritzing.org/)

## Microcontroller

Integrated circuit capable of executing instructions sequentially whose purpose is to control or automate some process.

Part of  Microcontroller: 
* Memory where we will store the input and output peripheral code
* Processing unit #Execute instructions
* I/O ports pins

### Difference Between Microcontroller and Microprocessor
Arduino is basically a microcontroller while Raspberry Pi is a minicomputer. A microcontroller is one of the parts that a computer contains, so, in theory, we can only do some of the different functions that we can do with a computer.

Arduino is specially designed to carry out different electronic projects. We can connect many components and sensors to the connectors on the board. This makes it easy to perform simple tasks that do not require complex programming. In this field it can be more efficient than the Raspberry Pi.

The Arduino board performs the task for which it has been programmed once it is connected to power, without having to boot any operating system. It is faster for performing basic functions.

In addition, it includes a simple firmware that allows us to connect to it through the USB port. This allows us to access the board and load the necessary code. From there, the board will perform its task without the need for us to use a keyboard or mouse, we just have to plug it in.

Raspberry Pi requires an operating system in order to function. There are different ones based on Linux and they are installed on an SD card. Depending on the use that we are going to give them, we will use one.

In the Raspberry Pi we have different connections to the internet. It has a Wi-Fi port and an Ethernet connection. (Detail more elements.

Explain cases for use of Raspberry.

However, if we want to do a simpler project, like turning on a light, with Arduino we can do it more quickly and easily, with minimal programming, while with Raspberry we could do it, but making the task more complicated.

## Arduino Software (IDE)
El entorno de desarrollo integrado Arduino, o software Arduino (IDE), contiene un editor de texto para escribir código, un área de mensajes, una consola de texto, una barra de herramientas con botones para funciones comunes y una serie de menús. Se conecta al hardware Arduino para cargar programas y comunicarse con ellos.


## Variables


* char, se utilizan para almacenar caracteres, ocupan un byte.
byte, pueden almacenar un número entre 0 y 255.
* int, ocupan 2 bytes (16 bits), y por lo tanto almacenan número entre 2-15 y 215-1, es decir, entre -32,768 y 32,767.
* unsigned int, ocupa trambién 2 bytes, pero al no tener signo puede tomar valores entre 0 y 216-1, es decir entre 0 y 65,535.
* long, ocupa 32 bits (4 bytes), desde -2,147,483,648 a 2,147,483,647.
unsigned long.
*float, son números decimales que ocupan 32 bits (4 bytes). Pueden tomar valores entre -3.4028235E+38 y +3.4028235E+38.
* double, también almacena números decimales, pero disponen de 8-bytes (64 bit).


```
char miCaracter='a'; //declaramos una variable tipo char, llamada miCarcater y la inicializamos con valor a valores para ciertos protocolos
byte unNumero = 189; // variable tipo byte inicializada a 189 de 0 a 255
int unEntero; //variable tipo int sin inicializar
unsigned int numeroPositivo = 2343; //entero positivo inicializada
float numDecimal = 12.212; //numero decimal inicializado a 12,212
```