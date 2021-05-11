#!/bin/sh

BAUD=115200

DEVICE=/dev/ttyUSB0

COMMAND="sudo ./scripts/pyboard.py -b $BAUD -d $DEVICE"

$COMMAND -f cp src/main.py :main.py

$COMMAND -f rm util/__init__.py
$COMMAND -f rm util/wifi.py
$COMMAND -f rmdir util
$COMMAND -f mkdir util
$COMMAND -f cp src/util/__init__.py :util/__init__.py
$COMMAND -f cp src/util/wifi.py :util/wifi.py

$COMMAND -f rm mock/__init__.py
$COMMAND -f rm mock/gen_data.py
$COMMAND -f rmdir mock
$COMMAND -f mkdir mock
$COMMAND -f cp src/mock/__init__.py :mock/__init__.py
$COMMAND -f cp src/mock/gen_data.py :mock/gen_data.py

$COMMAND -f rm wifi/__init__.py
$COMMAND -f rm wifi/wifimgr.py
$COMMAND -f rmdir wifi
$COMMAND -f mkdir wifi
$COMMAND -f cp src/wifi/__init__.py :wifi/__init__.py
$COMMAND -f cp src/wifi/wifimgr.py :wifi/wifimgr.py
