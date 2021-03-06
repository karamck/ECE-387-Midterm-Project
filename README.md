# ECE-387-Midterm-Project
Ethernet Port and Cable

## Introduction
   For my 387 Midterm Project I chose to research and create a project using the ethernet port and cable. The ethernet cable is used for connecting devices to a network router for internet connection or creating local area networks. What interested me the most about ethernet was the ability to send information much faster than wireless connections with much higher efficiency. Ethernet cables are also faster than serial connections. To explore how to use this technology I connected two Raspberry Pi 3's via ethernet to create a local network.
   
   One Raspberry Pi is the Server and the other is the client but both are connected to 4 LEDs and 5 Buttons. Four of the buttons, when clicked, will illuminate the corresponding LEDs of the other Raspberry Pi. The additional button serves a different purpose for the server and for the client. In the case of the client, the fifth button simply closes the socket and terminates the program. For the server, the fifth button forces the client to close so that the socket can be reopened for a different client.
   
   A video of the working project can be found [here](https://www.youtube.com/watch?v=Nnm_pEIHlFs&t=1s).

## How it Works
   Unfortunately plugging an ethernet cable into the Raspberry Pis and calling it a day is not enough to get this project up and running. In order to connect our two Raspberry Pis together, both have to be configured with a static IPv4 address. The reason being is that everytime a device is connected to a network, it is assigned an IP address by the server, and that address can be changed everytime it connects. By setting the Raspberry Pis up with a static IP address there will be no need to dig and find out the new address for every connection. To do this, go to the [Setting Static IPs](SettingStaticIP.md) page in the wiki.
   
   Once both Raspberry Pis have been set up with static IP addresses, it is time to start creating the network. The method I chose to create my network with was using the socket module that is native to python. Socket servers are a server to client network where the server opens a port and binds to the first client which attempts to connect to that port. Think an outlet on the wall, it is available until something is plugged into it and nothing else can access it until the plug is removed. In this project, I designated one Raspberry Pi as the server and the other as the client. 
   
   The server pi instructions are under the [Programming the Server](Programming-the-Server.md) module and the client pi instructions are under the [Programming the Client](Programming-the-Client.md) module. 
   
   Once both the Raspberry Pis have been programmed and the breadboards set up, the project is ready to be run. First, start up the server pi and run the project-mid-server.py script in the terminal entering the desired port to be used (Note: use a port larger than 1023, 1023 and lower are privledged ports). Then, run the project-mid-client1.py script for the client, inserting the server's IP address into the command line followed by the port that was used for the server. You will see that they are now connected and you can control the LEDs of one Raspberry Pi with the buttons of the other. If you downloaded the project-mid-client2.py script you can press the terminating button on either Raspberry Pi, run the script on the client, and you will see that the network is back up and running. To close the server, just press ctrl+c on the keyboard.
   
## How to Implement this in your Projects
   My project is just one of many applications that can be done with the ethernet cable. My intention was to create a simple script that could be easily understood and manipulated to fit any project. Using the ethernet connection, you can connect two Raspberry Pis like I have to share data over a network, or you can get a shield for an arduino and create a network with two different chips. Another aspect I implemented in my project was the ability to terminate a client and keep the server socket open. By doing this, you could have multiple ethernet devices over a network and pick and choose which programs you would like to be running and when to end them.
   
#### Sources
Socket Programming in Pythong - By Nathan Jennings (https://realpython.com/python-sockets/)
Networking Lessons - By Raspberry Pi Foundation (https://github.com/raspberrypilearning/networking-lessons)
