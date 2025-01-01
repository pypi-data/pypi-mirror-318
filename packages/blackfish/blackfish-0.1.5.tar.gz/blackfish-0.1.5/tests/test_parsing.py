from pathlib import Path

from blackfish.parsing import ir_spectrum, roots, soc_absorption_spectrum, soc_states

ROOT = Path(__file__).parent


def test_parsing_ir_spectrum():
    df = ir_spectrum(ROOT / "data/ir_spectrum.txt")
    assert len(df) == 237
    assert df.columns == [
        "mode",
        "frequency_cm",
        "epsilon",
        "intensity",
        "t2",
        "tx",
        "ty",
        "tz",
        "rel_intensity",
    ]


def test_parsing_roots():
    df = roots(ROOT / "data/roots.txt")
    assert len(df) == 180
    assert df.columns == [
        "root",
        "mult",
        "donor",
        "acceptor",
        "weight",
        "energy_cm",
    ]


def test_parsing_soc_absorption_spectrum():
    df = soc_absorption_spectrum(ROOT / "data/soc_absorption_spectrum.txt")
    assert len(df) == 64
    assert df.columns == [
        "state",
        "mult",
        "energy_ev",
        "energy_cm",
        "wavelength_nm",
        "osc_strength",
        "d2",
        "dx",
        "dy",
        "dz",
        "rel_intensity",
    ]


def test_parsing_soc_states():
    df = soc_states(ROOT / "data/soc_states.txt")
    assert len(df) == 9
    assert df.columns == [
        "state",
        "spin",
        "root",
        "weight",
        "energy_cm",
    ]
