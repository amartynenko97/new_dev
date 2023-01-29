## *Generate 2500 thousand historical records in sql database using python*

___


### *Installing nessesary software*

+ *Проверить наличие `python` в системе*

```sh
$ python3 --version
```
+ *Установить конектор*
*Прежде чем вы сможете получить доступ к базам данных MySQL с помощью Python, вы должны установить один из следующих пакетов в virtual environment*
    + *`mysqlclient` : этот пакет содержит модуль `MySQLdb` . Он написан на C и является одним из наиболее часто используемых пакетов Python для MySQL.*
    + *`mysql-connector-python` : этот пакет содержит модуль `mysql.connector` . Он полностью написан на Python.*
    + *`PyMySQL` : этот пакет содержит модуль `pymysql` . Он полностью написан на Python.*
```sh
$ apt-get install pip
$ pip install mysql-connector-python 
```
___


### *Writing Code for inizialise*

***Points to remember***

*`is_connected()` — это метод класса `MySQLConnection`, с помощью которого мы можем проверить, подключено ли наше приложение Python к MySQL.*
*Наконец, мы закрываем соединение с базой данных MySQL, используя метод `close()` класса `MySQLConnection`.*


*Создание экземпляра класса `cursor` который используется для выполнения `SQL` инструкции в `Python`*


lambda и map
Он перебирает список строк и применяет лямбда-функцию к каждому элементу строки. Затем сохраняет значение, возвращенное лямбда-функцией, в новую последовательность для каждого элемента. Затем, наконец, возвращает новую последовательность перевернутых строковых элементов.

Он перебирает все элементы в заданной последовательности. При повторении последовательности он вызывает данную функцию callback() для каждого элемента, а затем сохраняет возвращенное значение в новой последовательности. В конце концов, он возвращает эту новую последовательность преобразованных элементов.


```python
import mysql.connector
from mysql.connector import MySQLConnection, Error
import logging
import os
import time
import sys
from configparser import ConfigParser


def configure_logging():
    
    filename = os.path.join('/root/sql_task/', 'logger.log')

    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    Logger = logging.getLogger()
    Logger.setLevel(logging.INFO)

    # Cоздать обработчик-регистратор для вывода в файл .log

    fileHandler = logging.FileHandler(filename.format(time.strftime('%Y%m%d%H%M%S')))
    fileHandler.setFormatter(logFormatter)
    Logger.addHandler(fileHandler)

    # Cоздать обработчик-регистратор для вывода в консоль

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    Logger.addHandler(consoleHandler)

    Logger.info("Logger Completed!")

    return Logger


def read_db_config(filename='config.ini', section='mysql'):

    # Cоздать парсер и прочитать файл конфигурации ini
    
    parser = ConfigParser()
    parser.read(filename)

    # Прочитать файл  построчно и добавить в словарь

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db



def connect(set_up_logger):
    
    # Передать в виде словаря наши данные для подключения к базе

    db_config = read_db_config()
    connection = None
    try:
        print('Connecting to MySQL database...')
        connection = MySQLConnection(**db_config)
        
    
        if connection.is_connected():
            db_Info = connection.get_server_info()
            set_up_logger.info("Connected to MySQL Server version %s" % db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            set_up_logger.info("You're connected to database: %s" % record)
        else:
            print('Connection failed.')

    except Error as error:
        set_up_logger.info("Error while connecting to MySQL %s" % error)
        sys.exit(1)

    return connection



def drop_and_create_table (connection):

    db_config = read_db_config()
    connection = MySQLConnection(**db_config)

    # Если таблица существует - удаляем, и создаем новую

    try:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS table_for_id;')
        print('Creating table....')
        cursor.execute ('''create table if not exists table_for_id (
                            id int unsigned not null auto_increment,
                            category enum('tea', 'coffee') not null,
                            name varchar(50) not null,
                            price decimal(5,2) not null,
                            primary key (id)
                        )''')
    except Error:
        print('Connection failed.')
    else:
        print("Table has been cleared.") 

                      
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")                        
                        



def main():
    
    
    
    

    set_up_logger = configure_logging() 

    db_connection = read_db_config()
    

    # print(read_db_config())

    connect_to_database = connect(set_up_logger)
    # print(connect(connect_to_database))

    execute_table = drop_and_create_table (connect_to_database)

if __name__ == '__main__':
    main()
```

___

### *Output*

