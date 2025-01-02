import os
from django.utils.termcolors import make_style

bold_yellow = make_style(opts=("bold",), fg="yellow")

if os.environ.get("RUN_MAIN"):
    print(bold_yellow("Hello from main thread!!!"))
