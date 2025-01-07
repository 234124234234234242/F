from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于flash消息

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
        try:
            answers = {}
            # 检查所有问题是否都已回答
            all_answered = True
            for question in survey_questions:
                answer = request.form.get(str(question['id']))
                if not answer:
                    all_answered = False
                    break
                answers[question['id']] = answer
            
            if not all_answered:
                flash('请回答所有问题后再提交！')
                return redirect(url_for('survey'))
            
            # 在 Vercel 环境中，我们暂时只打印答案而不保存
            print("收到的答案:", answers)
            return render_template('thank_you.html')
        except Exception as e:
            print(f"Error: {str(e)}")  # 添加错误日志
            flash('提交失败，请重试！')
            return redirect(url_for('survey'))
    
    return render_template('survey.html', questions=survey_questions)

# Vercel 需要这个
app.debug = False

# 添加这个处理函数
def handler(event, context):
    return app

if __name__ == '__main__':
    app.run() 