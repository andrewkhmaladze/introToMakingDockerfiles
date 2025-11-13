import os
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    app_env = os.getenv("APP_ENV", "undefined")
    message = os.getenv("WELCOME_MSG", "Hello from Docker Compose!")
    return f"Environment: {app_env} <br> Message: {message}"
 
if __name__ == '__main__':
    port = int(os.getenv("APP_PORT", 5000))
    app.run(host='0.0.0.0', port=port)