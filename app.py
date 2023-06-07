from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, 
            static_url_path='',
            static_folder='public',)

app.debug = True

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)