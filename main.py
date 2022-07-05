from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(26))
while True:
    Bit= adc.read_u16()
    V = Bit*3.3/65535
    T = V*(1/0.01)
    print("{:.2f}".format (T))
    sleep (1)
