# PHYS 203 Project

## Usage

Navigate to the `src` directory and run `python main.py <args>`. Call `main.py -h` for help.

## Overview
Simulation of ice-water transition with and without the presence of salt.
- Macroscopic descriptions of stability (internal energy, Gibbs free energy, entropy, etc.)
- Microscopic description of surface interaction at interface between water and ice

Investigate system around 0 to -20 degrees at atmospheric pressure (at least initially).
- Have parameters for pressure and temperature?

## Contributing

File structure:
```
src
|- utils
|    | - various packages (classes, functions, etc.)
|
|- main.py # Application entrypoint
|- (dependency management stuff)
```

How to make a change:
1. Make a feature branch
2. Commit changes to feature branch
3. Pull request feature branch to main branch
4. Ask for "code review"

## Considerations

Dimensionality problem:
- 2D simulation, 1D interface? Issues with degrees of freedom and structure of water
- 3D simulation, 2D interface (more difficult, but more accurate depiction)

Freezing brine ([phase diagram](https://www.tf.uni-kiel.de/matwis/amat/iss/kap_6/illustr/i6_2_2.html))
- Complicated, figure it out 
