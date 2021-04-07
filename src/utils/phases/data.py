# TODO: Manually calculate the heat of formation and standard entropy for
# ice at STP

# Helper functions
def find_nearest_value(key, table):
    '''
    Returns value corresponding to the nearest key in the table
    Assumes input key and keys in table are numeric
    '''
    ordered_keys = list(table.keys())
    if key in ordered_keys:
        return table[key]
    
    ordered_keys.sort()
    smaller = [i for i, item in enumerate(ordered_keys) if item < key]
    if len(smaller) > 0:
        prev = smaller[-1]
    else:
        prev = len(ordered_keys) - 1
    before = ordered_keys[prev]
    try:
        after = ordered_keys[prev + 1]
        if key - before < after - key:
            key = before
        else:
            key = after
    except IndexError:
        key = before
    return table[key]

# tables of constants

# Standard temperatures (K)
SATP_T = 298
STP_T = 273

# Standard pressure (Pa)
STP_P = 101325

# Molar concentration of pure water (mol/m^3)
LIQUID_WATER_MOLAR_CONC = 55.5e-3

# Standard molar enthalpy of formation (J/mol)
LIQUID_WATER_HF = -285830

# Standard molar enthalpy of formation (J/mol)
ICE_HF = 0 # TODO: Find this

# Standard salt enthalpy of formation (J/mol)
# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7647145&Mask=6F
SALT_HF = -411120

# Standard enthalpy of solution for salt (J/mol) (infinitely dilute solution)
# http://hbcponline.com/faces/documents/05_13/05_13_0005.xhtml
SALT_SOLUTION_H = 3880

# Standard molar entropy of H2 (J/mol K) (all from NIST)
GAS_H_S = 130.68

# Standard molar entropy of 02 (J/mol K)
GAS_O_S = 205.15

# Standard molar entropy of Na (J/mol K)
SOLID_NA_S = 51.46

# Standard molar entropy of Cl2 (J/mol K)
GAS_CL_S = 223.08

# Standard molar entropy of NaCl (J/mol K)
SOLID_SALT_S = 72.11

# Standard molar entropy of formation of salt (J/mol K)
SOLID_SALT_SR = SOLID_SALT_S - SOLID_NA_S - GAS_CL_S/2

# Standard molar entropy of liquid water (J/mol K)
LIQUID_WATER_S = 69.95

# Standard molar entropy of formation of water (J/mol K)
LIQUID_WATER_SR = LIQUID_WATER_S - GAS_H_S - GAS_O_S/2

# Standard molar entropy of solid ice (J/mol K)
ICE_S = 0 # TODO: FIND THIS

# Standard molar entropy of formation of solid ice (J/mol K)
ICE_SR = ICE_S - GAS_H_S - GAS_O_S/2

# From https://www.engineeringtoolbox.com/specific-heat-capacity-water-d_660.html
# (J/mol K) at 0C
LIQUID_WATER_CP = 76.026

# From https://pubs.acs.org/doi/pdf/10.1021/ja01377a001 (page 331)
# Molality of NaCl vs heat capacity of solution
NACL_MOLAL_CP = {
    0.00: 0.9979,
    0.01: 0.9971,
    0.02: 0.9963,
    0.05: 0.9940,
    0.10: 0.9902,
    0.20: 0.9829,
    0.35: 0.9726,
    0.50: 0.9629,
    0.75: 0.9478,
    1.00: 0.9338,
    1.25: 0.9209,
    1.50: 0.9088,
    2.00: 0.8872,
    2.50: 0.8684
}

# Molarity of NaCl solution vs relative heat capacity of solution (Cp soln / Cp pure)
NACL_MOLAR_RELATIVE_CP = {
    key/(1000/18): val/NACL_MOLAL_CP[0.00] for key, val in NACL_MOLAL_CP.items()
}

# From https://www.engineeringtoolbox.com/ice-thermal-properties-d_576.html
# (J/mol K) at 0C
ICE_CP = {
    273: 2.050,
    268: 2.027,
    263: 2.000,
    258: 1.972,
    253: 1.943,
    248: 1.913
}