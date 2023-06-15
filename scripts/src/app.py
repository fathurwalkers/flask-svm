from flask import redirect, url_for, render_template, request, session
import snscrape.modules.twitter as sntwitter 
import datetime

from scripts import app, connect

def cek_session():
    status_session = None
    session_user = session.get('login')
    if session_user == None:
        return False
    else:
        return True

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

@app.route('/dashboard/crawling', methods=('GET', 'POST'))
def dashboard_crawling():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    con = connect()
    cursor = con.cursor()
    date_tweet = None
    data_tweets = []
    if request.method == 'POST':
        kata_kunci = request.form['kata_kunci']
        jumlah_tweet = request.form['jumlah_tweet']
        tanggal_dari = request.form['tanggal_dari']
        tanggal_sampai = request.form['tanggal_sampai']
        maxTweets = int(jumlah_tweet)
        cari_kata = kata_kunci + " since:" + tanggal_dari + " until:" + tanggal_sampai + " lang:id"
        for tweet in sntwitter.TwitterSearchScraper(cari_kata).get_items():
            if len(data_tweets) == maxTweets :
                break
            else:
                date_tweet = datetime.datetime.strftime(tweet.date, "%d/%m/%Y %H:%M:%S")
                user_tweet = tweet.user.username
                isi_tweet = tweet.content
                tanggal_tweet = tweet.date

                input_query = "INSERT INTO crawling (user_tweet, isi_tweet, tanggal_tweet) VALUES (" + user_tweet + "," + isi_tweet + "," + tanggal_tweet + ")" 
                input_crawling = cursor.execute(input_query)
                data_tweets.append([tweet.date, tweet.user.username, tweet.content])
        cursor.execute("SELECT * FROM prefix")
    return render_template('crawling.html', data_tweets=data_tweets, date_tweet=date_tweet)

@app.route('/dashboard/pre-processing')
def dashboard_preprocessing():
    ceksession = cek_session()
    if ceksession == False:
        return redirect(url_for('login'))
    return render_template('pre-processing.html')

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