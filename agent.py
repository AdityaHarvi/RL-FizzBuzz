import numpy as np
from actionValues import ActionValueTable

OG_NUM, FIZZ, BUZZ, FIZZBUZZ = 0, 1, 2, 3 # agents actions
GAMMA = 0.99
STEP_SIZE = 0.25
EPSILON = 0.1


class QLearningAgent():
    def __init__(self, dimensions):
        self.actions = [OG_NUM, FIZZ, BUZZ, FIZZBUZZ]
        self.values = ActionValueTable(dimensions)
        self.gamma = GAMMA
        self.step_size = STEP_SIZE
        self.epsilon = EPSILON


    def update(self, state, action, reward, next_state, done):
        '''
        This function will update the values stored in self.value using Q-learning.

        HINT: Use self.values.get_value and self.values.set_value
        HINT: Remember to add a special case to handle the terminal state

        parameters:
            state : (list) a list of type [bool, int, int] where the first entry is whether the agent
            posseses the key, and the next two entries are the row and column position of the agent in
            the maze

            action : (int) the action taken at state

            reward : float

        returns:
            action : (int) a epsilon-greedy action for state
        '''
        current_action_value = self.values.get_value(state, action)
        greedy_action_value = self.values.get_value(next_state, self.get_greedy_action(next_state))

        new_action_value = current_action_value + self.step_size * (reward + self.gamma * greedy_action_value - current_action_value)
        self.values.set_value(state, action, new_action_value)

        return self.get_action(state)


    def get_action(self, state):
        '''
        This function returns an action from self.actions given a state.

        Implement this function using an epsilon-greedy policy.

        HINT: use np.random.rand() to generate random numbers
        HINT: If more than one action has maximum value, treat them all as the greedy action. In other words,
        if there are b greedy actions, each should have probability epsilon/b + |A|, where |A| is
        the number of actions in this state.

        parameters:
            state : (list) a list of type [bool, int, int] where the first entry is whether the agent
            posseses the key, and the next two entries are the row and column position of the agent in
            the maze

        returns:
            action : (int) a epsilon-greedy action for state

        '''
        should_pick_random_action = np.random.rand(1, 1)[0][0]

        if should_pick_random_action < self.epsilon:
            random_nums = np.random.rand(1, len(self.actions))[0]
            random_nums = [i for i, x in enumerate(random_nums) if x == max(random_nums)]
            return np.random.choice(random_nums)

        return self.get_greedy_action(state)


    def get_greedy_action(self, state):
        '''
        This function returns an action from self.actions given a state.

        Implement this function using a greedy policy, i.e. return the action with the highest value
        HINT: If more than more than one action has maximum value, uniformly randomize amongst them

        parameters:
            state : (list) a list of type [bool, int, int] where the first entry is whether the agent
            posseses the key, and the next two entries are the row and column position of the agent in
            the maze

        returns:
            action : (int) a greedy action for state
        '''
        action_values = [self.values.get_value(state, OG_NUM),
            self.values.get_value(state, FIZZ),
            self.values.get_value(state, BUZZ),
            self.values.get_value(state, FIZZBUZZ)]

        max_action_val_indexes = [i for i, x in enumerate(action_values) if x == max(action_values)]

        return np.random.choice(max_action_val_indexes)

    def get_final_results(self, state):
        action = self.get_greedy_action(state)

        if action == OG_NUM:
            return str(state + 1)
        elif action == FIZZ:
            return "Fizz"
        elif action == BUZZ:
            return "Buzz"
        else:
            return "FizzBuzz"
