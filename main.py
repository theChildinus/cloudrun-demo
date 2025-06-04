#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def post():
    try:
        return "<p>Hello, World!</p>"
    except Exception as e:
        print("[E] request except", e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
