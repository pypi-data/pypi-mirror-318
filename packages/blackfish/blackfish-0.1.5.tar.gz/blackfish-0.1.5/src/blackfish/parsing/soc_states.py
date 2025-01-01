from pathlib import Path
from typing import Iterator

import polars as pl


def soc_states(orca_output: Path) -> pl.DataFrame:
    """Parse SOC states from ORCA output into a Polars DataFrame."""
    # Read file content
    content = Path(orca_output).read_text().splitlines()

    # Find the start of SOC states section
    try:
        start_idx = (
            next(
                i
                for i, line in enumerate(content)
                if "Eigenvectors of the SOC matrix:" in line.strip()
            )
            + 3
        )
    except StopIteration:
        raise ValueError("SOC matrix section not found in input")

    # Parse states
    soc_states = []
    for state_lines in _iter_soc_states(content[start_idx:]):
        state_data = _parse_single_state(state_lines)

        # Flatten the data structure
        for root in state_data["roots"]:
            soc_states.append(
                {
                    "state": state_data["state"],
                    "energy_cm": state_data["energy_cm"],
                    **root,
                }
            )

    # Create and transform DataFrame
    df = pl.DataFrame(soc_states)
    return (
        df.group_by(["state", "spin"])
        .agg([pl.first("root"), pl.sum("weight"), pl.first("energy_cm")])
        .sort(["state", "weight"], descending=[False, True])
    )


def _parse_single_state(state_lines: list[str]) -> dict:
    """Parse a single SOC state block into a dictionary.

    Example input format:
    STATE 1: 0.000000
       1.000000    1.000000    0.000000     1    1    1
       0.000000    0.000000    0.000000     2    1    0
    """
    # Parse header line
    header = state_lines[0].strip()
    state_num = int(header[5 : header.index(":")])
    energy = float(header[header.index(":") + 1 :])

    # Parse root contributions
    roots = []
    for line in state_lines[1:]:
        parts = line.replace(":", "").strip().split()
        roots.append(
            {
                "weight": float(parts[0]),
                "real": float(parts[1]),
                "imag": float(parts[2]),
                "root": int(parts[3]),
                "spin": int(parts[4]),
                "ms": int(parts[5]),
            }
        )

    return {"state": state_num, "energy_cm": energy, "roots": roots}


def _iter_soc_states(lines: list[str]) -> Iterator[list[str]]:
    """Iterate over SOC state blocks in the input text."""
    current_state = []

    for line in lines:
        line = line.strip()
        if not line:
            break

        if line.startswith("STATE"):
            if current_state:
                yield current_state
            current_state = [line]
        elif current_state:
            current_state.append(line)

    if current_state:  # Don't forget the last state
        yield current_state
