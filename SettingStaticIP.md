# How to set your Static IP 
Setting up static IP addresses on your Raspberry Pi device is very simple. All this will take is a few linux terminal commands. First, enter the command:  sudo nano /etc/dhcpcd.conf and press enter. The file will open and you need to scroll down to the very bottom and type out these lines:

interface eth0

static ip_address=192.168.X.Y
static routers=192.168.X.1
static domain_name_servers=192.168.X.1

Notice the X and Y variables. You can decide whatever number you would like to use for X as it is unimportant, as long as you use the same number for both pis. The Y is unique for each device on the network so whichever you choose for one of the pis, cannot be used for the others. Thi number 1 is reserved for the network server, so choose a value between 2-255. In my project I set my server pi as 192.168.0.2 and my client pi as 192.168.0.3. Close the file by pressing ctrl + x (don't forget to save) and then reboot the system by entering the command: sudo reboot. Upon reboot, this will configure your Raspberry Pi to have a static IP when connected to ethernet. This can be undone by re-accessing the file and commenting out or deleting the added lines.
