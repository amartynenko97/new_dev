from constants import *
import math


class PseudoRandomDataSource:
    instance = None
    
    @classmethod
    def get_instance(cls): 
        if not cls.instance:
            cls.instance = cls()
        return cls.instance
    
    def next_generate(self):
        self.value = (1/math.pi * math.acos(math.cos(((self.value) * self.scale))) * 
                                    (self.range_high - self.range_low ) + self.range_low )
        
        return self.value

    def setup(self, new_value, scale):
        self.value = new_value
        self.range_low = GENERATOR_RANGE_LOW
        self.range_high = GENERATOR_RANGE_HIGH
        self.scale = scale
        
