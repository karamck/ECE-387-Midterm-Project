# ECE-387-Midterm-Project
Ethernet Port and Cable

# Introduction
   For my 387 Midterm Project I chose to research and create a project using the ethernet port and cable. The ethernet cable is used for connecting devices to a network router for internet connection or creating local area networks. What interested me the most about ethernet was the ability to send information much faster than wireless connections with much higher efficiency. Ethernet cables are also faster than serial connections. To explore how to use this technology I connected two Raspberry Pi 3's via ethernet to create a local network.
   
   One Raspberry Pi is the Server and the other is the client but both are connected to 4 LEDs and 5 Buttons. Four of the buttons, when clicked, will illuminate the corresponding LEDs of the other Raspberry Pi. The additional button serves a different purpose for the server and for the client. In the case of the client, the fifth button simply closes the socket and terminates the program. For the server, the fifth button forces the client to close so that the socket can be reopened for a different client.

# How it Works
   Unfortunately plugging an ethernet cable into the Raspberry Pis and calling it a day is not enough to get this project up and running. In order to connect our two Raspberry Pis together, both have to be configured with a static IPv4 address. The reason being is that everytime a device is connected to a network, it is assigned an IP address by the server, and that address can be changed everytime it connects. By setting the Raspberry Pis up with a static IP address there will be no need to dig and find out the new address for every connection. To do this, go to the [Setting Static IPs](https://github.com/karamck/ECE-387-Midterm-Project/blob/master/SettingStaticIP.md) page in the wiki.
   
   Once both Raspberry Pis have been set up with static IP addresses, it is time to start creating the network. The method I chose to create my network with was using the socket module that is native to python. Socket servers are a server to client network where the server opens a port and binds to the first client which attempts to connect to that port. Think an outlet on the wall, it is available until something is plugged into it and nothing else can access it until the plug is removed. In this project, I designated one Raspberry Pi as the server and the other as the client. 
   The server pi 
