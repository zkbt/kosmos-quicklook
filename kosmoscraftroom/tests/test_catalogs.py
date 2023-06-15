from kosmoscraftroom.catalogs import *
import os


def test_basic_catalog():
    d = os.path.dirname(__file__)

    # make a tiny catalog
    names = ["A", "B", "C"]
    coordinates = SkyCoord(ra=[1, 2, 3] * u.hourangle, dec=[-1, 0, 1] * u.deg)
    table = Table(dict(names=names, sky_coordinates=coordinates))
    tiny = TUICatalog("random-tiny-test")
    tiny.from_table(table)

    # write it out and try to reload it
    tiny.to_TUI()
    new = TUICatalog("reloaded-tiny-test")
    new.from_TUI("random-tiny-test.tui")

    # cleanupt
    os.remove("random-tiny-test.tui")
