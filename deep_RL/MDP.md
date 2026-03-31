# Markov Decision Process (MDP)

A mathematical model that models agents interacting with an environment with uncertainty. 

It has the following components:

1. state
2. action 
3. transition model
4. reward
5. policy

Discounting is the idea that we care more about immediate rewards rather then future ones. It is used
to ensure convergence of infinite-horizon return. It takes value between 0 and 1. A higher value means that we care more about future rewards, while a lower value means that we care more about immediate rewards. 

Solving MDPs:

Assuming we have access to all dynamics information, i.e. the transition and reward. Two algotirhms can be used to solve MDPs:

1. Value iteration
2. Policy iteration 

Both are offline learning methods

## value iteration

