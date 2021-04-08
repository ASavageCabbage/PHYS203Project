from utils.phases.ice import Ice
from utils.phases.water import Water
from utils.phases.salt import Salt

def test_init_ice():
    n = 2
    T = 260
    ice = Ice(n, T)
    assert (n*ice.H_molar == ice.H)
    assert (n*ice.S_molar == ice.S)
    assert (n*ice.G_molar == ice.G)
    assert (ice.T == T)

def test_init_water():
    n = 2
    T = 320
    water = Water(n, T)
    assert (n*water.H_molar == water.H)
    assert (n*water.S_molar == water.S)
    assert (n*water.G_molar == water.G)
    assert (water.T == T)

def test_init_salt():
    n = 2
    T = 320
    salt = Salt(n, T)
    assert (n*salt.H_molar == salt.H)
    assert (n*salt.S_molar == salt.S)
    assert (n*salt.G_molar == salt.G)
    assert (salt.T == T)
