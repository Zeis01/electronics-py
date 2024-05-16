import math

def getVolt(watt: float, amper: float) -> float:
    return watt / amper
def getAmper(coulomb: float, seconds: float) -> float:
    return coulomb / seconds
def getOhm(volt: float, amper: float) -> float:
    return volt / amper
def getFarad(coulomb: float, volt: float) -> float:
    return coulomb / volt
def getdBm(miliwatt: float) -> float:
    return 10 * math.log10(miliwatt/1)
def getConductance(resistance: float) -> float:
    return 1 / resistance
def getDeviceEfficiency(power_in: float, power_out: float) -> float:
    return power_out / power_in * 100
def getFrequency(hz: float) -> float:
    return 1 / hz
def getStreamMagneticAssociated(stream: float, number_of_turns: float) -> float:
    return stream * number_of_turns
def getInductance(weber: float, amper: float) -> float:
    return weber / amper
def getPulsation(frequency: float) -> float:
    return frequency * 2 * math.pi
def getReactanceCapacitive(frequency: float, capacitor_capacity: float) -> float:
    return 1 / (2 * math.pi * frequency * capacitor_capacity)
def getPower(volt: float, amper: float) -> float:
    return volt * amper
def getMagneticStream(magnetic_induction: float, area: float) -> float:
    return magnetic_induction * area
def getMagneticFieldStrength(magnetic_induction: float, permeability_magnetic_environment: float) -> float:
    return magnetic_induction / permeability_magnetic_environment
