# ECE-387-Midterm-Project
Ethernet Port and Cable

# Introduction
 \nFor my 387 Midterm Project I chose to research and create a project using the ethernet port and cable. The ethernet cable is used for connecting devices to a network router for internet connection or creating local area networks. What interested me the most about ethernet was the ability to send information much faster than wireless connections with much higher efficiency. Ethernet cables are also faster than serial connections. To explore how to use this technology I connected two Raspberry Pi 3's via ethernet to create a local network.

# How it Works
 \nUnfortunately plugging an ethernet cable into the Raspberry Pis and calling it a day is not enough to get this project up and running. In order to connect our two Raspberry Pis together, both have to be configured with a static IPv4 address. The reason being is that everytime a device is connected to a network, it is assigned an IP address by the server, and that address can be changed everytime it connects. By setting the Raspberry Pis up with a static IP address there will be no need to dig and find out the new address for every connection. To do this, go to the [Setting Static IPs](https://github.com/karamck/ECE-387-Midterm-Project/blob/master/SettingStaticIP.md) page in the wiki.
