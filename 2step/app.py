from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from random import randint

app = Flask(__name__)
app.secret_key = 'your_secret_key'

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'njeiz2050@gmail.com'
app.config['MAIL_PASSWORD'] = '14921254'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup form submission
        email = request.form['email']
        # You can add more signup validations here
        otp = str(randint(100000, 999999))

        msg = Message('OTP for Two-Step Verification', sender='your_email@gmail.com', recipients=[email])
        msg.body = f'Your OTP is: {otp}'
        mail.send(msg)

        return render_template('verify.html', email=email)
    else:
        return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']

    # Check if email is valid (e.g., in a database)
    if email:
        otp = str(randint(100000, 999999))

        msg = Message('OTP for Two-Step Verification', sender='your_email@gmail.com', recipients=[email])
        msg.body = f'Your OTP is: {otp}'
        mail.send(msg)

        return render_template('verify.html', email=email)
    else:
        flash('Invalid email')
        return redirect(url_for('home'))

@app.route('/verify', methods=['POST'])
def verify():
    otp = request.form['otp']

    # Check if OTP is valid (e.g., match with the sent OTP)
    if otp == '123456':  # Replace '123456' with the actual OTP sent
        flash('Login successful!')
        return redirect(url_for('home'))
    else:
        flash('Invalid OTP')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
