from flask import Flask, render_template, request

app = Flask(__name__)

# 问卷问题
survey_questions = [
    {"id": 1, "question": "曾涛的手机号码是什么?", "type": "text"},
    {"id": 2, "question": "曾涛的性别是什么？", "type": "radio", "options": ["男", "女"]},
    {"id": 3, "question": "曾涛是Gay吗？", "type": "radio", "options": ["是", "否", "不确定"]},
    {"id": 4, "question": "曾涛的年龄是多少？", "type": "number"},
    {"id": 5, "question": "曾涛的职业是什么？", "type": "text"},
]

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        return render_template('thank_you.html')
    return render_template('survey.html', questions=survey_questions)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

# Vercel 需要这个
application = app.wsgi_app 