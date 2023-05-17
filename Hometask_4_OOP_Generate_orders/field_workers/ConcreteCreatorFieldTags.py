import constants as const

class ConcreteCreatorFieldTags():

    def generate_value(self, provider_value):
        return next(value for key, value in const.DICT_TAGS.items() if key == provider_value)
