import sys
from src.logger import logging

def error_message_deatil (error,error_deatil:sys):
    _,_,exe_tb = error_deatil.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    line_number = exe_tb.tb_lineno
    error = str(error)
    error_message = f"Error occured in pytohn script name {file_name} line number {line_number} error message {error}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_deatil:sys):
        super().__init__(error_message)
        self.error_message = error_message_deatil(error_message,error_deatil=error_deatil)

    def __str__(self):
        return self.error_message