from flask import Flask, request, render_template

app = Flask(__name__)

# ダミーの学校データ
dummy_schools = [
    {"name": "架空学園中学校", "area": "東京都千代田区", "feature": "最先端のICT教育が特徴です。"},
    {"name": "空想義塾高等学校", "area": "東京都渋谷区", "feature": "グローバルな視野を育む国際交流が盛んです。"},
    {"name": "夢見台小学校", "area": "東京都世田谷区", "feature": "自然豊かな環境でのびのびと学べます。"},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_schools = []
    if request.method == 'POST':
        # 本当はここでAIレコメンドをするが、今はダミーデータを返すだけ
        area = request.form.get('area')
        if area == "東京都":
            recommended_schools = dummy_schools

    return render_template('index.html', schools=recommended_schools)

if __name__ == '__main__':
    app.run(debug=True)
