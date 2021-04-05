## class handling the interplay of different distinct phases in a system
## Last updated: 02/05/2021

import phases
import absolute
import differential

class System:

    def __init__(self, liquid, solid, step=0, area=0):
        self.liquid = liquid # liquid phase
        self.solid = solid # solid phase
        self.step = step # time step with each tick, TODO update the default
        self.area = area # area of the interface between phases, TODO update the default

    # moves forwards a time step
    def tick(self):
        u_liquid, u_solid = self.calc_chem_potentials()
        rate = self.calc_rate()
        probability = self.calc_probability(u_liquid, u_solid)
        net_liquid, net_solid = self.net_movement(rate, probability)
        net_q_liquid, net_q_solid = self.net_heat((net_liquid, net_solid))
        self.update_phases((net_liquid, net_solid), (net_q_liquid, net_q_solid))

    # calculates the chemical potential of each phase, by testing the change
    # in gibbs free energy that results from adding one mole
    # TODO: Just a reminder to switch to deep copy if needed
    def calc_chem_potentials(self):
        # this seems like a dumb way to do this, but it's a low cost copy
        # so it should be fine
        (liquid_copy, solid_copy) = (self.liquid.copy(), self.solid.copy())
        (G_0_liquid, G_0_solid) = (liquid_copy.G, solid_copy.G)
        liquid_copy.add_moles(1)
        solid_copy.add_moles(1)
        (G_1_liquid, G_1_solid) = (liquid_copy.G, solid_copy.G)
        return (G_1_liquid - G_0_liquid, G_1_solid - G_0_solid)

    # calculates the rate at which particles attempt to go from solid to liquid,
    # and vice versa, using area, number of particles in each phase, temperature
    # and the activation energy of breaking a bond in the solid
    # this assumes that particles "attempt" to cross from liquid to solid and vice
    # versa at the same rate, and deals with the fact that they don't in the
    # probability of success
    # TODO: How would one actually calculate this?
    def calc_rate(self):
        return 0

    # calculates the probability of a "free" particle moving into the solid
    # based on the chemical potential
    # TODO: Again, how would one actually do this?
    def calc_probability(self, u_liquid, u_solid):
        return 0

    # calculates the net moles of particles moving into the liquid and solid
    def net_movement(self, rate, probability):
        attempted = rate*self.step/2 # amount of particles that each phase "loses"
        to_solid = rate*probability*self.step # num of particles that go into the solid
        to_liquid = rate*(1-probability)*self.step
        return (to_liquid-attempted, to_solid-attempted)

    # calculates the neat heat flow into each phase due to temperature difference from
    # conduction (which we have to use assuming a uniform fluid) 
    # also adds on heat flow due to energy required to break/form bonds in solid
    # equation 2 here is good https://en.wikipedia.org/wiki/Thermal_contact_conductance
    # TODO: this method
    def net_heat(self particle_flow):
        pass

    # inputs the particle and heat flow into the phases
    def update_phases(self, particle_flow, heat_flow):
        self.liquid.add_moles(particle_flow[0])
        self.solid.add_moles(particle_flow[1])
        self.liquid.add_heat(heat_flow[0])
        self.solid.add_heat(heat_flow[1])

    # adds n moles of salt to the liquid
    def add_salt(self,n):
        self.liquid.add_salt(n)
    
    # adds n moles of liquid into the system
    def add_liquid(self,n):
        self.liquid.add_moles(n)

    # adds n moles of liquid into the system
    def add_solid(self,n):
        self.solid.add_moles(n)
        