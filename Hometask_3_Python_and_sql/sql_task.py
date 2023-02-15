
from mysql.connector import MySQLConnection, Error
import logging
import os
import time
from configparser import ConfigParser
import math
import datetime
import sys
sys.path.append("/root/sql_task/variables.py")
import variables as constants
from functools import reduce
import functools
import operator
from itertools import accumulate

def configure_logging():
    filename = os.path.join('/root/sql_task/', 'logger.log')
    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    Logger = logging.getLogger()
    Logger.setLevel(logging.INFO)

    # Create a logger to output to a .log file
    fileHandler = logging.FileHandler(filename.format(time.strftime('%Y%m%d%H%M%S')))
    fileHandler.setFormatter(logFormatter)
    Logger.addHandler(fileHandler)

    # Create a logger for output to the console
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    Logger.addHandler(consoleHandler)
    Logger.info("Logger Completed!")

    return Logger


def generate_all_pseudo_random_number():
    # Initialization of a two-dimensional array, deduce the required number of columns and rows from constants and fill with zeros.
    generate_pseudorandom_numbers_list = [[0 for x in range(constants.COLUMNS)] for x in range(constants.ROWS)] 
    # We get data to generate from the dictionary, the key of the first level of the dictionary matches column 2 of the dimensional array (from 0 to ...)
    dict = constants.FIND_PSEUDORANDOM_ROWS1
    for row in range(constants.ROWS):
        for column in range(constants.COLUMNS):
            for table_column_index, ranges_for_columns in dict.items():
                for range_as_key, value in ranges_for_columns.items():
                        if row in range_as_key:
                                if table_column_index == column:
                                    if table_column_index != 8 and table_column_index != 5:
                                    # We get generated random numbers for all columns, only for the first row - unique, for the rest - sequentially from the first row
                                        if row == 0:
                                             formula = 1/math.pi * math.acos(math.cos(dict[table_column_index][range_as_key]['start_value'] + 100)) * (dict[table_column_index][range_as_key]['upper_limit'] - \
                                             dict[table_column_index][range_as_key]['bottom_limit1']) + dict[table_column_index][range_as_key]['bottom_limit2']
                                             generate_pseudorandom_numbers_list[row][column] = round(formula, 3)

                                        else:
                                             formula = 1/math.pi * math.acos(math.cos(((generate_pseudorandom_numbers_list[row-1][column]) * dict[table_column_index][range_as_key]['coefficient_for_high_dispersion']) + 100)) * \
                                             (dict[table_column_index][range_as_key]['upper_limit'] - dict[table_column_index][range_as_key]['bottom_limit1']) + dict[table_column_index][range_as_key]['bottom_limit2']
                                             generate_pseudorandom_numbers_list[row][column] = round(formula, 3)

                                    # Get "create date" given the break time from 23:00 - 24:00
                                    if table_column_index == 5:  
                                        if row == 0:
                                            generate_pseudorandom_numbers_list[row][column] = (dict[table_column_index][range_as_key]['start_value']) + dict[table_column_index][range_as_key]['start_time_unix']
                                            
                                        else:
                                            formula = (1/math.pi * math.acos(math.cos(((generate_pseudorandom_numbers_list[row-1][column]) * dict[table_column_index][range_as_key]['coefficient_for_high_dispersion']) + 100)) * \
                                            (dict[table_column_index][range_as_key]['upper_limit'] - dict[table_column_index][range_as_key]['bottom_limit1']) + dict[table_column_index][range_as_key]['bottom_limit2']) + \
                                            dict[table_column_index][range_as_key]['start_time_unix']
                                            generate_pseudorandom_numbers_list[row][column] = round(formula, 4)
                                            
                                            if generate_pseudorandom_numbers_list[row][column]  > constants.START_BREAK and generate_pseudorandom_numbers_list[row][column]  < constants.END_BREAK:
                                                time_after_break = (constants.END_BREAK + generate_pseudorandom_numbers_list[row][4])  
                                                generate_pseudorandom_numbers_list[row][column] = round(time_after_break, 4)
                                                
                                    # We get the generated random numbers for the matching instrument from the 4th column
                                    if table_column_index == 8:   
                                            temp_comparison_with_instrument_column = round(generate_pseudorandom_numbers_list[row][3])
                                            for fourth_level_index, value in value.items():
                                                if temp_comparison_with_instrument_column == fourth_level_index:
                                                    if row == 0:
                                                        formula = 1/math.pi * math.acos(math.cos(dict[table_column_index][range_as_key][fourth_level_index]['start_value'] + 100)) * (dict[table_column_index][range_as_key][fourth_level_index]['upper_limit'] - \
                                                        dict[table_column_index][range_as_key][fourth_level_index]['bottom_limit1']) + dict[table_column_index][range_as_key][fourth_level_index]['bottom_limit2']  
                                                        generate_pseudorandom_numbers_list[row][column] = round(formula, 4) 

                                                    else:
                                                        formula = 1/math.pi * math.acos(math.cos(((generate_pseudorandom_numbers_list[row-1][column]) * dict[table_column_index][range_as_key][fourth_level_index]['coefficient_for_high_dispersion']) + 100)) * \
                                                        (dict[table_column_index][range_as_key][fourth_level_index]['upper_limit'] - dict[table_column_index][range_as_key][fourth_level_index]['bottom_limit1']) + dict[table_column_index][range_as_key][fourth_level_index]['bottom_limit2']
                                                        generate_pseudorandom_numbers_list[row][column] = round(formula, 4) 
    # We extract the seventh column with statuses to pass to the next function. We remove one fourth column from the array, as an auxiliary one, and return the list                                           
    getting_column_for_status_random = functools.reduce(operator.iconcat,[[j for i,j in enumerate(sub) if i == 7] for sub in generate_pseudorandom_numbers_list])
    return [[j for i,j in enumerate(sub) if i != 4] for sub in generate_pseudorandom_numbers_list], getting_column_for_status_random


