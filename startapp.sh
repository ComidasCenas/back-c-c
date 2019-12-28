#!/bin/bash
export LOG_LEVEL="DEBUG"
export LOG_FORMAT="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
export LOG_DATE_FORMAT="%d-%m-%Y %H:%M:%S"
python app.py