#!/usr/bin/bash
./generate.py -o test.xlsx -n 50000
/usr/bin/libreoffice --view ./test.xlsx
