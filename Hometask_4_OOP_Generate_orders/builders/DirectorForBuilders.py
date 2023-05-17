from builders.BuilderRecordAllZone import BuilderRecordAllZones
import constants as const
from nltk import flatten
import datetime 

class Director():

    def __init__(self, records_collection, ready_records_collection, context):
        self.records_collection = records_collection
        self.ready_records_collection = ready_records_collection
        self.context = context
        self.__temp_list = []
        self.builders_for_records = BuilderRecordAllZones()
        

    def build_all_records(self):
        red_zone_rows = round((int(self.context['config']['rows']['percent_of_redzone_strings']) / 100) * int(self.context['config']['rows']['total_rows']))
        green_zone_rows = round((int(self.context['config']['rows']['percent_of_greenzone_strings']) / 100) * int(self.context['config']['rows']['total_rows']))
        blue_zone_rows = round((int(self.context['config']['rows']['percent_of_bluezone_strings']) / 100) * int(self.context['config']['rows']['total_rows']))

        self.records_collection.append(const.NULL_STRING_ORDER) 
        self.context['logger'].info(f"Row calculation succeeded! We will get {red_zone_rows} Red zone lines, {green_zone_rows} Green zone lines, {blue_zone_rows} Blue zone lines")
                                    
        counter_status_lists = 0
        counter_zone_limit = 0
        for current_index in range(1, int(self.context['config']['rows']['total_rows'])):
            
            zones_list = [[red_zone_rows,                                      'RED_ZONE',   self.builders_for_records], 
                          [green_zone_rows + red_zone_rows,                    'GREEN_ZONE', self.builders_for_records], 
                          [blue_zone_rows + (green_zone_rows + red_zone_rows), 'BLUE_ZONE',  self.builders_for_records]]

            if counter_status_lists < zones_list[counter_zone_limit][0]:
            
                zones_list[counter_zone_limit][2].setup_builder(self.context, self.records_collection[-1], zones_list[counter_zone_limit][1])
                self.__ready_order = zones_list[counter_zone_limit][2].get_ready_order()
                self.__format_to_datatime(self.__ready_order['create_date'])
                self.__unpack_into_ready_order(self.__ready_order)
                self.records_collection.append(self.__ready_order)
                counter_status_lists += len(self.records_collection[-1]['status'])
            
            if current_index == (zones_list[counter_zone_limit][0]):
                    counter_zone_limit += 1
            

    def __unpack_into_ready_order(self, records_collection):

        for index_list, status_list in enumerate(records_collection['status']):
            flattened_list = flatten(records_collection['status'][index_list])
            
            self.__temp_list = [records_collection['id'], records_collection['provider'], records_collection['direction'], records_collection['instrument'], 
                                records_collection['create_date'], flattened_list[1], flattened_list[0], records_collection['initial_price'], flattened_list[2], 
                                records_collection['initial_volume'], flattened_list[3], records_collection['tags'], records_collection['description'], records_collection['extra_data']]
            
            self.ready_records_collection.append(self.__temp_list)
            
      
    def __format_to_datatime(self, unix_time):

        unix_convert_to_datatime = datetime.datetime.utcfromtimestamp(unix_time).astimezone()
        formatted_time = (unix_convert_to_datatime.strftime(const.FORMAT_FOR_DATATIME)[:const.LEAVE_23_CHARACTERS_FIRST] + 
                          unix_convert_to_datatime.strftime(const.FORMAT_FOR_DATATIME)[const.LEAVE_26_CHARACTERS_END:]).replace(const.UTC_FORMAT, const.UTC_EXCEL_FORMAT)
        
        self.__ready_order['create_date'] = formatted_time
        
        