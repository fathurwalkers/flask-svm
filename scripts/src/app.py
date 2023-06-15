from flask import redirect, url_for, render_template, request, session
import snscrape.modules.twitter as sntwitter 
import datetime
import re
from cleantext import clean

from scripts import app, connect

def cek_session():
    status_session = None
    session_user = session.get('login')
    if session_user == None:
        return False
    else:
        return True

def cleaning_crawling(text):
    return (
        text.replace("&", '').
        replace('"', '').
        replace("'", "").
        replace('?', '').
        replace(',', '').
        replace("<", "").
        replace(">", "").
        replace(":", "").
        replace("/", "").
        replace('\\', "").
        replace("(", '').
        replace(")", '').
        replace("{", '').
        replace("}", '').
        replace("@", "").
        replace("? s'", "")
    )

# def cleaning_emoji(data):
#     emoj = re.compile("["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#         u"\U00002500-\U00002BEF"  # chinese char
#         u"\U00002702-\U000027B0"
#         u"\U00002702-\U000027B0"
#         u"\U000024C2-\U0001F251"
#         u"\U0001f926-\U0001f937"
#         u"\U00010000-\U0010ffff"
#         u"\u2640-\u2642" 
#         u"\u2600-\u2B55"
#         u"\u200d"
#         u"\u23cf"
#         u"\u23e9"
#         u"\u231a"
#         u"\ufe0f"  # dingbats
#         u"\u3030""]+", re.UNICODE)
#     return re.sub(emoj, '', data)

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
    text_crawling = None
    cleaning_text_crawling = None
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

                text_crawling = tweet.content

                # clean(text, no_emoji=True)
                cleaningemoji = clean(text_crawling, no_emoji=True)
                cleaning_text_crawling = cleaning_crawling(cleaningemoji)

                input_query = "INSERT INTO crawling (user_tweet, isi_tweet, tanggal_tweet) VALUES (" + user_tweet + "," + cleaning_text_crawling + "," + date_tweet + ")" 
                input_crawling = cursor.execute(input_query)

                data_tweets.append([tweet.date, tweet.user.username, tweet.content])
        cursor.execute("SELECT * FROM prefix")
    return render_template('crawling.html', data_tweets=data_tweets, date_tweet=date_tweet, text_crawling=text_crawling, cleaning_text_crawling=cleaning_text_crawling, cleaningemoji=cleaningemoji)

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