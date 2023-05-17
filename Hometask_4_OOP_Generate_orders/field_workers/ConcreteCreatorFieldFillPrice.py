import constants as const

class ConcreteCreatorFieldFillPrice():

    def generate_value(self, current_status_list, prev_status_list, current_initial_price):
        
        koeficient_by_status = const.CHECK_PREV_REJECT_STATUS[prev_status_list[0] == const.STATUS[0] and current_status_list[0] == const.STATUS[1]]
        if (const.CHECK_DEPENDMENT_STATUS[koeficient_by_status]):
            koeficient_by_status = const.FILL_PRICE_BY_STATUS[current_status_list[0]]
            if koeficient_by_status == 0:
                return 0
            
        return round(current_initial_price * koeficient_by_status, 3)

       
            
       
                
    
                    

      