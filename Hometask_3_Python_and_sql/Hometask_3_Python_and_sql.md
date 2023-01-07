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


### *Writing Code*

***Points to remember***

*`is_connected()` — это метод класса `MySQLConnection`, с помощью которого мы можем проверить, подключено ли наше приложение Python к MySQL.*
*Наконец, мы закрываем соединение с базой данных MySQL, используя метод `close()` класса `MySQLConnection`.*


*Создание экземпляра класса `cursor` который используется для выполнения `SQL` инструкции в `Python`*


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