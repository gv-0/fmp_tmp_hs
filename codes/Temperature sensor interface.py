from smbus2 import SMBus
import board
from mlx90614 import MLX90614 
from time import sleep
import urllib3


i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
#print(sensor.get_amb_temp())
#print(sensor.get_obj_temp())
http = urllib3.PoolManager()
'''
urls = ('/','index')
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    sleep(1)
    '''
while(1):
    #first locate your host on network then include ip
    t = http.request('POST','http://192.168.0.114:8080')
    print(t.data)
    sleep(1)
bus.close()

#sudo i2cdetect -y 1
#if returns with 5a then mlx is connected
