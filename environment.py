import numpy as np

OG_NUM, FIZZ, BUZZ, FIZZBUZZ = 0, 1, 2, 3 # agents actions

class FizzBuzzEnvironment():
    def __init__(self, lengthOfArray):
        self.start = 0
        self.end = lengthOfArray - 1

        self.loc = self.start  # the location of the agent

        self.max_state = lengthOfArray
        self.dimension = [lengthOfArray + 1, 4]


    def reset(self):
        self.loc = self.start
        return self.loc


    def FizzBuzz(self, state):
        currentState = state + 1 # Increase state by 1 to get numeric value.

        rtnValue = ""
        if currentState % 3 == 0:
            rtnValue += "Fizz"
        if currentState % 5 == 0:
            rtnValue += "Buzz"

        if rtnValue != "":
            return rtnValue
        return str(currentState)


    def performAction(self, action, state):
        if action == OG_NUM:
            return str(state + 1)
        elif action == FIZZ:
            return "Fizz"
        elif action == BUZZ:
            return "Buzz"
        else:
            return "FizzBuzz"


    def step(self, action):
        # Check if the action performed was the correct choice
        if self.performAction(action, self.loc) == self.FizzBuzz(self.loc):
            reward = 1
        else:
            reward = -1

        self.loc += 1
        is_done = False

        if self.loc == self.max_state:
            is_done = True

        return self.loc, reward, is_done
