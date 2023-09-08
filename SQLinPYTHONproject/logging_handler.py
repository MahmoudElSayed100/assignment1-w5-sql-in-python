import logging

logger = logging.getLogger

def show_err_message(err_str_prefix, err_str_suffix):
   err_messsage = err_str_prefix + "=" + err_str_suffix
   print(err_messsage) 