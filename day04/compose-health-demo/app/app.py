import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask App!"

@app.route('/health')  # ← ADD THIS HEALTH ENDPOINT
def health():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}, 200

if __name__ == '__main__':
    port = int(os.getenv("APP_PORT", 5000))
    app.run(host='0.0.0.0', port=port)