from Init_block.config_controller import ConfigController
from Init_block.ServiceLogger import LoggerSetup
from builders.DirectorForBuilders import Director
from pseudo_random_generators.PseudoRandomDataSource import PseudoRandomDataSource
from Init_block.ServiceMySQL import DatabaseProviderMySQL
import constants as const

class Main():

    def __init__(self):
        self.context = dict()

    def get_config(self):
        config_controller = ConfigController()
        config_controller._check_config_path()
        config_controller._validate()
        self.config = config_controller.config
        self.context['config'] = self.config
        
    def set_logger(self):
        service_logger = LoggerSetup()
        service_logger.setup(self.context['config']['logger']['level'], self.context['config']['logger']['log_file_name'])
        self.context['logger'] = service_logger.logger
        self.context['logger'].info("Logger Completed!")

    def workflow(self):
        records_collection = []
        self.history_records_collection = []
        self.context['pseudo_random_sources'] = PseudoRandomDataSource.get_instance()
        self.context['values'] = const.VALUES_FOR_PSEUDORANDOM_GENERATION
        director = Director(records_collection, self.history_records_collection, self.context)
        director.build_all_records()
        self.context['logger'].info(f"{len(self.history_records_collection)} rows in orders have been collected, ready to be inserted into the database")

    def connection_to_mysql(self):
        connection = DatabaseProviderMySQL()
        connection.output_in_MySQL(self.history_records_collection, self.context['logger'], self.context['config']['mysql'])
        
if __name__ == '__main__':
    main = Main()
    main.get_config()
    main.set_logger()
    main.workflow()
    main.connection_to_mysql()

   
