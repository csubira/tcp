.. Challenge 1 documentation master file, created by
   sphinx-quickstart on Tue May  1 18:34:06 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Challenge 1's documentation!
=======================================
The goal of this mini challenge is to develop a new communication protocol of application layer 7 similar to other protocols like HTTP, FTP, DNS, etc..

A protocol is just the definition of the rules that must be followed to maintain a communication between two endpoints. 

In this case we will apply this to a model client/server. This means that when the client says something specific to the server, the server must answer in a very specific way that the client already understands. Any other message format not defined in the protocol shared between both ends should be considered invalid.

In this case the protocol will implement a basic flight controlling communication rules:
Command action

The command action must have, at least, two variables:
The specific command
The ID of the flight

The command action must be answered with:
The ID of the flight
A valid answer to that requested command.

Call action

The call must have, at least, one variable:
The airline ID

The call must be answered, with:
The airline ID

Requirements

The exercise must be developed in python
It must be developed in three parts:
A client
A server
A communication library that is imported by both parts
Implement a basic error handling. If the client or server receive messages that they don’t understand they should be able to raise a error but not make crash the program
Write some documentation about the protocol, the client and the server

Extra balls

Implement basic tests
Being able to process requests in parallel
Some clues

Start developing the server. When you have been able to handle basic TCP connections and messages, start moving the common communication logic to a external library.
Leave the client development for the end. Start using programs like nc or telnet. They are TCP basic clients that you can use to send messages to a TCP server and see the answer
For the documentation, maybe it’s easier to use rdoc documentation instead of writing it manually in a external doc

The demo

The demo at the end of the exercise will consist on:
Start the server
Send commands through the client to the server using command parameters
Try to send commands or contents that are not defined in the protocol and see the answers
Try to modify a little bit the server so it answers with invalid responses


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   librarycode
   errorhandling



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
