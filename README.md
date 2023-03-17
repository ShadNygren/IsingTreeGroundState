# Ising Tree Ground State

This is an implementation of Belief Propagation algorithm in Python that solves the Ising Tree Ground State problem and prints the state of each node and the Minimum Energy.

The function ising_tree_bp takes as input two numpy arrays: J, the coupling matrix, and h, the external magnetic field. It returns the state of each node and the minimum energy.

To use this function, you can define the J and h matrices for your Ising Tree problem and then call ising_tree_bp.

As currently written this will output the following:

Node states: [ 1. -1. -1.  1.]  
Minimum energy: -1.3

The node states correspond to the ground state of the Ising Tree problem, and the minimum energy is the energy of the ground state.
