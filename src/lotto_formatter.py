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
        ("normal_sep", "-" * columns),
    ]


def _format_line(numbers: List[int], index: int, columns: int) -> List[Line]:
    label = f"A{index}"
    nums = [f"{n:02d}" for n in numbers]
    # Minimum length: label + space + numbers with single spaces between them.
    min_len = len(label) + 1 + sum(len(n) for n in nums) + (len(nums) - 1)
    extra = max(0, columns - min_len)
    gaps = len(nums) - 1
    # Start with one space between each number, then spread remaining spaces
    # outward from the center so gaps stay visually balanced.
    spaces = [1] * gaps
    left = gaps // 2 - 1
    right = gaps // 2
    for _ in range(extra):
        if right < gaps:
            spaces[right] += 1
            right += 1
        elif left >= 0:
            spaces[left] += 1
            left -= 1

    parts = [label, " "]
    for i, n in enumerate(nums):
        parts.append(n)
        if i < gaps:
            parts.append(" " * spaces[i])
    return [("medium_left", "".join(parts))]



def format_lotto_ticket(
    numbers: List[List[int]],
    columns: int = 21,
) -> List[Line]:
    lines: List[Line] = _header(columns)
    lines.append(("normal_left", f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}"))
    lines.append(("blank", ""))

    for i, line in enumerate(numbers, start=1):
        lines.extend(_format_line(line, i, columns))

    lines.append(("normal_sep", "-" * columns))
    lines.append(("small_center", "Good luck!"))
    lines.append(("blank", ""))
    lines.append(("blank", ""))
    return lines