def generate_status_all_zones(column_of_statuses_list):
    main_list_for_cases_red = []
    main_list_for_cases_green = []
    main_list_for_cases_blue = []
    # Depending on the ranges of zones, we compare the sequences generated earlier for these zones with arrays of possible variants of status subsets from the dictionary. We write them down in different lists.
    dict = constants.DICT_STATUS_GENERATE_ALL_ZONES
    names = [main_list_for_cases_red, main_list_for_cases_green, main_list_for_cases_blue]
    for count_of_names, value_of_names_list in enumerate(names):
        for index in range(len(column_of_statuses_list)):
            for count_of_ranges, ranges in dict.items():
                if count_of_names == count_of_ranges:  
                    for range_as_key, value_of_count_lists in ranges.items():
                        if index in range_as_key:    
                            names[count_of_names].append(dict[count_of_ranges][range_as_key][round(column_of_statuses_list[index])])
    # We remove one level of arrays, and write the statuses into a one-dimensional one sequentially, add to the general array "list_for_flatten_statuses", such an amount that we need for zones          
    list_for_flatten_statuses  = reduce(lambda x, y: x + y, main_list_for_cases_red )[0:376] + reduce(lambda x, y: x + y, main_list_for_cases_green)[0:1372] \
    + reduce(lambda x, y: x + y, main_list_for_cases_blue)[0:754]

    return list_for_flatten_statuses
        

