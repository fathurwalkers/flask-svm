from flask import Flask
# import module
import pandas as pd
import pymysql

app = Flask(__name__, 
            static_url_path='',
            static_folder='public',)
app.secret_key = "sangatrahasia"
app.debug = True

def connect():    
    return pymysql.connect(host="localhost", user="root", password="", database="aplikasi_svm", charset='utf8mb4')

from scripts.src import *