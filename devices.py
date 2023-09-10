from time import sleep, perf_counter
from threading import Timer

class Device:
    state = 'None'
    def __init_(self):
        self.state = 'Off'
    def swon(self):
        self.state = 'On'
    def swoff(self):
        self.state = 'Off'
    def connect(self):
        self.state = 'Connected'
    def disconnect(self):
        self.state = 'Disconnected'

class Camera(Device):
    shutter = 'Closed'
    def __init__(self,name,px,py,state=None):
        super().__init__()
        self.name = name
        self.px = px
        self.py = py
    def close(self):
        self.shutter = 'Closed'
        print('shutter closed in '+self.name)
    def async_expose(self, time):
        timer1 = Timer(time, self.close)
        print('shutter open in '+self.name)
        self.shutter = 'Open'
        timer1.start()
    def expose(self, time):
        self.shutter = 'Open'
        init = perf_counter()
        print('exposure started in '+self.name+' for '+ str(time)+ ' secs')
        while (perf_counter()-init) < time:
            sleep(0.5)
            print('.', end='', flush=True)
        print()
        print('Exposure finished in '+self.name)
    def info(self):
        print(f'Camera: {self.name} State: {self.state} Shutter: {self.shutter}')
    def get_shutter(self):
        return self.shutter
        