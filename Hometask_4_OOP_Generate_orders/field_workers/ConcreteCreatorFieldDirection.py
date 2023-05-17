import constants as const

class ConcreteCreatorFieldDirection():

    def generate_value(self, context):
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['direction'], context['values']['scale_value']['direction'])
        next_generated_number = pseudorandom_data.next_generate()
        context['values']['start_value']['direction'] = next_generated_number

        return next(value for index,value in enumerate(const.DIRECTION_LIST) if index == round(next_generated_number))
    