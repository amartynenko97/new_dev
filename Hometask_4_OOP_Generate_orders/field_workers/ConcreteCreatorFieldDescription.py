import constants as const

class ConcreteCreatorFieldDescription():

    def generate_value(self, zone_name):
        return next(value for key, value in const.DICT_DESCRIPTION.items() if key == zone_name)
    
