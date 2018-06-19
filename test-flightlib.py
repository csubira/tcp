import unittest
from flightlib import FlightControllerConversation
from errors import *

fc = FlightControllerConversation()

class FlightLibTestCase(unittest.TestCase):
    """Tests for `flightlib.py`."""

    def test_check_airline_ibe(self):
        """Check if IBE is an airline"""
        self.assertTrue(fc.check_airline('IBE'), msg="Not a valid airline id")
    
    def test_check_airline_aaa(self):
        """Check AAA is not an airline"""
        self.assertFalse(fc.check_airline('AAA'), msg="Not a valid airline id")

    def test_check_flight_id_1234(self):
        """Check 1234 is a valid flight id"""
        self.assertTrue(fc.check_flight_id('1234'), msg="Not a valid flight id")

    # def test_check_airline_ave(self):
    #     """Check if IBE is an airline"""
    #     with self.assertRaises(AirlineNotValid):
    #         fc.check_airline('AVE')

if __name__ == '__main__':
    unittest.main()