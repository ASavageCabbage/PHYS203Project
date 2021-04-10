# PHYS 203 Project

## Usage

Navigate to the `src` directory and run `python main.py <args>`. Call `main.py -h` for help.

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

## Simulation structure

Salt-water-ice [phase diagram](https://www.tf.uni-kiel.de/matwis/amat/iss/kap_6/illustr/i6_2_2.html))
- Try to replicate top-left corner: interaction between liquid+solid and liquid

Simulation components:
- Phase objects: ice, water, salt
- Reservoir to act as a heat bath and calorimeter (tallying heat flow)
- Sub-system to handle mixing between water and salt (enthalpy of dissolution, entropy of mixing, etc)
- Iterator to find optimal global state via gradient descent

The goal is to recreate the phase diagram linked above near the regime where salt water is liquid and unsaturated.

## Notes

Internal Energy/Entropy of Water/Ice
- tabulate on per-molar basis, assume this is roughly constant with temperature?
- calculate changes in temperature by assuming constant heat capacity, use function to model?
- use enthalpy of formation to determine energy of water/ice?
- we need to make sure all quatities are measured relative to the same point

Changes in salt concentration
- things will dilute as ice melts, which maybe changes internal energy of saltwater in a weird way
    - UPDATE: the plan is to account for this, just treat it like adding U of pure water
- assume salt concentrations are low enough that the change in energy is same for all volumes
    - UPDATE: everything is now done per mole, this is not an issue
- how can we calculate the affect on entropy? use entropy of mixing, neglect energy affects?
    - this general idea, maybe assume the energy released during mixing doesn't affect temperature?

Heat flow --> Low priority, implement last
- maybe use thermal conductivity to model spontaneous heat flow?
- equation 2: https://en.wikipedia.org/wiki/Thermal_contact_conductance
- also maybe useful: https://phas.ubc.ca/~kiefl/ch15_part2.pdf

Heat capacity
- taking the heat capacity in steps might fail for large temperature changes

General ideas
- main idea with phase is to compute the chemical potential (sort of, change in gibbs from adding
- or removing a mole) and have system use that to get probability of bond breaking
- bonds breaking is done by pulling/adding energy to different phases
- everything is done with pressure assumed to be constant, heat capacity assumed to be constant
- with respect to temperature
- heat capacity is used to compute changes in entropy from heat
- salt assumed to only dissolve in water

Data
- Here's some interesting supercooled water data (no heat capacity sadly)
- http://hbcponline.com/faces/documents/06_44/06_44_0001.xhtml

## Unresolved Issues
- currently unknown whether an animation object works in a static class