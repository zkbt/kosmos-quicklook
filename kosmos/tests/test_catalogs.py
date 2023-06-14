from kosmos.catalogs import *
import os


def test_basic_catalog():
    d = os.path.dirname(__file__)
    filename = os.path.join(d, "test.tui")
    a = TUICatalog("test-again")
    a.from_TUI(filename)
    # print(a.table)
    a.to_TUI()
    b = TUICatalog()
    b.from_TUI("test-again.tui")
    # print(b.table)
