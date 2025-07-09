import os
from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# ★★★★★ ここにあなたのAPIキーを設定してください ★★★★★
# Railwayの環境変数からAPIキーを読み込むのが一番安全です
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    # POSTリクエスト（＝フォームが送信された）の場合
    if request.method == 'POST':
        try:
            # フォームからユーザーの入力内容を取得
            area = request.form.get('area')
            policy = request.form.get('policy')
            feature = request.form.get('feature')

            # AIへの指示（プロンプト）を作成
            prompt = f"""
            あなたは経験豊富な進路指導アドバイザーです。
            以下の条件に基づいて、日本の東京都内にある架空の学校を3つ提案してください。
            それぞれの学校について、ユニークで魅力的な名前と、具体的な特徴を考えてください。

            # 条件
            - 地域: {area}
            - 親の教育方針: {policy}
            - 学校に求める特徴: {feature}

            # 出力形式（必ずこの形式に従ってください）
            [
                {{"name": "学校名1", "area": "地域1", "feature": "特徴1"}},
                {{"name": "学校名2", "area": "地域2", "feature": "特徴2"}},
                {{"name": "学校名3", "area": "地域3", "feature": "特徴3"}}
            ]
            """

            # OpenAI APIを呼び出す
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは最高の進路アドバイザーです。"},
                    {"role": "user", "content": prompt}
                ]
            )

            # AIからの回答を処理
            # response_text は JSON 形式の文字列なので、Pythonのリストに変換する必要がある
            import json
            recommended_schools = json.loads(response.choices[0].message['content'])
            
            # 結果をWebページに渡して表示
            return render_template('index.html', schools=recommended_schools, user_inputs=request.form)

        except Exception as e:
            # エラーが発生した場合、エラーメッセージを表示する
            error_message = f"AIとの通信中にエラーが発生しました: {e}"
            return render_template('index.html', error=error_message)

    # GETリクエスト（＝初めてページを開いた）の場合
    return render_template('index.html')

if __name__ == '__main__':
    # Railwayでは使われないが、ローカルでのテスト用に残しておく
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
