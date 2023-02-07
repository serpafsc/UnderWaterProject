import spidev
from time import sleep
import RPi.GPIO as GPIO

# Set spi bus
bus = 0
device = 0
spi = spidev.SpiDev()
spi.no_cs
spi.open(bus, device)
spi.max_speed_hz = 100000

#Set chip selection
pin = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)


#16-bit data to be sent
data = 0b1000000000000000
#Raise chip selection signal (normally True)
GPIO.output(pin, True)

while True:
    #Split 16-bit data into too bytes c:coarse and f:fine
    c, f = divmod(data, 256)
    to_send = [c, f]
    GPIO.output(pin, False)
    spi.xfer(to_send)
    GPIO.output(pin, True)
    data = data + 0b000000000010000
    sleep(0.01)
