import sys
from logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Find error [{0}] in the file [{1}] at line number [{2}]".format(str(error),file_name,line_number)

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_details)

    def __str__(self) -> str:
        return self.error_message
