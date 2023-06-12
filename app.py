from flask import Flask, redirect, url_for, render_template, request
import pymysql
import pandas as pd
import snscrape.modules.twitter as sntwitter 

app = Flask(__name__, 
            static_url_path='',
            static_folder='public',)
app.secret_key = "sangatrahasia"
app.debug = True

def connect():    
    return pymysql.connect(host="localhost", user="root", password="", database="aplikasi_svm", charset='utf8mb4')

@app.route("/")
def home():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    con = connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM login")
    login = cursor.fetchall()
    return render_template('dashboard.html', login=login)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard/crawling', methods=('GET', 'POST'))
def dashboard_crawling():
    data_tweets = []
    if request.method == 'POST':
        kata_kunci = request.form['kata_kunci']
        jumlah_tweet = request.form['jumlah_tweet']
        maxTweets = int(jumlah_tweet)
        print("start scraping")
        cari_kata = kata_kunci + " since:2022-09-01 until:2023-01-01 lang:id"
        print(cari_kata)
        for tweet in sntwitter.TwitterSearchScraper(cari_kata).get_items():
            if len(data_tweets) == maxTweets :
                break
            else:
                data_tweets.append([tweet.date, tweet.user.username, tweet.content])
    return render_template('crawling.html', data_tweets=data_tweets)

@app.route('/dashboard/pre-processing')
def dashboard_preprocessing():
    return render_template('pre-processing.html')

@app.route('/dashboard/spell-correction')
def dashboard_spell_correction():
    return render_template('spell-correction.html')

@app.route('/dashboard/pembobotan-kata')
def dashboard_pembobotan_kata():
    return render_template('pembobotan-kata.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)