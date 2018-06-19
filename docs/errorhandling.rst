Error Handling
=====================

The error message follows the structure below:

    **XXXYYYY/ERRZ!**

    Composed by:
        - Airline indicator (If airline indicator in request was correct it uses the same one, otherwise XXXX)
        - Flight id (If flight indicator in request was correct it uses the same one, otherwise YYY)
        - Trailing slash
        - "ERR"
        - Error code (number)
        - Exclamation mark

The error code is defined as follows:

- 0: 'Message structure not valid',
- 1: 'Airline indicator not valid or airline not authorized',
- 2: 'Flight indicator not valid',
- 3: 'action not valid',
- 4: 'Response not valid',
- 5: 'This is not my indicator'