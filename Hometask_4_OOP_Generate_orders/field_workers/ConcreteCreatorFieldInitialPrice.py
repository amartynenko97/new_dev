import constants as const

class ConcreteCreatorFieldInitialPrice():

    def generate_value(self, context, instrument_name):
        
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['initial_price'], context['values']['scale_value']['initial_price'])
        next_generated_number = pseudorandom_data.next_generate()
        context['values']['start_value']['initial_price'] = next_generated_number
        for instrument, values in const.DICT_PRICES.items():
            if instrument == instrument_name:

                return round((((values[0] - values[1]) * next_generated_number + values[1])), 3)

               
            