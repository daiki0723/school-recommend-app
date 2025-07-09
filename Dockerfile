# 1. ベースとなるPython環境を準備
FROM python:3.10-slim

# 2. 作業ディレクトリを設定
WORKDIR /app

# 3. リポジトリのすべてのファイルを、この作業ディレクトリにコピーする
# (main.py, templatesフォルダなどが全部コピーされる、一番確実な方法です)
COPY . .

# 4. 必要な部品（Flask, gunicorn, openai）をインストールする
RUN pip install --no-cache-dir Flask gunicorn openai

# 5. アプリを起動するコマンド
# (Railwayが自動で$PORTを設定してくれるので、それに合わせます)
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "main:app"]
