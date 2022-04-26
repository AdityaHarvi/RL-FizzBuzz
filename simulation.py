
from environment import FizzBuzzEnvironment
from agent import QLearningAgent
from tqdm import tqdm
import sys
from inputValidation import validateInput


NUM_EPISODES = 1000


def run_qlearning(lengthOfArray):
    env = FizzBuzzEnvironment(lengthOfArray)
    agent = QLearningAgent(env.dimension)

    t = tqdm(range(NUM_EPISODES))

    for _ in t:
        state = env.reset() # get the initial state of the environment
        done = False        # boolean whether the episode has terminated

        while not done:
            action = agent.get_action(state)
            new_state, reward, done = env.step(action)
            agent.update(state, action, reward, new_state)
            state = new_state

    # Print out the final solution
    spaces = 8
    error_count = 0

    for x in range(0, lengthOfArray):
        if agent.get_final_results(x) != env.FizzBuzz(x) and x != lengthOfArray - 1:
            error_count += 1

    print("Simulation Complete")
    print("\nSUMMARY:")
    print("Length of Array: " + str(lengthOfArray))
    print("Errors Detected: " + str(error_count))
    print("Agent  Accuracy: " + str((1 - error_count / lengthOfArray) * 100) + "%")

    wantsOutput = input("\nWould you like to view the individual results? (y/n) ")
    if wantsOutput == "y":
        print("  AGENT  |  ACTUAL")
        for x in range(0, lengthOfArray):
            print(f'{agent.get_final_results(x):<{spaces}} | {env.FizzBuzz(x)}')
    else:
        print("Program complete")


if __name__ == "__main__":
    if validateInput(sys.argv):
        if (len(sys.argv) > 1):
            run_qlearning(int(sys.argv[1]))
        else:
            print("No number provided. Using default length of 100")
            run_qlearning(100)
