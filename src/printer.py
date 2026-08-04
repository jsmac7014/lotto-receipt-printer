import logging
from typing import Dict, List, Tuple

from escpos.exceptions import Error as EscposError
from escpos.printer import File

logger = logging.getLogger(__name__)

Line = Tuple[str, str]


def build_printer(printer_config: Dict) -> File:
    device = printer_config.get("device", "/dev/usb/lp4")
    return File(devfile=device)


def _apply_style(printer, style: str) -> None:
    if style == "big_center":
        printer.set(
            align="center",
            bold=True,
            double_height=False,
            double_width=False,
            custom_size=True,
            width=2,
            height=2,
        )
    elif style == "normal_center":
        printer.set(
            align="center",
            bold=False,
            double_height=False,
            double_width=False,
            custom_size=True,
            width=1,
            height=1,
        )
    elif style == "normal_left":
        printer.set(
            align="left",
            bold=False,
            double_height=False,
            double_width=False,
            custom_size=True,
            width=1,
            height=1,
        )
    elif style == "normal_sep":
        printer.set(
            align="center",
            bold=False,
            double_height=False,
            double_width=False,
            custom_size=True,
            width=1,
            height=1,
        )
    elif style == "small_center":
        printer.set(
            align="center",
            bold=False,
            double_height=False,
            double_width=False,
            custom_size=True,
            width=1,
            height=1,
        )


def print_receipt(lines: List[Line], printer_config: Dict) -> None:
    try:
        p = build_printer(printer_config)
    except EscposError as exc:
        logger.error("Printer connection failed: %s", exc)
        raise

    try:
        p.codepage = "CP437"
        for style, text in lines:
            if style == "blank":
                p.text("\n")
                continue
            _apply_style(p, style)
            p.text(text + "\n")
        p.text("\n\n")
        if printer_config.get("cut", True):
            try:
                p.cut()
            except Exception as exc:
                logger.warning("Cut failed: %s", exc)
        p.close()
    except Exception as exc:
        logger.error("Error during printing: %s", exc)
        raise


def print_to_console(lines: List[Line]) -> None:
    for style, text in lines:
        if style == "blank":
            print("")
        else:
            print(text)
