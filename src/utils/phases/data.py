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
    prev = [i for i, item in enumerate(ordered_keys) if item < key][-1]
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

# Standard temperature (K)
STP_T = 298

# Standard pressure (Pa)
STP_P = 101325

# Molar concentration of pure water (mol/m^3)
LIQUID_WATER_MOLAR_CONC = 55.5e-3

# Standard molar enthalpy of formation (J/mol)
LIQUID_WATER_HF = -285830

# Standard molar entropy (J/mol K)
LIQUID_WATER_S = 69.95

# From https://www.engineeringtoolbox.com/specific-heat-capacity-water-d_660.html
# (J/mol K)
LIQUID_WATER_CP = {
    0:   76.026,
    10:  75.586,
    20:  75.386,
    25:  75.336,
    30:  75.309,
    40:  75.300,
    50:  75.334,
    60:  75.399,
    70:  75.491,
    80:  75.611,
    90:  75.763,
    100: 75.950,
    110: 76.177,
    120: 76.451,
    140: 77.155,
    160: 78.107,
    180: 79.360,
    200: 80.996,
    220: 83.137,
    240: 85.971,
    260: 89.821,
    280: 95.285,
    300: 103.60,
    320: 117.78,
    340: 147.88,
    360: 270.31
}

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
