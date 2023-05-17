import constants as const

class ConcreteCreatorFieldInitialVolume():

    def generate_value(self, context):
        
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['initial_volume'], context['values']['scale_value']['initial_volume'])
        next_generated_number = pseudorandom_data.next_generate()
        context['values']['start_value']['initial_volume'] = next_generated_number

        return round((((const.VOLUME_LIST[0] - const.VOLUME_LIST[1]) * next_generated_number + const.VOLUME_LIST[1])), 3)
        
       