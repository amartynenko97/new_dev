import constants as const

class ConcreteCreatorFieldInstrument():

    def generate_value(self, context):
            pseudorandom_data = context['pseudo_random_sources']
            pseudorandom_data.setup(context['values']['start_value']['instrument'], context['values']['scale_value']['instrument'])
            next_generated_number = pseudorandom_data.next_generate()
            context['values']['start_value']['instrument'] = next_generated_number
        
            return next(value for index,value in enumerate(const.INSTRUMENT_LIST) if index == round(next_generated_number * 10))