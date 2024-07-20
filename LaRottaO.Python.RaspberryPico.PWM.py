#Uses MicroPython
#Raspberry Pi Pico RP2040

from machine import Pin, PWM, ADC
from time import sleep

# Setup PWM on GP15 (PIN 20)
pwm = PWM(Pin(15))

adc_freq = ADC(26)  # PIN 31 Potentiometer for frequency control
adc_duty = ADC(27)  # PIN 32 Potentiometer for duty cycle control

while True:
  
    freq_value = adc_freq.read_u16() 
    duty_value = adc_duty.read_u16()  
   
    freq = int(5+(freq_value / 65535) * (1000 - 10))
    duty = int((duty_value / 65535) * (100 - 0))  
    
    if(freq<10):
        freq = 10
    
    pwm.freq(freq)
    pwm.duty_u16(duty_value)
    
    sleep(0.01)