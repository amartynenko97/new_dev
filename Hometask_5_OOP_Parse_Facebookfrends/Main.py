from ConfigController import ConfigController
from LoggerSetup import LoggerSetup
import pandas
from collections import defaultdict
from AuthorizationFacebookStage import AuthorizationFacebook  
from ParseInfoFromFrendsListStage import ParseInfoFromFrendsList   

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
        
    def workflow(self):
        self.details_collection = defaultdict(list)
        authorization = AuthorizationFacebook(email=self.context['config']['credentials']['email'], 
                                              password=self.context['config']['credentials']['password'],
                                              driver_path=self.context['config']['driver']['path_driver'],
                                              logger=self.context['logger'])
        authorization.facebook_login()
        self.context['driver'] = authorization.driver
        self.context['wait'] = authorization.wait
        search_information = ParseInfoFromFrendsList()
        search_information.parse_links_from_frends_list(driver=self.context['driver'], 
                                                        wait=self.context['wait'], 
                                                        logger=self.context['logger'],
                                                        collection_facebook=self.details_collection,
                                                        total_profiles=int(self.context['config']['parser']['amount_of_friends']))
        df = pandas.DataFrame(self.details_collection)
        self.context['logger'].info(f"The necessary information was collected from {len(df)} profiles")
        print(df)
        self.context['driver'].close()
        self.context['driver'].quit()
            
if __name__ == '__main__':
    main = Main()
    main.get_config()
    main.set_logger()
    main.workflow()














       