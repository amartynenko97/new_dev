import constants as const
from mysql.connector import Error, MySQLConnection


class DatabaseProviderMySQL():

    def output_in_MySQL(self, data_for_output, logger, database_config):
        try:
            connection = MySQLConnection(**database_config)
            if connection.is_connected():
                db_Info = connection.get_server_info()
                logger.info("Connected to MySQL Server version %s" % db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                logger.info("You're connected to database: %s" % record)
                all_orders_string_for_output_in_database = str(tuple(data_for_output[0]))
                
                for index in range(1, len(data_for_output)):
                    all_orders_string_for_output_in_database += ', ' + str(tuple(data_for_output[index]))
                formatted_sql_query = const.INSERT_QUERY + all_orders_string_for_output_in_database
                connection._execute_query(formatted_sql_query)
                connection.commit()       
                logger.info("Data successfully added to the database")
                
        except Error:
            logger.critical(Error)

        finally:
            if connection.is_connected():
                connection.close()
                logger.info("MySQL connection is closed")    