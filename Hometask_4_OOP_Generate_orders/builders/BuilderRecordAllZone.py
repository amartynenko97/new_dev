from interfaces.Builder import Builder
from field_workers.ConcreteCreatorFieldID import ConcreteCreatorFieldID
from field_workers.ConcreteCreatorFieldProviderID import ConcreteCreatorFieldProviderID
from field_workers.ConcreteCreatorFieldDirection import ConcreteCreatorFieldDirection
from field_workers.ConcreteCreatorFieldInstrument import ConcreteCreatorFieldInstrument
from field_workers.ConcreteCreatorFieldCreateDate import ConcreteCreatorFieldCreateDate
from field_workers.ConcreteCreatorFieldChangeDate import ConcreteCreatorFieldChangeDate
from field_workers.ConcreteCreatorFieldStatus import ConcreteCreatorFieldStatus
from field_workers.ConcreteCreatorFieldInitialPrice import ConcreteCreatorFieldInitialPrice
from field_workers.ConcreteCreatorFieldFillPrice import ConcreteCreatorFieldFillPrice
from field_workers.ConcreteCreatorFieldInitialVolume import ConcreteCreatorFieldInitialVolume
from field_workers.ConcreteCreatorFieldFillVolume import ConcreteCreatorFieldFillVolume
from field_workers.ConcreteCreatorFieldTags import ConcreteCreatorFieldTags
from field_workers.ConcreteCreatorFieldDescription import ConcreteCreatorFieldDescription
from field_workers.ConcreteCreatorFieldExxtraData import ConcreteCreatorFieldExxtraData
import constants as const

class BuilderRecordAllZones(Builder):

    def setup_builder(self, context, prev_order, zone_name):

        self.zone_name = zone_name
        self.context = context
        self.prev_order = prev_order
        self.current_order = {} 
        self.field_id = ConcreteCreatorFieldID()
        self.field_provider_id = ConcreteCreatorFieldProviderID()
        self.field_direction = ConcreteCreatorFieldDirection()
        self.field_instrument = ConcreteCreatorFieldInstrument()
        self.field_create_date = ConcreteCreatorFieldCreateDate()
        self.field_change_date = ConcreteCreatorFieldChangeDate()
        self.field_status = ConcreteCreatorFieldStatus()
        self.field_initial_price = ConcreteCreatorFieldInitialPrice()
        self.field_fill_price = ConcreteCreatorFieldFillPrice()
        self.field_initial_volume = ConcreteCreatorFieldInitialVolume()
        self.field_fill_volume = ConcreteCreatorFieldFillVolume()
        self.field_tags = ConcreteCreatorFieldTags()
        self.field_description = ConcreteCreatorFieldDescription()
        self.field_extra_data = ConcreteCreatorFieldExxtraData()
        
    def get_ready_order(self):

        self.current_order['id'] = self.field_id.generate_value(self.context, self.prev_order['id'])
        self.current_order['provider'] = self.field_provider_id.generate_value(self.context)
        self.current_order['direction'] = self.field_direction.generate_value(self.context)
        self.current_order['instrument'] = self.field_instrument.generate_value(self.context)
        self.current_order['create_date'] = self.field_create_date.generate_value(self.context, self.zone_name)
        self.current_order['initial_price'] = self.field_initial_price.generate_value(self.context, self.current_order['instrument'])
        self.current_order['initial_volume'] = self.field_initial_volume.generate_value(self.context)
        self.current_order['tags'] = self.field_tags.generate_value(self.current_order['provider'])
        self.current_order['description'] = self.field_description.generate_value(self.zone_name)
        self.current_order['extra_data'] = self.field_extra_data.generate_value(self.current_order['direction'])
        self.current_order['status'] = self.field_status.generate_value(self.context, self.zone_name)
        self.__fill_status_dependent_values(self.current_order['status'])
        
        return self.current_order


    def __generate_status_list_empty_values(self, temp, order_list, index_list):

        order_list[index_list][1] = self.field_change_date.generate_value(index_list, self.current_order['create_date'], 
                                                                                  order_list[index_list-1][1], self.context['values']['start_value']['create_date'])
                
        order_list[index_list][2] = self.field_fill_price.generate_value(order_list[index_list], order_list[temp], self.current_order['initial_price'])
                                                                        
        order_list[index_list][3] = self.field_fill_volume.generate_value(self.context['values']['start_value']['initial_volume'], 
                                                                        order_list[index_list], order_list[temp], order_list[index_list-1][3], self.current_order['initial_volume'])
       
    def __fill_status_dependent_values(self, order_list):
         
        for index_list, status_list in enumerate(order_list):
            if index_list == 0:
                self.__generate_status_list_empty_values(index_list, order_list, index_list)
            else:
                self.__generate_status_list_empty_values(index_list-1, order_list, index_list)
                 
       
       