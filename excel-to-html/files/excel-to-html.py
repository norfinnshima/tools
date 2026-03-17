from __future__ import annotations

import argparse
import html
from typing import TYPE_CHECKING, Any
from pathlib import Path

if TYPE_CHECKING:
    import pandas as pd


DEFAULT_INPUT = Path("test.xlsx")
DEFAULT_OUTPUT = Path("table.html")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Excel を HTML テーブル断片に変換します。"
    )
    parser.add_argument(
        "input",
        nargs="?",
        default=DEFAULT_INPUT,
        type=Path,
        help="入力する Excel ファイル。既定値は test.xlsx",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        type=Path,
        help="出力先 HTML ファイル。既定値は table.html",
    )
    parser.add_argument(
        "-s",
        "--sheet",
        default=0,
        help="読み込むシート名または 0 始まりのシート番号。既定値は 0",
    )
    return parser.parse_args()


def coerce_sheet(sheet: str) -> str | int:
    try:
        return int(sheet)
    except ValueError:
        return sheet


def is_empty_cell(value: object) -> bool:
    if value is None:
        return True

    if isinstance(value, float):
        return value != value

    return False


def normalize_value(value: object) -> str:
    if is_empty_cell(value):
        return ""

    escaped = html.escape(str(value))
    return escaped.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")


def build_rowspan_map(df: Any) -> list[list[int]]:
    row_count = len(df.index)
    col_count = len(df.columns)
    spans = [[1 for _ in range(col_count)] for _ in range(row_count)]

    for col_index in range(col_count):
        row_index = 0
        while row_index < row_count:
            value = df.iat[row_index, col_index]

            if is_empty_cell(value):
                spans[row_index][col_index] = 0
                row_index += 1
                continue

            span = 1
            next_row = row_index + 1
            while next_row < row_count and is_empty_cell(df.iat[next_row, col_index]):
                span += 1
                spans[next_row][col_index] = 0
                next_row += 1

            spans[row_index][col_index] = span
            row_index = next_row

    return spans


def render_table(df: Any) -> str:
    spans = build_rowspan_map(df)
    header_cells = "\n".join(
        f"        <th>{html.escape(str(column))}</th>" for column in df.columns
    )

    body_rows: list[str] = []
    for row_index in range(len(df.index)):
        cells: list[str] = []
        for col_index in range(len(df.columns)):
            span = spans[row_index][col_index]
            if span == 0:
                continue

            value = normalize_value(df.iat[row_index, col_index])
            rowspan_attr = f' rowspan="{span}"' if span > 1 else ""
            cells.append(f"        <td{rowspan_attr}>{value}</td>")

        body_rows.append("      <tr>\n" + "\n".join(cells) + "\n      </tr>")

    return "\n".join(
        [
            '<div class="table_wrap">',
            '  <table class="table">',
            "    <thead>",
            "      <tr>",
            header_cells,
            "      </tr>",
            "    </thead>",
            "    <tbody>",
            "\n".join(body_rows),
            "    </tbody>",
            "  </table>",
            "</div><!-- table_wrap -->",
            "",
        ]
    )


def main() -> None:
    args = parse_args()
    try:
        import pandas as pd
    except ImportError as error:
        raise SystemExit(
            "pandas が見つかりません。`pip install pandas openpyxl` を実行してください。"
        ) from error

    sheet = coerce_sheet(str(args.sheet))
    df = pd.read_excel(args.input, sheet_name=sheet)
    html_text = render_table(df)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_text, encoding="utf-8")


if __name__ == "__main__":
    main()
