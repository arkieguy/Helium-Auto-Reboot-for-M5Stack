# Helium-Auto-Reboot-for-M5Stack

Here is a M5Stack UIFlow to monitor your [Helium miner](https://www.helium.com/mine) and automatically reboot it if it goes off line.

This script is designed to control a [M5Stack ATOM Socket Kit (HLW8023)](https://shop.m5stack.com/collections/m5-atom/products/atom-socket-kit-hlw8023-jp-us?variant=39295191744684) (you will also need to purchase a "[computer power cord](https://amzn.to/2UMP2Eu)").  The script will monitor a Helium Hotspot using the [Helium API](https://api.helium.io/v1/hotspots/name/) and will turn the hotspot off and back on automaticlly (rebooting it) if it shows as being "offline" on the API call.

- **main.m5f** - this is the [UIFlow](https://flow.m5stack.com) source.
- **main.py**  - this is the generated python script.

You can toggle the power to the hotspot by pushing the button on the M5Atom.  Green means the power is on, red means the power is off.  Once an hour, the Atom will check the API to see if the hotspot is online.  If it's not, it will cycle the poewer.  It will also cycle power once ever 24 hours for a daily reboot.

# Some basic M5Stack information 

Here are the steps needed to program the Atom:

1) Follow the instruction in the [M5Flow quick start documentation](https://docs.m5stack.com/en/quick_start/atom/atom_quick_start_uiflow). Be sure to write down the API key that is provided as part of the flash process, you will need it later.
2) Open [UIFlow Website](https://flow.m5stack.com) - choose "Beta" if prompted.
3) Click on the "API Key" link at the bottom left of the page.
4) Choose "Atom Lite" and enter you API Key.
5) Click on the hamburger menu in the upper right corner of the screen.  Choose "Open" and click on the **setup.m5** file from this repository.
6) Enter your Hotspot name in the second block of the program.
7) Click on the down arrow at the upper right corner to download the program to the Atom.

The M5Stack Atom Lite has 4 modes - Online Programming (Green), Offline Programming (Blue), WiFi Setup (Yellow) and App (Purple).  You can set the default mode with the M5Burner or by holding down the center button on the Atom as you apply power - release the button while it's displaying the color of the mode you would like.

To get the unit to automaitcally start the application on power up, select the "App" (purple) mode and it should automatically kick off the the program named "main" (this is why I renamed the modules).
