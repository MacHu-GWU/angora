##encoding=utf8

from __future__ import print_function
from angora.PandasSQL.sqlite3blackhole import Sqlite3BlackHole, CSVFile

def main():
    bh = Sqlite3BlackHole("test.db") # define database
    # define first file
    advertisement = CSVFile(r"test_data/advertisement.txt", # path
                            table_name="advertisement", # table_name
                            sep=",", # seperator
                            dtype={"id": "TEXT", "hour": "DATETIME"}, # datatype
                            usecols=[0,1,2,3,4,5,6,7,8,9], # use cols
                            primary_key_columns=["id"]) # primary_key_columns
    # define second file
    employee = CSVFile(r"test_data/employee.txt",
                       table_name="employee",
                       sep=",",
                       dtype={"employee_id": "TEXT", "start_date": "DATE"},
                       primary_key_columns=["employee_id"])

    bh.add(advertisement)
    bh.add(employee)
    bh.devour()
    
    bh.engine.prt_howmany(advertisement.table)
    bh.engine.prt_howmany(employee.table)
        
main()