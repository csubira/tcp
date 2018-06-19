class FlightControllerException():
    ERRORS = {
        0: 'Message structure not valid',
        1: 'Airline indicator not valid or airline not authorized',
        2: 'Flight indicator not valid',
        3: 'action not valid',
        #Client side
        4: 'Response not valid',
        5: 'This is not my indicator'
    }

    def __init__(self):
        self.reset_error()
    
    def raise_error(self, error_code):
        self.error_code = error_code
        
    def get_error(self):
        try:
            FlightControllerException.ERRORS[self.error_code]
        except:
            return None
        return FlightControllerException.ERRORS[self.error_code]
    
    def get_error_code(self):
        return self.error_code
    
    def reset_error(self):
        self.error_code = None


# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class AirlineNotValid(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
