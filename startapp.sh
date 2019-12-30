#!/bin/bash
export LOG_LEVEL="DEBUG"
export LOG_FORMAT="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
export LOG_DATE_FORMAT="%d-%m-%Y %H:%M:%S"
export APP_HASH="7E46581B89BA99E457820AC38C352177"
export DB_PATH="sqlite:///data.db"
export APP_PORT=5000
export APP_SECRET_KEY="marramiau"

python app.py
