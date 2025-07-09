# 1. ベースとなるPython環境を準備
FROM python:3.10-slim

# 2. 作業ディレクトリを設定
WORKDIR /app

# 3. 必要な部品リストをコピー
COPY main.py templates/ ./
COPY templates/ ./templates/

# 4. 必要な部品（Flaskとgunicorn）をインストール
RUN pip install Flask gunicorn

# 5. アプリが使うドア（ポート）を知らせる
EXPOSE 8080

# 6. アプリを起動するコマンド（環境変数を読み込む）
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 main:app