```sh
root@debian ~/sql_task $ python3 /root/sql_task/sql_task.py
2023-01-07 18:45:21 - root - INFO - sql_task - Logger Completed!
Connecting to MySQL database...
2023-01-07 18:45:21 - mysql.connector.authentication - INFO - authentication - package: mysql.connector.plugins
2023-01-07 18:45:21 - mysql.connector.authentication - INFO - authentication - plugin_name: caching_sha2_password
2023-01-07 18:45:21 - mysql.connector.authentication - INFO - authentication - AUTHENTICATION_PLUGIN_CLASS: MySQLCachingSHA2PasswordAuthPlugin
2023-01-07 18:45:21 - root - INFO - sql_task - Connected to MySQL Server version 8.0.31
2023-01-07 18:45:21 - root - INFO - sql_task - You're connected to database: new_schema
Creating table....
Table has been cleared.
MySQL connection is closed
```
___

### *logger.log*

```sh
[mysql]
host = localhost
database = new_schema
user = root
password = anton129
```




___


### *Part of generation*

```python
def Get_pseudorandom_coefficient(start_value, upper_limit, bottom_limit1, bottom_limit2):
    k = (1/math.pi*math.acos(math.cos(start_value+100))*(upper_limit-bottom_limit1)+bottom_limit2);
    return k


def generate_id_hex():
    hex_id_list = []
    coefficients_list = []

    coefficients_list.append(Get_pseudorandom_coefficient(100, 1, 0.1, 0.1))
    hex_id_list.append(constants.START_VALUE_GENERATION_ID)

    for i in range(1,2500):
        coefficients_list.append(Get_pseudorandom_coefficient(i-1, 1, 0.1, 0.1))
    

    for i in range(1,2500):
        temp = constants.INCREMENT_FOR_RANDOMNESS * coefficients_list[i]
        hex_id_list.append(hex(int(hex_id_list[i-1],16)+round(temp)))


    for index in range(0,2500):
        hex_id_list[index] = hex_id_list[index].lstrip("0x").upper().zfill(10)    
  

    return hex_id_list


def generate_provider():
    provider_list = []

    provider_list.append(Get_pseudorandom_coefficient(250, 100, 1, 1))

    for i in range(1,2500):
        provider_list.append(Get_pseudorandom_coefficient(provider_list[i-1], 100, 1, 1))

    update_provider_list = list(map(lambda x: 'SQM' if x <= 50 else 'FXCM', provider_list))

    return update_provider_list


def generate_direction():
    direction_list = []
    direction_list.append(Get_pseudorandom_coefficient(150, 100, 1, 1))

    for i in range(1,2500):
        direction_list.append(Get_pseudorandom_coefficient(direction_list[i-1], 100, 1, 1))

    update_direction_list = list(map(lambda x: 'sell' if x <= 50 else 'buy', direction_list))

    return update_direction_list


def generate_instrument():
    instrument_list = []

    instrument_list.append(Get_pseudorandom_coefficient(350, 110, 1, 1))

    for i in range(1,2500):
        instrument_list.append(Get_pseudorandom_coefficient(instrument_list[i-1], 100, 1, 1))
    
    update_instrument_list = list(map(lambda x: round(x/10), instrument_list))
 

    # Используем list comprehension/тернарный оператор
    update2_instrument_list = [x for key in update_instrument_list 
                               if key in constants.instrument_dictionary 
                               for x in constants.instrument_dictionary[key]]

    return update2_instrument_list




def generate_creation_date():
    redzone_list = [(constants.START_VALUE_RED_ZONE + constants.START_TIME_RED)]
    greenzone_list = [(constants.START_VALUE_GREEN_ZONE + constants.START_TIME_GREEN)]
    bluezone_list = [(constants.START_VALUE_BLUE_ZONE + constants.START_TIME_BLUE)]
    increase_after_break_list = [constants.START_VALUE_INCREASE]
    main_zones_list=[]

    for index in range(1, constants.END_RANGE_RED_ZONE):
        koef_for_red_zone = (Get_pseudorandom_coefficient(redzone_list[index-1], 3300, 10, 10))
        redzone_list.append(koef_for_red_zone + constants.START_TIME_RED)

    for index in range(1, constants.END_RANGE_GREEN_ZONE):
        koef_for_green_zone = Get_pseudorandom_coefficient(greenzone_list[index-1], 78900, 10, 10)
        increase_after_break_list.append(Get_pseudorandom_coefficient(increase_after_break_list[index-1], 300, 1, 1))
        unix_time_temp = koef_for_green_zone + constants.START_TIME_GREEN
        
        if (unix_time_temp > constants.START_BREAK and unix_time_temp < constants.END_BREAK):
            time_after_break = (constants.END_BREAK + increase_after_break_list[index-1])
            greenzone_list.append(time_after_break)
        else:
            greenzone_list.append(unix_time_temp)

    for index in range(1, constants.END_RANGE_BLUE_ZONE):
        koef_for_blue_zone = (Get_pseudorandom_coefficient(bluezone_list[index-1], 3300, 10, 10))
        bluezone_list.append(koef_for_blue_zone + constants.START_TIME_BLUE)


    # Ковертировать Unix в datatime. Вернуть datetime объект с информацией о часовом поясе.
    # Форматировать строку datatime в удобочитаемое. Обрезать до 3 милисекунд и добавить двоеточие.

    for index in itertools.chain(redzone_list, greenzone_list, bluezone_list):

        unix_convert_to_datatime = datetime.datetime.utcfromtimestamp(index)
        add_utc = unix_convert_to_datatime.astimezone()
        formatted_time = (add_utc.strftime(constants.FORMAT_FOR_DATATIME)[:23]+add_utc.strftime(constants.FORMAT_FOR_DATATIME)[26:])
        main_zones_list.append(formatted_time.replace('+0200', '+02:00'))
            
    return main_zones_list, redzone_list, greenzone_list, bluezone_list



def generate_change_date(creation_date_red_list, creation_date_green_list, creation_date_blue_list):

    increase_koef_list = [constants.START_VALUE_LIST]
    union_unix_list = [*creation_date_red_list, *creation_date_green_list, *creation_date_blue_list]
    change_date_list = []

    for index in range(len(union_unix_list)):

        if index == 0:
            value_unix_convert_to_dt = datetime.datetime.utcfromtimestamp(increase_koef_list[index] + union_unix_list[index])
        
        if index != 0:
            increase_koef_list.append(Get_pseudorandom_coefficient(increase_koef_list[index-1], 300, 1, 1))
            value_unix_convert_to_dt = datetime.datetime.utcfromtimestamp(union_unix_list[index] + increase_koef_list[index])
        
        add_utc = value_unix_convert_to_dt.astimezone()
        formatted_time = (add_utc.strftime(constants.FORMAT_FOR_DATATIME)[:23]+add_utc.strftime(constants.FORMAT_FOR_DATATIME)[26:])
        change_date_list.append(formatted_time.replace('+0200', '+02:00'))

    return change_date_list
    



def generate_initial_price():

    generate_price_function_start_value = {0 : Get_pseudorandom_coefficient(44.7791665112599, 135.95, 130.95, 130.95),      # USDJPY
                                           1 : Get_pseudorandom_coefficient(44.7791665112599, 1.25, 1.19, 1.19),            # GBPUSD
                                           2 : Get_pseudorandom_coefficient(44.7791665112599, 0.96, 0.91, 0.91),            # USDCHF
                                           3 : Get_pseudorandom_coefficient(44.7791665112599, 0.721, 0.6821, 0.6821),       # AUDUSD
                                           4 : Get_pseudorandom_coefficient(44.7791665112599, 1.0845, 1.0331, 1.0331),      # EURUSD
                                           5 : Get_pseudorandom_coefficient(44.7791665112599, 3.65, 3.2323, 3.2323),        # CADPLN
                                           6 : Get_pseudorandom_coefficient(44.7791665112599, 87.7, 80.65, 80.65),          # NZDJPY
                                           7 : Get_pseudorandom_coefficient(44.7791665112599, 1.7503, 1.603, 1.603),        # GBPCAD
                                           8 : Get_pseudorandom_coefficient(44.7791665112599, 0.6009, 0.5589, 0.5589),      # NZDCHF
                                           9 : Get_pseudorandom_coefficient(44.7791665112599, 7.11, 6.99, 6.99),            # MXNJPY
                                          10 : Get_pseudorandom_coefficient(44.7791665112599, 1.05, 0.9661, 0.9661),        # EURCHF
                                            }


    rows = 2500
    columns = 11
    mylist = [[0 for x in range(columns)] for x in range(rows)] 

    generate_price_function = {0 : partial(Get_pseudorandom_coefficient, upper_limit=140,   bottom_limit1=130.95, bottom_limit2=130.95), # USDJPY
                               1 : partial(Get_pseudorandom_coefficient, upper_limit=1.30,  bottom_limit1=1.12,   bottom_limit2=1.12),   # GBPUSD
                               2 : partial(Get_pseudorandom_coefficient, upper_limit=0.99,  bottom_limit1=0.9,    bottom_limit2=0.9),    # USDCHF
                               3 : partial(Get_pseudorandom_coefficient, upper_limit=0.720, bottom_limit1=0.670,  bottom_limit2=0.670),  # AUDUSD
                               4 : partial(Get_pseudorandom_coefficient, upper_limit=1.2,   bottom_limit1=1.03,   bottom_limit2=1.03),   # EURUSD
                               5 : partial(Get_pseudorandom_coefficient, upper_limit=3.7,   bottom_limit1=3.2323, bottom_limit2=3.2323), # CADPLN
                               6 : partial(Get_pseudorandom_coefficient, upper_limit=88,    bottom_limit1=80.65,  bottom_limit2=80.65),  # NZDJPY
                               7 : partial(Get_pseudorandom_coefficient, upper_limit=1.810, bottom_limit1=1.60,   bottom_limit2=1.60),   # GBPCAD
                               8 : partial(Get_pseudorandom_coefficient, upper_limit=0.65,  bottom_limit1=0.55,   bottom_limit2=0.55),   # NZDCHF
                               9 : partial(Get_pseudorandom_coefficient, upper_limit=7.11,  bottom_limit1=6.75,   bottom_limit2=6.75),   # MXNJPY
                              10 : partial(Get_pseudorandom_coefficient, upper_limit=1.09,  bottom_limit1=0.946,  bottom_limit2=0.946),  # EURCHF
                               }
    
    for i in range(rows):
        for j in range(columns):
            for key, function in generate_price_function_start_value.items():
                if key == j and i == 0:
                    mylist[i][j] = round(function,3)
                else:
                    for key1, function1 in generate_price_function.items():   
                        if key1 == j and i != 0:
                            mylist[i][j] = round(function1(start_value=(mylist[i - 1][j])*i*666666),3)

               
                    
    
    return mylist 

def main():
    
    # set_up_logger = configure_logging() 

    # db_connection = read_db_config()
    
    # connect_to_database = connect(set_up_logger)

    # execute_table = drop_and_create_table (connect_to_database)
    

    Hex_Id = generate_id_hex()
    Provider_Name = generate_provider()
    Direction_Name = generate_direction()
    Instrument_Name = generate_instrument()
    Creation_Date = generate_creation_date()
    

    creation_date_main_list = Creation_Date[0]
    creation_date_red_list = Creation_Date[1]
    creation_date_green_list = Creation_Date[2]
    creation_date_blue_list = Creation_Date[3]

    Change_Date = generate_change_date(creation_date_red_list, creation_date_green_list, creation_date_blue_list)
    Fill_price = generate_initial_price()[:-10]



    for index in range(0,70):
        print(#Hex_Id[index], Provider_Name[index], Direction_Name[index], Instrument_Name[index], 
              #creation_date_main_list[index], Change_Date[index], 
              Fill_price[index][0], Fill_price[index][1],
              Fill_price[index][2], Fill_price[index][3], Fill_price[index][4], Fill_price[index][5],
              Fill_price[index][6], Fill_price[index][7], Fill_price[index][8], Fill_price[index][9], Fill_price[index][10])



if __name__ == '__main__':
    main()
```



