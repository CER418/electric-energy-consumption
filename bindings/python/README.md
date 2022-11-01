# LED Matrix documentation

### Python 3
You can also build for Python 3:

```shell
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)
```


To use different wiring without recompiling the library to change the default,
you can use `--led-gpio-mapping` (or `-m`). For example, to use Adafruit HAT:
```bash
cat >> p
sudo ./runtext.py --led-gpio-mapping=adafruit-hat
```


