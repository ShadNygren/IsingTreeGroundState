import numpy as np

def ising_tree_bp(J, h):
    # initialize messages
    N = len(J)
    messages = [np.zeros_like(J[i]) for i in range(N)]
    beliefs = np.zeros(N)

    # perform message passing
    for i in range(N):
        # send message from node i to its neighbor j
        for j in range(N):
            if J[i, j] != 0:
                messages[i][j] = np.tanh(J[i, j] * beliefs[i] + h[i])

        # update belief for node i
        beliefs[i] = h[i] + sum(messages[i])

    # compute minimum energy and node states
    energy = 0
    states = np.zeros(N)
    for i in range(N):
        energy += -0.5 * np.dot(J[i], messages[i]) - h[i] * beliefs[i]
        states[i] = np.sign(beliefs[i])

    # print results
    print("Node states:", states)
    print("Minimum energy:", energy)

    return states, energy


J = np.array([[0, 1, 0, 0],
              [1, 0, 1, 1],
              [0, 1, 0, 1],
              [0, 1, 1, 0]])

h = np.array([0.5, -0.2, 0.3, -0.1])

ising_tree_bp(J, h)
