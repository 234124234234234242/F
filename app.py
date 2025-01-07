from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
        answers = {}
        for question in survey_questions:
            answer = request.form.get(str(question['id']))
            answers[question['id']] = answer
        return render_template('thank_you.html')
    return render_template('survey.html', questions=survey_questions)

# Vercel 需要这个
def app_handler(event, context):
    return app.wsgi_app

app.debug = False

if __name__ == '__main__':
    app.run() 