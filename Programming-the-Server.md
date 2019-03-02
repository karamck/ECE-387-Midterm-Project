# How to Program the Server
This module will talk you through programming your server pi. I suggest dowloading the full file and running it if you are interested in using my project, as I will mainly discuss the important lines that are crucial to creating your own application. I also recommend that you use a sticky note to mark which pi is your server and its IP address. Follow along with the project-mid-server.py file.

The first thing you must do when creating your server is to import the socket library, and the sys library is also important if you choose to use command line arguments.  
The Host varialbe on line 10 should contain the IP address of the server because it will host any client that tries to connect.  
Lines 19-89 are just variables and methods for my specific project.
The server code reatlly begins with the try: function. By using a try, except, I allow for the server to be terminated by a keyboard input so that the server can be safely shut down and the error will be handled.  
The while True: loop on line 115 allows for a constant reopening of the socket so that when a connection is closed, the server will open a new one.  
Line 119 initiates a socket object s and the bind function on the next line chooses which port to open for the socket. It is important to use a port greater than 1023 because any lower is reserved.  
The s.listen(1) command waits until the first connection is attempted and then s.accept() accepts the connection and returns a tuple of the client socket connection and its address.  
The with connection: on line 128 gurantees that the connection was actually a success before continuing with the code, and the while connected: loop ensure that the loop will run until connection is lost.  
data = connection.recv(1024) on line 132 is how to read in what is sent from the client. This is encoded by the network conection into byte data so the data.decode('utf-8') command on line 141 is necessary to convert the message back into a useable string.  
Sending a message works the same as recieveing, just in reverse. First, the string must be encoded (Line 146) and then sent using the connection.sentall() command (Line147).  
Be sure that if connection is lost that the socket is closed (Line 150) before attempting to reopen in the next loop or else an error will occur because the port is still in use.