___

### *Constants*

```python
# Using for generation psevdorandom hex id

START_VALUE_GENERATION_ID = hex(4374977048)
INCREMENT_FOR_RANDOMNESS = 92832629




# Using for generation instrument

instrument_dictionary = {0: ['USDJPY'], 1: ['GBPUSD'], 2: ['USDCHF'],
                        3: ['AUDUSD'], 4: ['EURUSD'], 5: ['CADPLN'], 6: ['NZDJPY'],
                        7: ['GBPCAD'], 8: ['NZDCHF'], 9: ['MXNJPY'], 10: ['EURCHF']}

# Using for generation creation date

START_TIME_RED = 1669118400
START_TIME_GREEN = 1669122000
START_TIME_BLUE = 1669201200
START_BREAK = 1669158000
END_BREAK = 1669161600

START_VALUE_RED_ZONE = 1471.948678
START_VALUE_GREEN_ZONE = 2891.759427
START_VALUE_BLUE_ZONE = 1266.035704
START_VALUE_INCREASE = 97.310

END_RANGE_RED_ZONE = 375
END_RANGE_GREEN_ZONE = 1372
END_RANGE_BLUE_ZONE = 754

# Using for generation change date

START_VALUE_LIST = 82.7140802
FORMAT_FOR_DATATIME = '%Y-%m-%d %H:%M:%S.%f%z'
```


