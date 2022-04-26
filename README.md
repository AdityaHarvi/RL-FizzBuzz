<p align="center">
  <img src="https://user-images.githubusercontent.com/45128157/165376538-f4852c10-9d49-4a13-a09b-fd83766d4a90.png"/>
</p>

# FizzBuzz is HARD, so I made a RL agent do it instead
This agent utilizes a Q-Learning algorithm to learn the proper actions to perform in this problem.
This mini project was mainly used as a learning opportunity for how to train RL agents.

## Prerequisites
- Ensure you have python installed
- Install the libraries needed for this project with `pip3 install -r preReqs.txt`

## Running Instructions
- To run the program use `python3 simulation.py <optional: number>`
  - The optional number represents how far you wish to go up to. For example `python3 simulation.py 500` will make the agent train from 1 to 500.
  - If no number is provided, the agent will train on a default value of 100.

By default, the agent runs 1000 episodes. This can be modified by changing the `NUM_EPISODES` value in `simulation.py`.
