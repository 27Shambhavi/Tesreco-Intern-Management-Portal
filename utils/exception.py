class InvalidEmailError(Exception):

    def __init__(self, message="Invalid Email Address"):
        super().__init__(message)


class InvalidDurationError(Exception):

    def __init__(self, message="Duration should be between 1 and 12 months"):
        super().__init__(message)


# Driver Code
if __name__ == "__main__":

    try:

        email = "abcgmail.com"

        if "@" not in email:
            raise InvalidEmailError()

    except InvalidEmailError as e:

        print(e)


    try:

        duration = 15

        if duration < 1 or duration > 12:
            raise InvalidDurationError()

    except InvalidDurationError as e:

        print(e)