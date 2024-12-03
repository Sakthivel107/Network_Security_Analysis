import sys
def error_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error in the python script[{0}] line number [{1}] the error is [{2}]".format(
        file_name,exc_tb,str(error))
    return error_message
class MyException(Exception):
        def __init__(self,error_message,error_detail):
            super().__init__(error_message)
            self.error_message=error_details(error_message,error_detail=error_detail)
        def __str__(self) :
            return self.error_message     