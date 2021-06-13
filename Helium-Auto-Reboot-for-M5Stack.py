from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import machine
import time
import json




mode = None
HotspotName = None
switchStat = None




# Describe this function...
def reboot():
  global mode, HotspotName, switchStat
  setSwitch('Off')
  wait(300)
  setSwitch('On')

# Describe this function...
def setSwitch(mode):
  global HotspotName, switchStat
  if mode=='On':
    rgb.setColorAll(0x33cc00)
    pin0.on()
    switchStat = 'On'
  elif mode=='Off':
    rgb.setColorAll(0xff0000)
    pin0.off()
    switchStat = 'Off'
  else:
    if switchStat == 'Off':
      setSwitch('On')
    else:
      setSwitch('Off')

# Describe this function...
def checkHost():
  global mode, HotspotName, switchStat
  try:
    req = urequests.request(method='GET', url=(str('https://api.helium.io/v1/hotspots/name/') + str(HotspotName)))
    if 'online' != ((((json.loads((req.text)))['data'])[0]['status'])['online']):
      reboot()
  except:
    pass


def buttonA_wasPressed():
  global HotspotName, mode, switchStat
  setSwitch('Toggle')
  pass
btnA.wasPressed(buttonA_wasPressed)

@timerSch.event('checkOnlineHourly')
def tcheckOnlineHourly():
  global HotspotName, mode, switchStat
  checkHost()
  pass

@timerSch.event('rebootDaily')
def trebootDaily():
  global HotspotName, mode, switchStat
  reboot()
  pass


HotspotName = 'helium-hotspot-name-here'
pin0 = machine.Pin(23, mode=machine.Pin.OUT, pull=machine.Pin.PULL_DOWN)
setSwitch('On')
timerSch.run('checkOnlineHourly', (60 * 60 * 1000), 0x00)
timerSch.setTimer('rebootDaily', (24 * 60 * 60 + 1000), 0x00)
