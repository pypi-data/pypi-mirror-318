from pathlib import Path

import polars as pl


def ir_spectrum(orca_output: Path) -> pl.DataFrame:
    lines = Path(orca_output).read_text().splitlines()

    TABLE_HEADER = "IR SPECTRUM"
    TABLE_HEADER_OFFSET = 6

    table_start_idx = next(
        i for i, line in enumerate(lines) if TABLE_HEADER in line.strip()
    )
    table_start_idx += TABLE_HEADER_OFFSET

    # Collect table
    rows = []
    for row in lines[table_start_idx:]:
        # Stop on empty line
        if not row.strip():
            break

        rows.append(row)

    print(rows)

    processed_rows = [
        row.replace(":", "").replace("(", "").replace(")", "").strip().split()
        for row in rows
    ]

    df = pl.DataFrame(
        processed_rows,
        orient="row",
        schema={
            "mode": pl.Int64,
            "frequency_cm": pl.Float64,
            "epsilon": pl.Float64,
            "intensity": pl.Float64,
            "t2": pl.Float64,
            "tx": pl.Float64,
            "ty": pl.Float64,
            "tz": pl.Float64,
        },
    )

    df = df.with_columns(
        (pl.col("intensity") / pl.col("intensity").max()).alias("rel_intensity")
    )

    return df
