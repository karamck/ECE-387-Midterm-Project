# How to Program the Client
This module is just like the programming the server module. I still recomend that you mark your client pi in some way and record its IP address. This module will only talk about the socket specific programming, so if you wish to recreate project I suggest you download project-mid-client1.py file. The client is a much simpler program that simply connects to the server, and then loops until it decided to disconnect. Use the project-mid-client1.py file to follow along.

First, the socket library must be imported and the sys library must be imported to use command line arguments.  
Skipping lines 8-103 of project specific code brings us to the with socket as s function on line 105. Just like in the server code this will run code once a socket object is created, but this is not contained in a while true loop because we only want the client created once. It should only be created when the programs starts.  
The client connects to the server with the s.connect((host,port)) command on line 108, and the host is the IP of the server adn teh port is whatever port was used for the server socket. The client does not need to bind to a port like the server, it only needs to connect to the server's port.  
The while connected: loop with run until the connection is lost.  
The client is programmed to send a message to the server upon connection (line 118) but it first need to be encoded (line 117).  
Then, the client checks for a response from the server using the s.recv(1024) command (line 121). This message must be decoded (line 122) before it can be used. 

