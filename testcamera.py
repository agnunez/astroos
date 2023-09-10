from devices import Camera
from time import sleep

cam1 = Camera('STL', 4096, 4096)
cam2 = Camera('ASI', 4096, 4096)

cam1.info()
cam2.info()

cam1.swon()
cam2.connect()

cam1.info()
cam2.info()

cam1.expose(4)
cam2.async_expose(4)

i=0
while cam2.shutter == 'Open':
    print(f"{str(i)} {cam2.shutter}")
    sleep(1)
    i+=1