Library documentation
=====================
.. currentmodule:: flightlib

Flightlib is a python library designed to allow communications in the FlightController TCP protocol.

The main class in Flightlib, `FlightControllerConversation`, defines a conversation between the server(Controller) and the client(Pilot).
The conversation starts when the pilot makes a request to the controller and ends when the answer is received/collated by the pilot.
(In this challenge, the conversation is not ended until any of the participants closes the comunication)

The conversation is established through encoded messages described below.




Request Message
=======================
*(From pilot to controller)*

The pilot asks the controller for two different actions:

1. **Startup**
The pilot asks for approval for engine startup

2. **Pushback**
The pilot asks for nose direction in pushback manouver

**Structure:**

    Request message structure should be:
    
    **XXXYYYY/Z**
    
    Composed by:
        - Airline indicator
        - Flight id
        - Trailing slash
        - Action
    
    *i.e:* **IBE1234/1**

Airline indicator: As defined in `ICAO Rules for airline designators <https://www4.icao.int/3LD/Home/Rules>`_
an airline designator should be composed of three letters.

In this challenge only the following three airlines would be admitted:

- IBE as Iberia
- DLH as Lufthansa
- EZY as EasyJet

Flight indicator: Designated by `IATA <https://www.icao.int/APAC/Meetings/2011_FPL_AM_TF4_Seminar/WP13.pdf>`_, it should include 4 numbers.

Action: As defined for this protocol

- 0: Startup
- 1: Pushback




Answer Message
=======================
*(From controller to pilot)*

The controller answers the pilot according to the previous request:

- Requested **Startup**:
    - Pushback approved
    - Pushback defined


- Requested *Pushback*
    - Direction nose in pushback


**Structure:**

    Answer message structure should be:
    
    **XXXYYYY/Z**
    
    Composed by:
        - Airline indicator
        - Flight id
        - Trailing slash
        - Answer
    
    *i.e:* **IBE1234/N**

    +----------+-----------------+------------+----------+
    | Startup                    | Pushback   |          | 
    +==========+=================+============+==========+
    | T        | Accepted        | N          | North    |
    +----------+-----------------+------------+----------+
    | F        | Denied          | S          | South    |
    +----------+-----------------+------------+----------+
    |          |                 | E          | East     |
    +----------+-----------------+------------+----------+
    |          |                 | W          | West     |
    +----------+-----------------+------------+----------+





Library Reference
=======================

.. autoclass:: FlightControllerConversation
   :members:
   :private-members: