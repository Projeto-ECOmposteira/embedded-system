[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Projeto-ECOmposteira_embedded-system&metric=alert_status)](https://sonarcloud.io/dashboard?id=Projeto-ECOmposteira_embedded-system)
[![Maintainability](https://api.codeclimate.com/v1/badges/3f1dc044c3d0714f59d5/maintainability)](https://codeclimate.com/github/Projeto-ECOmposteira/embedded-system/maintainability)

# Sistema embarcado (ESP32)

## Instalação

### ESP32

Primeramente baixe um [binário do micro python](https://micropython.org/download/esp32/)

Após isso realize os seguintes passos:

```bash
pip3 install esptool
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 <binary path>
```


### Dependências da ESP32

Configure a [network](http://docs.micropython.org/en/latest/esp32/quickref.html#networking) da sua ESP32 e use o comando baixo via acesso 
serial ao controlador.

```python3
import upip
upip.install("micropython-umqtt.simple2")
```

### Conexão Serial

```bash
picocom /dev/ttyUSB0 -b115200
```

