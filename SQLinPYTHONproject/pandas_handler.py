import pandas as pd
from lookups import ErrorHandling, InputTypes
from logging_handler import show_err_message

def remove_duplicates(df):
   try:
      removed_dup = df.drop_duplicates()
   except Exception as e:
      err_str_suffix = str(e)
      err_str_preffix = ErrorHandling.REMOVE_DUPLICATES_ERROR.value
      show_err_message(err_str_preffix,err_str_suffix)
      removed_dup = None
   finally:
      return removed_dup
   
def remove_nulls(df):
   try:
      removed_nulls = df.dropna()
   except Exception as e:
      err_str_suffix = str(e)
      err_str_preffix = ErrorHandling.REMOVE_NULLS_ERROR.value
      show_err_message(err_str_preffix,err_str_suffix)
      removed_nulls = None
   finally:
      return removed_nulls
   
def get_blanks(df):
   try:
      blank_rows = df[df.isnull()]
   except Exception as e:
      err_str_suffix = str(e)
      err_str_preffix = ErrorHandling.GET_NULLS_ERROR.value
      show_err_message(err_str_preffix,err_str_suffix)
      blank_rows = None
   finally:
      return blank_rows

def get_shape(df):
   try:
      shape = df.shape
   except Exception as e:
      err_str_suffix = str(e)
      err_str_preffix = ErrorHandling.GET_SHAPE_ERROR.value
      show_err_message(err_str_preffix,err_str_suffix)
      shape = None
   finally:
      return shape

def get_length(df):
   try:
      length = len(df)
   except Exception as e:
      err_str_suffix = str(e)
      err_str_preffix = ErrorHandling.GET_LENGTH_ERROR.value
      show_err_message(err_str_preffix,err_str_suffix)
      length = None
   finally:
      return length