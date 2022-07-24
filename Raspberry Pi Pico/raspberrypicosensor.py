from machine import ADC
from time import sleep_ms

#Set up the ADC port using the chanel number
#Set convert factor for ADC output to Voltage
port = ADC(27)
conversion_factor = 3.3 / (65535)

#Change this value depending on your board
offset = 0.279 ;

#Set board led
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(0)

doc = open("sensor_data.txt", "w")

while True:
    lectura = round((str(port.read_u16())), 2)
    voltage = (str(port.read_u16() * conversion_factor))
    format_voltage = "{:.2f}".format(float(voltage))
    presion = (str(((float(voltage) - offset) * 250))) #Calculate water pressure
    format_presion = "{:.2f}".format(float(presion))
    
    doc.write(lectura + " ")
    doc.write(voltage + " ")
    doc.write(presion + " \n")
    
    print("ADC: ", lectura)
    print("Voltage: ", voltage, " V")
    print("Formato Voltage: ",format_voltage, " V")
    print("Presion: ", presion, " KPa")
    print("Formato Presion: ",format_presion, " KPa")
    
    
    led_onboard.value(1)
    sleep_ms(1000)
    led_onboard.value(0)
    sleep_ms(1000) 
