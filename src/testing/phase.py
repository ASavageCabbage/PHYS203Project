from utils.phases.salt_water import Saltwater
from utils.phases.ice import Ice

def test_init_saltwater():
    n = 2
    T = 290
    sw = Saltwater(n, T)
    assert (n*sw.H_molar == sw.H)
    assert (n*sw.S_molar == sw.S)
    assert (n*sw.G_molar == sw.G)
    assert (sw.T == T)

def test_init_ice():
    n = 2
    T = 260
    ice = Ice(n, T)
    assert (n*ice.H_molar == ice.H)
    assert (n*ice.S_molar == ice.S)
    assert (n*ice.G_molar == ice.G)
    assert (ice.T == T)
