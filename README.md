# PHYS 203 Project

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
- How do we figure out a probability of bond breaking? (seems to be no tables on this)

Freezing brine ([phase diagram](https://www.tf.uni-kiel.de/matwis/amat/iss/kap_6/illustr/i6_2_2.html))
- Complicated, figure it out

Internal Energy/Entropy of Water/Ice
- tabulate on per-molar basis, assume this is roughly constant with temperature?
- calculate changes in temperature by assuming constant heat capacity, use function to model?
- use enthalpy of formation to determine energy of water/ice?

Changes in salt concentration
- things will dilute as ice melts, which maybe changes internal energy of saltwater in a weird way?
- assume salt concentrations are low enough that the change in energy is same for all volumes?
- how can we calculate the affect on entropy? use entropy of mixing, neglect energy affects?

Chemical potential
- do we need to factor it in? I don't think so

General ideas
- main idea with phase is to compute the chemical potential (sort of, change in gibbs from adding
- or removing a mole) and have system use that to get probability of bond breaking
- bonds breaking is done by pulling/adding energy to different phases
- everything is done with energy/mole, pressure, heat capacity assumed to be constant
- heat capacity is used to compute changes in entropy
