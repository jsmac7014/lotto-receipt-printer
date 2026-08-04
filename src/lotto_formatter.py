from datetime import datetime
from typing import List, Tuple

Line = Tuple[str, str]


def center(text: str, width: int) -> str:
    if len(text) >= width:
        return text
    left = (width - len(text)) // 2
    right = width - len(text) - left
    return " " * left + text + " " * right


def _header(columns: int) -> List[Line]:
    return [
        ("big_center", "Lotto 6/45"),
        ("normal_center", "Lucky Numbers"),
        ("normal_sep", "=" * columns),
    ]


def _format_line(numbers: List[int], index: int, columns: int) -> List[Line]:
    first = " ".join(f"{n:02d}" for n in numbers[:3])
    second = " ".join(f"{n:02d}" for n in numbers[3:])
    return [
        ("normal_left", f"A{index}"),
        ("big_center", first),
        ("big_center", second),
    ]



def format_lotto_ticket(
    numbers: List[List[int]],
    columns: int = 21,
) -> List[Line]:
    lines: List[Line] = _header(columns)
    lines.append(("normal_left", f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}"))
    lines.append(("blank", ""))

    for i, line in enumerate(numbers, start=1):
        lines.extend(_format_line(line, i, columns))

    lines.append(("normal_sep", "=" * columns))
    lines.append(("small_center", "Good luck!"))
    lines.append(("blank", ""))
    lines.append(("blank", ""))
    return lines
