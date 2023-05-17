import constants as const

class ConcreteCreatorFieldFillVolume():

    def generate_value(self, multiplier_next_generated_number, current_status_list, prev_status_list, prev_record_fill_price, current_initial_price):

        part_check = const.PART_FILL_KOEFICIENTS.setdefault(const.FILL_VOLUME_STATUSES_INDEXES[current_status_list[0]],
                                                             multiplier_next_generated_number)
        
        if (prev_status_list[0] == const.STATUS[0] and current_status_list[0] == const.STATUS[1]):
            return 0
        
        elif (prev_status_list[0] == const.STATUS[2] and current_status_list[0] == const.STATUS[1]):
            return prev_record_fill_price
        
        else:
            if round(part_check * current_initial_price, 3) == 0:
                return 0 
            return round(part_check * current_initial_price, 3)
