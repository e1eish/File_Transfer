# Overview

This is a simple program to transfter files from a server to a client. First run the server, then run the client and choose the file to save and put the destination file path in the FILENAME constant.

This was made to learn and practice the basics of networking with TCP and sockets.

[Software Demo Video](https://youtu.be/o0VfgC4NaD0)

# Network Communication

This uses client/server architecture using the socket python library. TCP was used on port 65432. The messages sent are json files in the form of strings.

# Development Environment

This program was written in python using Visual Studio Code. The socket library was necessary to set up sockets and stream data.

# Useful Websites

* [Client-server model - Wikipedia](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [What's the Difference Between TCP and UDP? - How-To Geek](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [Python Socket Libraries](https://docs.python.org/3.6/library/socket.html)
* [Creating a Simple Socket Server and Client in Python - YouTube](https://www.youtube.com/watch?v=sUzM-vIC-s4)
* [Sockets with Python 3 - YouTube](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdzLB_0JSTTcl8E8jsJLhR5)

# Future Work

* Make adding more files to download easier and not require hard coding.
* Handle erroneous client inputs.
* Allow clients to upload files.