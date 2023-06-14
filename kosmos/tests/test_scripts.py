from kosmos.scripts import *


def test_basic_calibration_script():
    s = ScriptWriter()
    s.take_bias(n=5)
    for lamp in ["neon", "argon", "krypton"]:
        s.take_lamps(lamp, n=3)
    s.take_lamps("quartz", n=10)
    s.take_bias(n=5)
    s.print()
    s.copy()
