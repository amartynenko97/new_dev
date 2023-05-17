import constants as const

class ConcreteCreatorFieldExxtraData():

    def generate_value(self, direction_name):
        return next(value for key, value in const.DICT_EXTRA_DATA.items() if key == direction_name)