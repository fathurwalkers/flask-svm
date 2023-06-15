from flask import redirect, url_for, render_template, request, session
import snscrape.modules.twitter as sntwitter 
import datetime
import re
from cleantext import clean
import random
import string

from scripts import app, connect

def cek_session():
    status_session = None
    session_user = session.get('login')
    if session_user == None:
        return False
    else:
        return True

def cleaning_crawling(text):
    cleaningstring = re.sub('[^A-Za-z0-9]+', ' ', text)
    return cleaningstring
    # return (
    #     text.replace("&", '').
    #     replace('"', '').
    #     replace("'", "").
    #     replace('?', '').
    #     replace(',', '').
    #     replace("<", "").
    #     replace(">", "").
    #     replace(":", "").
    #     replace("/", "").
    #     replace('\\', "").
    #     replace("(", '').
    #     replace(")", '').
    #     replace("{", '').
    #     replace("}", '').
    #     replace("@", "").
    #     replace("? s'", "")
    # )

@app.route("/")
def home():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    con = connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM login")
    login = cursor.fetchall()
    return render_template('dashboard.html', login=login)

@app.route('/login', methods=('GET', 'POST'))
def login():
    username = None
    password = None
    users = None
    ceksession = cek_session()
    if ceksession == True:
        return redirect(url_for('dashboard'))
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        query = "SELECT * FROM login WHERE login_username='" + username +"'"
        con = connect()
        cursor = con.cursor()
        cursor.execute(query)
        users = cursor.fetchone()
        if users: 
            if ceksession == False:
                session['login'] = username
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('dashboard'))
        else:
            users = "User Kosong"
    return render_template('login.html', username=username, password=password, users=users, cek_session=ceksession)

@app.route('/logout', methods=('POST', 'GET'))
def logout():
    if request.method == 'POST':
        session['login'] = None
        return redirect(url_for('login'))

@app.route('/dashboard/crawling', methods=('GET', 'POST'))
def dashboard_crawling():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    con = connect()
    cursor = con.cursor()
    date_tweet = None
    text_crawling = None
    cleaning_text_crawling = None
    cleaningemoji = None
    input_query = None
    random_strings = None
    cek_prefix = None
    data_tweets = []

    if request.method == 'POST':
        kata_kunci = request.form['kata_kunci']
        jumlah_tweet = request.form['jumlah_tweet']
        tanggal_dari = request.form['tanggal_dari']
        tanggal_sampai = request.form['tanggal_sampai']
        maxTweets = int(jumlah_tweet)
        cari_kata = kata_kunci + " since:" + tanggal_dari + " until:" + tanggal_sampai + " lang:id"

        random_strings = 'prefixes' + ''.join(random.choice(string.ascii_lowercase) for kkk in range(5))
        prefix_query = "INSERT INTO prefix (prefix_kode) VALUES ('" + random_strings + "')"
        prefix = cursor.execute(prefix_query)

        for tweet in sntwitter.TwitterSearchScraper(cari_kata).get_items():
            if len(data_tweets) == maxTweets :
                break
            else:
                date_tweet = datetime.datetime.strftime(tweet.date, "%d/%m/%Y")
                user_tweet = tweet.user.username
                isi_tweet = tweet.content
                tanggal_tweet = tweet.date
                text_crawling = tweet.content
                cleaningemoji = clean(text_crawling, no_emoji=True)
                cleaning_text_crawling = cleaning_crawling(cleaningemoji)
                input_query = "INSERT INTO crawling (user_tweet, isi_tweet, tanggal_tweet, prefix_crawling) VALUES ('" + user_tweet + "','" + cleaning_text_crawling + "','" + date_tweet + "','" + random_strings + "')"
                input_crawling = cursor.execute(input_query)
                con.commit()
                data_tweets.append([tweet.date, tweet.user.username, tweet.content])
    return render_template('crawling.html', data_tweets=data_tweets, date_tweet=date_tweet, text_crawling=text_crawling, cleaning_text_crawling=cleaning_text_crawling, cleaningemoji=cleaningemoji, input_query=input_query, cek_prefix=random_strings)

@app.route('/dashboard/pre-processing/<prefix>', methods=('GET', 'POST'))
def dashboard_preprocessing(prefix):
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    cek_prefix = prefix
    preprocessing = None

    if cek_prefix == None:
        return render_template('pre-processing.html', cek_prefix=cek_prefix, preprocessing=preprocessing)
    else:
        query_all_crawling = "SELECT * FROM crawling WHERE prefix_crawling='" + cek_prefix + "'"
        con = connect()
        cursor = con.cursor()
        cursor.execute(query_all_crawling)
        preprocessing = cursor.fetchall()
    return render_template('pre-processing.html', cek_prefix=cek_prefix, preprocessing=preprocessing)


@app.route('/dashboard/spell-correction')
def dashboard_spell_correction():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    return render_template('spell-correction.html')

@app.route('/dashboard/pembobotan-kata')
def dashboard_pembobotan_kata():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    return render_template('pembobotan-kata.html')

@app.route('/dashboard/prefix')
def prefix():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))

    con = connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM prefix")
    prefixes = cursor.fetchall()

    return render_template('prefix.html', prefixes=prefixes)