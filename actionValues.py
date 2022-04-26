import numpy as np

class ActionValueTable():
    def __init__(self, dimensions):
        '''
        Creates a table of size array_length * 4.
        Each state will have 4 actions:
            1) Return the number given
            2) Return 'fizz'
            3) Return 'buzz'
            4) Return 'fizzbuzz'
        '''
        self.table = np.zeros(dimensions)


    def get_value(self, state, action):
        '''
        Returns the value for a (state, action) pair
        '''
        return self.table[state - 1, action]


    def set_value(self, state, action, new_value):
        '''
        Set the value for a (state, action) pair to new_value
        '''
        self.table[state - 1, action] = new_value
