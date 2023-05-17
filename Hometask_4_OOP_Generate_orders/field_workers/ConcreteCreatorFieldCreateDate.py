import constants as const

class ConcreteCreatorFieldCreateDate():

    def generate_value(self, context, zone_name):
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['create_date'], context['values']['scale_value']['create_date'])
        next_generated_number = pseudorandom_data.next_generate()
        
        context['values']['start_value']['create_date'] = next_generated_number
        next_pseudorandom_koef = ((const.ORDER_EXECUTION_TIME[0] - const.ORDER_EXECUTION_TIME[1]) * next_generated_number + const.ORDER_EXECUTION_TIME[1])

        for key, values in const.UNIX_DICT.items():
            if zone_name == key:
                if(isinstance(values, list)):
                    unix_time = round((((values[0] - values[1]) + values[2]) * next_generated_number) + values[3], 3)
                    if unix_time  > const.START_BREAK and unix_time  < const.END_BREAK:
                        unix_time = round((const.END_BREAK + next_pseudorandom_koef), 3)   
                    
        return unix_time 
        
