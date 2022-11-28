# *-* coding: utf-8 *-*
#!/bin/python

__doc__ = """
# 1st Release   :      29th Nov 2022 (GMT+6)
# MiLocalShare  :      Local File Sharing Web Application
# Version       :      1.0
# Lisence       :      MIT
# Copyright (C) 2022 InferiorAK\n"""


"""MIT License

Copyright (c) 2022 Mi Taseen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from res import *
from res import __version__

app = engine.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload():
    engine.engine()
    return engine.render_template("index.html")


if __name__ == "__main__":
    if arg.args.version:
        print(f"MiLocalShare {__version__}")
    else:
        print(__doc__)
        app.run(debug=True, host="0.0.0.0", port=arg.args.port)
