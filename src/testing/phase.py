from utils.phases.salt_water import Saltwater

def test_init_saltwater():
    n = 2
    sw = Saltwater(n)
    assert (n*sw.U_molar == sw.U)
    assert (n*sw.S_molar == sw.S)
    assert (n*sw.G_molar == sw.G)
