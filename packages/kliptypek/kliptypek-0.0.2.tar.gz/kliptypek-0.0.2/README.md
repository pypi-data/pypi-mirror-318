# kliptypek

Clipboard typer. Insert text from clipboard using simulated typing.

# Start

Just copy needed text in clipboard and run:

```bash
kliptypek
```

Then focus needed window. There are 3 seconds for this by default, change it with flag `--delay_before` if needed.

# Installation

For `GNU/Linux` some package needed for `pyautogui`:

```bash
sudo pacman -S tk scrot
sudo apt install python3-tk scrot
```

```bash
pip3 install --upgrade pip
pip3 install kliptypek
```

There are flags to configure program behaviour. Type "--help" to see them. For example, you can use text not from clipboard with another timings:

```bash
kliptypek --help
kliptypek  --print_unicode_special
kliptypek --clip_text "c⌫kliptyper=←⌫k→)↵" --delay_between_up_down 1 --delay_between 100 --delay_before 2000
```
