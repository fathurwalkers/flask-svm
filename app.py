from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, 
            static_url_path='',
            static_folder='public',)

app.debug = True

@app.route("/")
def home():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard/crawling')
def dashboard_crawling():
    return render_template('crawling.html')

@app.route('/dashboard/pre-processing')
def dashboard_preprocessing():
    return render_template('pre-processing.html')

@app.route('/dashboard/spell-correction')
def dashboard_spell_correction():
    return render_template('spell-correction.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)