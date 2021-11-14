#!/usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient
from flask import Flask

import time


app = Flask(__name__)
@app.route('/')

# ======== Routing =========================================================== #
def read_lights():
	red = "1"
	green = "0"
	return(red, green)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")