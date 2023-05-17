import constants as const


class ConcreteCreatorFieldID():

    def generate_value(self, context, prev_hex_number):
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['id'], context['values']['scale_value']['id'])
        next_generated_number = pseudorandom_data.next_generate()
        context['values']['start_value']['id'] = next_generated_number
        hex_number = (hex(round(next_generated_number * const.INCREMENT_FOR_RANDOMNESS) + 
                                     int(prev_hex_number, 16)).lstrip("0x").upper().zfill(10))

        return hex_number



    