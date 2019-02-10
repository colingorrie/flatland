# Flatland

We want to create an artificial life simulator, under the following constraints:

- the world will be a 2d grid
  - grid size:
    - big enough to be interesting
    - small enough to be performant on our machines
    - 64x64?
  - boundary conditions
    - periodic identification (looping)
    - Dirichlet (constant) / Von Neumann conditions
- we want to model predator-prey relationships
- we want to simulate evolution
  - genetic programming, specifically the representation of programs as tree structures that are mutated and recombined in a way that mimics biological processes
- we want to simulate behaviour

Technically:

- we want to use Python for the simulation
  - `pandas`
  - `numpy`
- we will probably use a web frontend
  - `vue`
- handle communication between simulation and the UI via websockets

## Goal

Make it fun above all else!

- non-trivial
- chaotic
- doesn't terminate too quickly
- equilibrium
