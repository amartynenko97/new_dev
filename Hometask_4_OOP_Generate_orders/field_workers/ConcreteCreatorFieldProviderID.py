import constants as const

class ConcreteCreatorFieldProviderID():

    def generate_value(self, context):
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['provider'], context['values']['scale_value']['provider'])
        next_generated_number = pseudorandom_data.next_generate()
        context['values']['start_value']['provider'] = next_generated_number

        return next(value for index,value in enumerate(const.PROVIDER_LIST) if index == round(next_generated_number))
    
       