# LED Matrix documentation

## Installation

### Python 3

```shell
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)
```

### Clone Github repository
```shell
git clone https://github.com/CER418/electric-energy-consumption.git
```

### Create cronjob
```shell
cat <(crontab -l) <(python rpi-rgb-led-matrix/bindings/python/samples/elspot.py --led-slowdown-gpio 3) | crontab -
```


Feel free to make a pull request (:
