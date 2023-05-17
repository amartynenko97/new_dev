import constants as const

class ConcreteCreatorFieldStatus():

    def generate_value(self, context, zone_name):
        pseudorandom_data = context['pseudo_random_sources']
        pseudorandom_data.setup(context['values']['start_value']['status'], context['values']['scale_value']['status'])
        next_generated_number = pseudorandom_data.next_generate()
        context['values']['start_value']['status'] = next_generated_number
        for zone_names, list_of_status in const.DICT_STATUS_GENERATE_ALL_ZONES.items():
            if zone_name == zone_names:
                for number_list, list_correct_status in list_of_status.items():
                    if round(next_generated_number * list_correct_status[1]) == number_list:
                        temp_list = list_correct_status[0]
                        self.__value = []
                        for status in temp_list:
                            self.__value.append([status, 0, 0, 0])
                        return self.__value
                    