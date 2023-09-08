import psycopg2
from lookups import ErrorHandling, InputTypes
from logging_handler import show_err_message
import pandas as pd

db_name = "dvd_rental"
db_user = "postgres"
db_pass = "M@rkseven11"
db_host = "localhost"
db_port = 5432

def create_connection():
    db_session = None
    try:
        
        db_session = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_pass,
            host = db_host,
            port = db_port
    )
    except Exception as e:
        err_str_prefix = ErrorHandling.DB_CONNECTION_ERROR.value
        err_str_suffix = str(e)
        show_err_message(err_str_prefix,err_str_suffix)
    finally:
         return db_session
    
def return_query(db_session, query):
   try:
       cursor = db_session.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       db_session.commit()
   except Exception as e:
       err_str_prefix = ErrorHandling.DB_RETURN_QUERY_ERROR.value
       err_str_suffix = str(e)
       show_err_message(err_str_prefix,err_str_suffix)
   finally:
       return results
   
def return_data_as_df(db_session,file_executor, file_type):
    return_dataframe = None
    try:
        if file_type == InputTypes.CSV:
            return_dataframe = pd.read_csv(file_executor)
        elif file_type == InputTypes.EXCEL:
            return_dataframe = pd.read_excel(file_executor)
        elif file_type == InputTypes.SQL:
            return_dataframe = pd.read_sql_query(con= db_session, sql= file_executor)
        else:
            raise Exception("FILE TYPE NOT FOUND 404")
    except Exception as e:
        suffix = str(e)
        if file_type == InputTypes.CSV:
            error_prefix = ErrorHandling.RETURN_CVS_DATA_ERROR.value
        elif file_type == InputTypes.EXCEL:
            error_prefix = ErrorHandling.RETURN_EXCEL_DATA_ERROR.value
        elif file_type == InputTypes.SQL:
            error_prefix = ErrorHandling.RETURN_SQL_DATA_ERROR.value
        else:
            error_prefix = ErrorHandling.RETURN_UNDEFINED_DATA_ERROR.value
        show_err_message(error_prefix, suffix)
    finally:
        return return_dataframe
    
#get schema info
def get_schema_info(db_session, table_name):
    try:
        cursor = db_session.cursor()
        query = f"SELECT.... i don't knowwww"
        cursor.execute(query)
        info = cursor.fetchall()
        db_session.commit()
    except Exception as e:
        err_str_suffix = str(e)
        err_str_preffix = ErrorHandling.SCHEMA_INFO_ERROR.value
        show_err_message(err_str_preffix,err_str_suffix)
    finally:
        return info
    
#extra gift for zahi:
def close_connection(db_session):
    db_session.close()