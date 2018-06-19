import sys
import random
from errors import FlightControllerException, AirlineNotValid, Error


class FlightControllerConversation():
    AIRLINES = {"IBE" : "Iberia", "DLH" : "Lufthansa", "EZY" : "Easy Jet" }
    ACTIONS = { 0 : 'startup', 1 : 'pushback'}
    RESPONSES = {
            0: {'T': True , 'F': False},
            1: {'N':'North', 'S': 'South', 'E':'East', 'W': 'West'}
        }

    def __init__(self):
        """
            Flight Controller Conversation Class
        """
        self.error = FlightControllerException()
    
    def decode_request(self, r):
        """
            Decode request, checks if the request message is correct and prints elegible description

            :param str r: request message
            :rtype: array
            :return: Array containing airline id, flight id and action id.
            :raises: Error if message format is not correct
        """
        r = r.strip()

        if self.check_message(r):
            print('La aeronave numero ' + self.flight_id + ' de la compania ' + self.AIRLINES[self.airline_id] + ' solicita ' + self.ACTIONS[self.action_id])
            return True
        else:
            print self.error
            self.error.get_error()
            return False

    def order_response(self, message):
        """
            Define response

            If the request was correct:

                :return: The client indicator + the response encoded
                    i.e: `IBE1234N`

                    +----------+-------------+------------+----------+
                    | Startup                | Pushback   |          | 
                    +==========+=============+============+==========+
                    | T        | True        | N          | North    |
                    +----------+-------------+------------+----------+
                    | F        | False       | S          | South    |
                    +----------+-------------+------------+----------+
                    |          |             | E          | East     |
                    +----------+-------------+------------+----------+
                    |          |             | W          | West     |
                    +----------+-------------+------------+----------+
 
                :rtype: str

            If there is an error:

                :return: An error code to be decoded in the client side
                    i.e: `XXXYYYY/ERR3!`
                :rtype: str
        """

        if message:
            return self.encode_random_response()
        else:
            return self.encode_error_response()

    def encode_random_response(self):
        return self.airline_id + self.flight_id + random.choice(self.RESPONSES[self.action_id].keys()) + '!\n'

    def encode_error_response(self):
        try:
            self.airline_id and self.flight_id
        except:
            return 'XXXYYYY/ERR' + str(self.error.get_error_code()) + '!\n'
        return self.airline_id + self.flight_id + '/ERR' + str(self.error.get_error_code()) + '!\n'

    def check_message(self, r):
        """
            Request message structure should be:
            
            **XXXYYYY/Z**
            
            - Composed by:
                - Airline indicator: 3 letters (i.e `IBE`)
                - Flight id: 4 number (i.e `1234`)
                - Trailing slash ('\')
                - Action: 1 number (0 or 1) (i.e `1`)
            
            *i.e:* **IBE1234/1**
        """
        if self.check_message_structure(r):
            self.check_action(r)
            self.check_airline(r[0:3])
            self.check_flight_id(r[3:7])
            return self.check_action(r) and self.check_airline(r[0:3]) and self.check_flight_id(r[3:7])
        else:
            self.error.raise_error(0)
            return False
    
    def check_message_structure(self, r):
        """
            Checks if message structure is correct

            :param str r: request message
            :rtype: string
            :return: True if correct, False if incorrect
            :raises: Error if message format is not correct
        """

        if r.split('/'):
            if len(r.split('/')[0]) == 7:
                return True
            else:
                self.error.raise_error(3)
                return False
        else:
            return False
    
    def check_airline(self, airline_id):
        """
            Checks if airline id is valid and authorized

            :param str r: airline_id (positions 0-3 in message string)
            :rtype: string
            :return: True if correct, False if incorrect
            :raises: Error if message format is not correct
        """
        if airline_id in self.AIRLINES.keys():
            self.airline_id = airline_id
            return True
        else:
            self.error.raise_error(1)
            return False

    def check_flight_id(self, flight_id):
        """
            Checks if flight id is a valid number

            :param str r: flight_id (positions 3-7 in message string)
            :rtype: string
            :return: True if correct, False if incorrect
            :raises: Error if message format is not correct
        """
        if flight_id.isdigit():
            self.flight_id = flight_id
            return True
        else:
            self.error.raise_error(2)
            return False
    
    def check_action(self, r):
        """
            Checks if the action requested is among the list of options

            :param str r: a (3 first positions in message string)
            :rtype: string
            :return: True if correct, False if incorrect
            :raises: Error if message format is not correct
        """
        if r.split('/'):
            action = r.split('/')[1]
            if action.isdigit() and len(action) == 1:
                if int(action) in self.ACTIONS.keys():
                    self.action_id = int(action)
                    return True
                else:
                    self.error.raise_error(3)
                    return False
            else:
                self.error.raise_error(3)
                return False
        else:
            return False
