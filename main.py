from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    port = os.getenv("PORT", "PORTが設定されていません")
    return f"<h1>動いたッ！</h1><p>ついに、このアプリは起動しました。Railwayが指定したポートは: {port} です。</p>"
