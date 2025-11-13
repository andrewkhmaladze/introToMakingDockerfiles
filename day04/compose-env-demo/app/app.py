import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    app_env = os.getenv("APP_ENV", "undefined")
    message = os.getenv("WELCOME_MSG", "Hello from Docker Compose!")
    color = os.getenv("COLOR", "black")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Force blue color with strong styling
    if color == "blue":
        styled_message = f'<span style="color: blue !important; font-weight: bold; font-size: 28px; background-color: yellow; padding: 10px;">{message} - BLUE VERSION</span>'
    else:
        styled_message = f'<span style="color: {color}; font-size: 20px;">{message}</span>'
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Color Test</title>
        <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Expires" content="0">
    </head>
    <body>
        <h1>Environment: {app_env}</h1>
        <h2>Message: {styled_message}</h2>
        <p>Color setting: <strong>{color}</strong></p>
        <p>Last updated: {timestamp}</p>
        <p>Debug - COLOR env var: '{color}'</p>
        <hr>
        <p>If you don't see blue text with yellow background, your browser is caching!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.getenv("APP_PORT", 5000))
    app.run(host='0.0.0.0', port=port)