def get_data_from_pseudo_random_rows(all_list_pseudo_random_numbers, list_for_flatten_statuses):

    dict = constants.GET_VALUE_FROM_PSEUDORANDOM
    for column in range(constants.COLUMNS):
        for row in range(0, (constants.ROWS)-1):
            for table_column_index, first_level_values in dict.items():
                if table_column_index == column:
                    # First, we write the starting hex value in the first line. And then we make a dynamic random increment "temp" by which we multiply the previous row.
                    if column == 0:
                        if row == 0:
                            all_list_pseudo_random_numbers[row][column] = dict[table_column_index]['hex_start_number']
                        else:
                            temp = constants.INCREMENT_FOR_RANDOMNESS * all_list_pseudo_random_numbers [row][column]
                            all_list_pseudo_random_numbers[row][column] = ((hex(int(all_list_pseudo_random_numbers[row - 1][column], 16) + round(temp))).lstrip("0x").upper().zfill(10)) 
                    # We compare the key value from the string with the dictionary key and write the value to the array in columns 1..2..3
                    if column == 1 or column == 2:
                        all_list_pseudo_random_numbers[row][column] = dict[table_column_index][(round(float(all_list_pseudo_random_numbers[row][column])))]
                    # If the array "list_for_flatten_statuses" value corresponds to three statuses ('fill', 'done', 'part fill') in the dictionary, we get the initial price from column 7
                    if column == 8:
                            for key_status, bool_value in first_level_values.items():
                                if list_for_flatten_statuses[row - 1] != first_level_values['special_status'] and key_status == list_for_flatten_statuses[row] and True:
                                    all_list_pseudo_random_numbers[row][column] = all_list_pseudo_random_numbers[row][column - 1]
                    # If the value in the list "list_for_flatten_statuses" corresponds to the values in dict, then we write the value from column 9 multiplied on "multiplier_value" into column 10, 
                    # if "reject" is in the previous line in list "list_for_flatten_statuses", then in "done" we leave empty                
                    if column == 10:
                            for key_status, multiplier_value in first_level_values.items():
                                if list_for_flatten_statuses[row - 1] != first_level_values['special_status'] and key_status == list_for_flatten_statuses[row]: 
                                     all_list_pseudo_random_numbers[row][column] = round(all_list_pseudo_random_numbers[row][column - 1] * multiplier_value, 3)
                    # We iterate over the second column, if the value matches the value in the dictionary, we write it in column 11
                    if column == 11:
                        all_list_pseudo_random_numbers[row][column] = dict[table_column_index][all_list_pseudo_random_numbers[row][column - 10]]
                    # If the line number falls within the range in the dictionary, we write the corresponding value in column 12
                    if column == 12:
                        for ranges, value in first_level_values.items():
                            if row in ranges:
                                all_list_pseudo_random_numbers[row][column] = dict[table_column_index][ranges]
                    # We iterate over the third column, if the value matches the value in the dictionary, we write it in column 13
                    if column == 13:
                        all_list_pseudo_random_numbers[row][column] = dict[table_column_index][all_list_pseudo_random_numbers[row][column - 11]]
            # We overwrite a separate column from list "list_for_flatten_statuses"  with statuses in the corresponding one in the general table
            if column == 6:
                    all_list_pseudo_random_numbers[row][column] = list_for_flatten_statuses[row]
            # Line by line, we check the values of the array "list_for_flatten_statuses" with statuses line by line, if, depending on the range, the value is not "True", we overwrite the next line of the array with the current one.       
            if column == 3 or column == 7 or column == 9:
                for key_ranges, value in constants.IS_NEW_COLUMN_DICT.items():
                    if row in key_ranges:
                        if not value[list_for_flatten_statuses[row]]:
                            all_list_pseudo_random_numbers[row+1][column] = all_list_pseudo_random_numbers[row][column]
            if column == 3:
                all_list_pseudo_random_numbers[row][column] = dict[column][(round(float(all_list_pseudo_random_numbers[row][column])))]

    return  all_list_pseudo_random_numbers


def build_correct_table_based_on_statuses(updated_value_list_from_pseudo_random):
    # We iterate over the dictionary and the list checking the incoming status value
    updated_value_list_from_pseudo_random[0][5] = updated_value_list_from_pseudo_random[0][4] + updated_value_list_from_pseudo_random[0][5]
    for index in range(0,len(updated_value_list_from_pseudo_random)-1):
        for key_ranges, value in constants.IS_NEW_COLUMN_DICT.items():
            if index in key_ranges:
                # We collect tables depending on the statuses. Plus the Unix time + increment between columns 4 and 5. And before that, we do the correct sequence of increments in the 5th column when we form "current_row"
                if not value[updated_value_list_from_pseudo_random[index][6]]:
                    current_row = [updated_value_list_from_pseudo_random[index][0], updated_value_list_from_pseudo_random[index][1], updated_value_list_from_pseudo_random[index][2], updated_value_list_from_pseudo_random[index][3], updated_value_list_from_pseudo_random[index][4], \
                                  updated_value_list_from_pseudo_random[index][5] + updated_value_list_from_pseudo_random[index+1][5], updated_value_list_from_pseudo_random[index+1][6], updated_value_list_from_pseudo_random[index][7], updated_value_list_from_pseudo_random[index+1][8], updated_value_list_from_pseudo_random[index][9], \
                                  updated_value_list_from_pseudo_random[index+1][10], updated_value_list_from_pseudo_random[index][11], updated_value_list_from_pseudo_random[index][12], updated_value_list_from_pseudo_random[index][13]]
                    updated_value_list_from_pseudo_random[index+1] = current_row 
                # If not "done" we overwrite the next line (Unix time + increment change date)
                else:
                    updated_value_list_from_pseudo_random[index+1][5] = updated_value_list_from_pseudo_random[index+1][5] + updated_value_list_from_pseudo_random[index+1][4] 
                # Convert Unix to datatime. Return a datetime object with time zone information. Format the string datatime to human readable. Trim to 3 milliseconds and add a colon.
                unix_convert_to_datatime = datetime.datetime.utcfromtimestamp(updated_value_list_from_pseudo_random[index][4]).astimezone()
                formatted_time = (unix_convert_to_datatime.strftime(constants.FORMAT_FOR_DATATIME)[:23] + unix_convert_to_datatime.strftime(constants.FORMAT_FOR_DATATIME)[26:])
                updated_value_list_from_pseudo_random[index][4] = formatted_time.replace('+0200', '+02:00')
                unix_convert_to_datatime = datetime.datetime.utcfromtimestamp(updated_value_list_from_pseudo_random[index][5]).astimezone()
                formatted_time = (unix_convert_to_datatime.strftime(constants.FORMAT_FOR_DATATIME)[:23] + unix_convert_to_datatime.strftime(constants.FORMAT_FOR_DATATIME)[26:])
                updated_value_list_from_pseudo_random[index][5] = formatted_time.replace('+0200', '+02:00')

    return  updated_value_list_from_pseudo_random


