import argparse
import logging
import sys
from pathlib import Path
from typing import Any, Dict

import yaml

sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.lotto_formatter import format_lotto_ticket
from src.lotto_generator import generate_lines
from src.printer import print_receipt, print_to_console

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main(config_path: str, dry_run: bool = False, lines: int = None) -> int:
    try:
        config = load_config(config_path)
    except Exception as exc:
        logger.error("Failed to load config: %s", exc)
        return 1

    printer_config = config.get("printer", {})
    game_config = config.get("game", {})
    line_count = lines if lines is not None else game_config.get("lines", 5)
    columns = printer_config.get("columns", 21)

    numbers = generate_lines(line_count)
    receipt_lines = format_lotto_ticket(
        numbers,
        columns=columns,
    )

    if dry_run:
        print_to_console(receipt_lines)
        logger.info("Dry-run finished.")
        return 0

    try:
        print_receipt(receipt_lines, printer_config)
        logger.info("Lotto ticket printed.")
    except Exception as exc:
        logger.error("Print failed: %s", exc)
        return 1

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lotto 6/45 receipt printer")
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to config file (default: config.yaml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print to console instead of the physical printer",
    )
    parser.add_argument(
        "--lines",
        type=int,
        help="Override number of lines to generate",
    )
    args = parser.parse_args()

    sys.exit(main(args.config, args.dry_run, args.lines))
