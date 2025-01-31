from flask import Flask, request, render_template_string, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# مسیر فایل کاربران
USERS_FILE = 'users.txt'

# بررسی وجود فایل و ایجاد آن در صورت نیاز
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as file:
        file.write("alireza:mrhjf5780\n")  # یوزر پیش‌فرض

# تابع برای خواندن کاربران از فایل
def load_users():
    users = {}
    with open(USERS_FILE, 'r') as file:
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
    return users

# تابع برای افزودن کاربر جدید به فایل
def add_user(username, password):
    with open(USERS_FILE, 'a') as file:
        file.write(f"{username}:{password}\n")

# قالب HTML
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #fafafa;
            font-family: Arial, sans-serif;
        }
        .card {
            border-radius: 8px;
        }
        h3 {
            font-family: 'Billabong', cursive;
            font-size: 2rem;
            color: #262626;
        }
    </style>
</head>
<body>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card p-4 shadow-sm" style="width: 350px;">
            <h3 class="text-center mb-3">Instagram</h3>
            {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
            <div class="alert {{ messages[0][0] }} alert-dismissible fade show" role="alert">
                {{ messages[0][1] }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            {% endif %}
            {% endwith %}
            <form action="/login" method="POST">
                <div class="mb-3">
                    <input type="text" name="username" class="form-control" placeholder="Username" required>
                </div>
                <div class="mb-3">
                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Log In</button>
            </form>
            <p class="text-center mt-3">Don't have an account? <a href="/signup">Sign up</a></p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

signup_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Sign Up</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #fafafa;
            font-family: Arial, sans-serif;
        }
        .card {
            border-radius: 8px;
        }
        h3 {
            font-family: 'Billabong', cursive;
            font-size: 2rem;
            color: #262626;
        }
    </style>
</head>
<body>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card p-4 shadow-sm" style="width: 350px;">
            <h3 class="text-center mb-3">Instagram</h3>
            {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
            <div class="alert {{ messages[0][0] }} alert-dismissible fade show" role="alert">
                {{ messages[0][1] }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            {% endif %}
            {% endwith %}
            <form action="/signup" method="POST">
                <div class="mb-3">
                    <input type="text" name="username" class="form-control" placeholder="Choose a Username" required>
                </div>
                <div class="mb-3">
                    <input type="password" name="password" class="form-control" placeholder="Choose a Password" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Sign Up</button>
            </form>
            <p class="text-center mt-3">Already have an account? <a href="/">Log in</a></p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    users = load_users()  # بارگذاری کاربران از فایل

    if username in users and users[username] == password:
        flash('Success! Login successful.', 'alert-success')
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password.', 'alert-danger')
        return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()  # بارگذاری کاربران از فایل

        if username in users:
            flash('Username already exists.', 'alert-danger')
        else:
            add_user(username, password)  # افزودن کاربر جدید به فایل
            flash('Account created successfully! You can now log in.', 'alert-success')
            return redirect(url_for('home'))

    return render_template_string(signup_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
