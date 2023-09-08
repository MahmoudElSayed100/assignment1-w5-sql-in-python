from lookups import ErrorHandling, InputTypes
from logging_handler import show_err_message
import os

def get_csv_files_from_folder(path):
   csvfiles = []
   try:
      for fileName in os.listdir(path):
         if fileName.endswith(".csv"):
            csvfiles.append(os.path.join(path,fileName))
   except Exception as e:
      err_str_suffix = str(e)
      err_str_preffix = ErrorHandling.CSV_GET_FILES_ERROR.value
      show_err_message(err_str_preffix,err_str_suffix)
   finally:
      return csvfiles
