
from environment import FizzBuzzEnvironment
from agent import QLearningAgent
from tqdm import tqdm
import sys
from inputValidation import validateInput
from plotter import Plotter


NUM_EPISODES = 30


def run_qlearning(lengthOfArray):
    env = FizzBuzzEnvironment(lengthOfArray)
    agent = QLearningAgent(env.dimension)
    table = Plotter()

    t = tqdm(range(NUM_EPISODES))

    for episode in t:
        state = env.reset() # get the initial state of the environment
        done = False        # boolean whether the episode has terminated
        error_count = 0

        while not done:
            action = agent.get_action(state)
            new_state, reward, done = env.step(action)
            agent.update(state, action, reward, new_state)
            state = new_state

            if env.FizzBuzz(state) != agent.get_final_results(state):
                error_count += 1

        table.addData("x", episode)
        table.addData("y", error_count)

    # Print out the final solution
    spaces = 8
    error_count = 0

    # Obtain errors when exclusively following the final greedy optimal policy.
    for x in range(0, lengthOfArray):
        if agent.get_final_results(x) != env.FizzBuzz(x) and x != lengthOfArray - 1:
            error_count += 1

    print("Simulation Complete")
    print("\nSummary of Optimal Policy:")
    print("Length of Array: " + str(lengthOfArray))
    print("Errors Detected: " + str(error_count))
    print("Final  Accuracy: " + str((1 - error_count / lengthOfArray) * 100) + "%")

    print("\nQ-Learning follows an e-greedy behavioural policy. So expect some errors even in the later stages of the simulation.")
    table.showPlot()

    wantsOutput = input("\nWould you like to view the individual results? (y/n) ")
    if wantsOutput == "y":
        print("  AGENT  |  ACTUAL")
        for x in range(0, lengthOfArray):
            print(f'{agent.get_final_results(x):<{spaces}} | {env.FizzBuzz(x)}')


if __name__ == "__main__":
    if validateInput(sys.argv):
        if (len(sys.argv) > 1):
            run_qlearning(int(sys.argv[1]))
        else:
            print("No number provided. Using default length of 100")
            run_qlearning(100)
