# lotto

Lotto 6/45 lucky number generator and receipt printer for a thermal receipt printer.

## Files

- `lotto.py` — entry point
- `src/lotto_generator.py` — generate 6/45 lines
- `src/lotto_formatter.py` — format receipt-style output
- `src/printer.py` — ESC/POS printer driver
- `config.yaml` — printer and game settings

## Install

```bash
cd ~/lotto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

Dry-run (console output):

```bash
python3 lotto.py --dry-run
```

Print to the receipt printer:

```bash
python3 lotto.py
```

Generate 10 lines:

```bash
python3 lotto.py --lines 10
```

## Config

```yaml
printer:
  device: "/dev/usb/lp4"
  columns: 21
  cut: true

game:
  lines: 5
  grid_width: 7
```

## Cron example

```cron
0 8 * * 6 cd /home/jungwoos/lotto && /home/jungwoos/lotto/venv/bin/python lotto.py
```
