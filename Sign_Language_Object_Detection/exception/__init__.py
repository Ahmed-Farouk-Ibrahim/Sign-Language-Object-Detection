import sys

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error message information including the file name,
    line number, and the error message.

    :param error: Exception object
    :param error_detail: sys module to get exception information
    :return: Formatted error message string
    """
    # Extract traceback object from the exception information
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Format the error message with file name, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class SignException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Custom exception class for handling specific errors with detailed messages.

        :param error_message: Error message in string format
        :param error_detail: sys module to get exception information
        """
        # Initialize the parent Exception class with the error message
        super().__init__(error_message)

        # Generate detailed error message
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        """
        Return the detailed error message when converting the exception to a string.
        """
        return self.error_message
