import constants as const

class ConcreteCreatorFieldChangeDate():

    def generate_value(self, index_status, current_create_date, prev_record_date, next_pseudorandom_koef):

        unix_time = ((const.ORDER_EXECUTION_TIME[0] - const.ORDER_EXECUTION_TIME[1]) * next_pseudorandom_koef + const.ORDER_EXECUTION_TIME[1])
        
        if index_status == 0: return round(current_create_date + unix_time, 3)
            
        elif index_status <= 3: return round(prev_record_date + unix_time, 3)
            
         
