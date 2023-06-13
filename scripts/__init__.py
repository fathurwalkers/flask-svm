from flask import Flask
from module import connect
import pandas as pd

app = Flask(__name__, 
            static_url_path='',
            static_folder='public',)
app.secret_key = "sangatrahasia"
app.debug = True

from .app import *