def read_db_config(filename = constants.PATH_CONFIG_FILE, section='mysql'):
    # Create a parser and read the ini config file
    parser = ConfigParser()
    parser.read(filename)
    # Read file line by line and add to dictionary
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

def connect(set_up_logger):
    # Pass in the form of a dictionary our data to connect to the database
    db_config = read_db_config()
    connection = None
    try:
        print('Connecting to MySQL database...')
        connection = MySQLConnection(**db_config)
        # Establish a connection to the base, with the appropriate pin to pass to the next function
        if connection.is_connected():
            db_Info = connection.get_server_info()
            set_up_logger.info("Connected to MySQL Server version %s" % db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            set_up_logger.info("You're connected to database: %s" % record)
        else:
            set_up_logger.critical("MySQL connection is closed")  

    except Error as error:
        set_up_logger.info("Error while connecting to MySQL %s" % error)
        sys.exit(1)

    return connection

def drop_and_create_table (connection, build_correct_table_values, set_up_logger):
    # We iterate over the array, turn our strings into delimited tuples, and the following method will do a multiple concatenation of our qwery + string tuples
    try:
        sql_query_string_for_insert = str(tuple(build_correct_table_values[0]))
        for index in range (1, constants.ROWS-1):
            sql_query_string_for_insert += ', ' + str(tuple(build_correct_table_values[index]))
        formatted_sql_query = f"INSERT INTO test.new_table4 (ID, ProviderID, Direction, Instrument, CreationDate, ChangeDate, Status, InitialPrice, \
                                FillPrice, InitialVolume, FillVolume, Tags, Description, ExtraData) values " + sql_query_string_for_insert     
        connection._execute_query(formatted_sql_query)
        connection.commit()
        set_up_logger.info(f"lines for Red zone - {constants.ROWS_FOR_RED_ZONE}, for Green zone - {constants.ROWS_FOR_GREEN_ZONE}, Blue zone - {constants.ROWS_FOR_BLUE_ZONE}, successfully written to the database and saved!")

    except Error:
        set_up_logger.critical('Connection failed.')
    # Check if the connection to the database is open, if yes - close.              
    finally:
        if connection.is_connected():
            connection.close()
            set_up_logger.info("MySQL connection is closed")     

def main():

    set_up_logger = configure_logging() 
    generate_all_pseudo_random_numbers_list = generate_all_pseudo_random_number()
    all_list_pseudo_random_numbers = generate_all_pseudo_random_numbers_list[0]
    column_of_statuses_list = generate_all_pseudo_random_numbers_list[1]
    get_all_zones_from_numbers = generate_status_all_zones(column_of_statuses_list)
    updated_value_list_from_pseudo_random = get_data_from_pseudo_random_rows(all_list_pseudo_random_numbers, get_all_zones_from_numbers)
    build_correct_table_values = build_correct_table_based_on_statuses(updated_value_list_from_pseudo_random)
    db_connection_to_mysql = read_db_config()
    connect_to_database = connect(set_up_logger)
    set_and_execute_mysql_query = drop_and_create_table (connect_to_database, build_correct_table_values, set_up_logger)
if __name__ == '__main__':
    main()









